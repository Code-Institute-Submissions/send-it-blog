# importing required programs
import os
from datetime import datetime
import cloudinary
import cloudinary.uploader
import cloudinary.api
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# setting up cloudinary config variables
cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET')
)

# setting up mongo config variables
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
# index view
@app.route("/get_posts")
def get_posts():
    """getting all posts from db into a variable
    and rendering the template to show all posts"""
    show_all_posts = list(mongo.db.posts.find().sort("_id", -1))
    return render_template("index.html", posts=show_all_posts)


# search view
@app.route("/search", methods=["GET", "POST"])
def search():
    """ getting input value from search field into a variable
    and putting that through the index in the db then rendering
    the template """
    query = request.form.get("search")
    show_all_posts = mongo.db.posts.\
        find({"$text": {"$search": query}}).sort("_id", -1)
    return render_template("index.html", posts=show_all_posts)


# register view
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        """ check if username already exists in database, if
        yes than flash the message """
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        """ take the photo_url file from the template into
        a variable, use that variable with cloudinary
        function to upload """
        photo = request.files['photo_url']
        photo_upload = cloudinary.uploader.\
            upload(photo, upload_preset="n0wdtp5o")
        """ take form input as a dictionary and put into
        a variable, insert it into db """
        register = {
            "firstname": request.form.get("firstname").lower(),
            "lastname": request.form.get("lastname").lower(),
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "photo_url": photo_upload.get("secure_url")
        }
        mongo.db.users.insert_one(register)
        """ put newly created user into session cookie """
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful, Welcome!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# login view
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


# profile view
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """ get session users username from database,
    find in the db 3 newest posts from the user """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    show_user_posts = mongo.db.posts.\
        find({"created_by": username}).sort("_id", -1).limit(3)

    """ taking the users profile pic link from the db to be
    used in the template """
    profile_pic = mongo.db.users.find_one({"username": username})["photo_url"]

    if session["user"]:
        return render_template("profile.html", username=username,
                               posts=show_user_posts, profile_pic=profile_pic
                               )

    return redirect(url_for("login"))


# logout view
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You are now logged out")
    session.pop("user")
    return redirect(url_for("login"))


# create post view
@app.route("/create_post", methods=["GET", "POST"])
def create_post():
    if request.method == "POST":
        """ get session users username & profile
        pic url from database """
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        profile_pic = mongo.db.users.find_one(
            {"username": username})["photo_url"]
        show_all_posts = mongo.db.posts.find().sort("_id", -1)
        """ save the current time as a timestamp in
        a variable """
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        date_time = datetime.fromtimestamp(timestamp)
        """ take the photo_url file from the template into
        a variable, use that variable with cloudinary
        function to upload """
        photo = request.files['photo_url']
        photo_upload = cloudinary.uploader.upload(
            photo, upload_preset="n0wdtp5o")
        """ take form input as a dictionary and put into
        a variable, insert it into db """
        posts = {
            "post_title": request.form.get("post_title"),
            "post_date": date_time.strftime("%d/%m/%Y"),
            "edited_on": "",
            "post_preview": request.form.get("post_preview"),
            "post_content": request.form.get("post_content"),
            "created_by": session["user"],
            "photo_url": photo_upload.get("secure_url"),
            "profile_url": profile_pic
        }
        mongo.db.posts.insert_one(posts)
        flash("Post Successfully Published")
        return render_template("index.html", posts=show_all_posts)
    return render_template("create_post.html")

# edit post view


@app.route("/edit_post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    if request.method == "POST":
        show_all_posts = mongo.db.posts.find().sort("_id", -1)
        """ take save a formatted version of the date
        in a variable """
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y")
        """ insert edited data from form into db """
        edited_data = {
            "post_title": request.form.get("post_title"),
            "post_date": mongo.db.posts.post_date.find_one(),
            "edited_on": date_time,
            "post_preview": request.form.get("post_preview"),
            "post_content": request.form.get("post_content"),
            "created_by": session["user"],
        }
        mongo.db.posts.update({"_id": ObjectId(post_id)}, edited_data)
        flash("Post Successfully Edited")
        return render_template("index.html", posts=show_all_posts)

    post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    return render_template("edit_post.html", post=post)

# delete post view


@app.route("/delete_post/<post_id>")
def delete_post(post_id):
    rule = request.url_rule
    # find post by id and remove from db
    mongo.db.posts.remove({"_id": ObjectId(post_id)})
    flash("Post Successfully Deleted")

    if 'your_posts' in rule.rule:
        return redirect(url_for("your_posts"))

    return redirect(url_for("get_posts"))

# get post view


@app.route("/get_post/<post_id>")
def get_post(post_id):
    """ find specific post that has been clicked
    & go to template with full post """
    post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    return render_template("get_post.html", post=post)

# about page view


@app.route("/about")
def about():
    # go to about template
    return render_template("about.html")

# contact page view


@app.route("/contact")
def contact():
    # go to contact template
    return render_template("contact.html")

# your posts view


@app.route("/your_posts")
def your_posts():
    """ get session users username from database,
    find in the db all posts created the user """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    show_user_posts = mongo.db.posts.find(
        {"created_by": username}).sort("_id", -1)
    return render_template("your_posts.html", posts=show_user_posts)

# uploader view


@app.route("/uploader", methods=["GET", "POST"])
def uploader():
    if request.method == "POST":
        """ get session users username from database,
        use cloudinary function to upload local image
        return to users profile page """
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        photo = request.files['photo_url']

        photo_upload = cloudinary.uploader.upload(
            photo, upload_preset="n0wdtp5o")

        photo_url = photo_upload.get("secure_url")

        return render_template("profile.html",
                               username=username, photo_url=photo_url
                               )
    return render_template("upload_image.html")


# setting up server
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
