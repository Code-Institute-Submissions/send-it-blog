import os
import datetime
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["IMAGE_UPLOADS"] = "/workspace/send-it-blog/static/images/blog-images/uploads"
app.config["UPLOAD_EXTENSIONS"] = ["JPG", "JPEG", "PNG", "GIF"]
app.config["MAX_IMAGE_FILESIZE"] = 2 * 1024 * 1024


def allowed_extenstions(filename):
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["UPLOAD_EXTENSIONS"]:
        return True
    else:
        return False


app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_posts")
def get_posts():
    show_all_posts = mongo.db.posts.find()
    return render_template("index.html", posts=show_all_posts)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    posts = list(mongo.db.posts.find({"$text": {"$search": query}}))
    return render_template("index.html", posts=posts)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "firstname": request.form.get("firstname").lower(),
            "lastname": request.form.get("lastname").lower(),
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put newly created user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful, Welcome!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in the database
        existing_user = mongo.db.users.find_one({
            "username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches users input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # password doesnt match
                flash("Incorrect Password and/or Username")
                return redirect(url_for("login"))
        else:
            # username does not exist
            flash("Incorrect Password and/or Username")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get session users first name from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You are now logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/create_post", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        todays_date = datetime.date.today()
        posts = {
            "post_title": request.form.get("post_title"),
            "post_date": todays_date,
            "post_preview": request.form.get("post_preview"),
            "post_content": request.form.get("post_content"),
            "created_by": session["user"]
        }
        mongo.db.posts.insert_one(posts)
        flash("Post Successfully Published")
        return redirect(url_for("get_posts"))
    return render_template("create_post.html")


@app.route("/edit_post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    if request.method == "POST":
        edited_on_date = datetime.date.today()
        edited_data = {
            "post_title": request.form.get("post_title"),
            "post_date": edited_on_date,
            "post_preview": request.form.get("post_preview"),
            "post_content": request.form.get("post_content"),
            "created_by": session["user"]
        }
        mongo.db.posts.update({"_id": ObjectId(post_id)}, edited_data)
        flash("Post Successfully Edited")
        return redirect(url_for("get_posts"))
    
    post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    return render_template("edit_post.html", post=post)


@app.route("/delete_post/<post_id>")
def delete_post(post_id):
    mongo.db.posts.remove({"_id": ObjectId(post_id)})
    flash("Post Successfully Deleted")
    return redirect(url_for("get_posts"))


@app.route("/post_full/<post_id>")
def post_full(post_id):
    post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    return render_template("post_full.html", post=post)


def allowed_image_filesize(filesize):
    return int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]
    """ if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False """


@app.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():

    if request.method == "POST":
        if request.files:
            if "filesize" in request.cookies:
                if not allowed_image_filesize(request.cookies.get("filesize")):
                    print("File exceeded maximum size")
                    flash("File exceeded maximum size")
                    return render_template("edit_profile.html")

                image = request.files["image"]

                # check if image has a name
                if image.filename == "":
                    flash("Image file must have a name")
                    return render_template("edit_profile.html")

                # check if image is allowed file type
                if allowed_extenstions(image.filename):
                    filename = secure_filename(image.filename)

                    image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

                    print("image saved")
                    flash("Upload Successfull!")

                    return redirect(url_for('profile', username=session['user']))

                else:
                    flash("Image format not accepted")

                    return render_template("edit_profile.html")

    return render_template("edit_profile.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
