# Send It On Blog

![screenshot of the site on different devices](https://res.cloudinary.com/ivanprojects/image/upload/v1614918865/send-it-images/Screenshot_2021-03-05_at_05.34.00_iihu26.png)

# Project Description

The “Send It" blog is a site where a collective posts a curated selection of news on music and culture.

Below is a live link to the site which is hosted on Heroku.
[HERE](https://send-it-blog.herokuapp.com/)

## Table Of Contents

1. [Project Goals](#project-goals)
2. [Target Audience](#target-audience)
3. [UX Design](#ux-design)
    - [Strategy](#strategy)
    - [Owner Stories](#owner-stories)
    - [User Stories](#user-stories)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Wire frames](#wire-frames)
    - [Surface](#surface)
4. [Design Choices](#design-choices)
    - [Typography](#typography)
    - [Color](#color)
    - [Imagery](#imagery)
    - [Framework](#framework)
    - [Design Wrap-Up](#design-wrap-up)
5. [Existing Features](#existing-features)
6. [Features Left To Implement](#features-left-to-implement)
7. [Database](#database)
8. [Technologies Used](#technologies-used)
9. [Testing](#testing)
10. [Deployment](#deployment)
11. [Credits](#credits)

-----

## Project Goals

The aims of this web app are as follows:
-   Showcase skills with Python & MongoDB.
-   Add a more potential client relevant project to my portfolio.
-   Give client collective a space to share content.
-   Give users unique content content to read about.

-----

## Target Audience

-   Client collective interested in sharing relevant content.
-   Other potential freelance clients.
-   People interested in music & culture.
-   Peers interested in networking

-----

## UX Design

### Strategy

This site was created for a client who is a lover of music and culture. The client wanted to have a space where they and some chosen associates could write and enjoy content about the music and culture that they love. The client thought there was a space for quality, hand-picked content away from algorithms and computed playlists. Hence the idea of a music blog came to be. The focus of the site is on having a functional space where the client collective and other users can reliably and consistently create new blog posts, edit said blog posts, read other users blog posts and delete their own posts. Based on this and the target audience, the following owner and user stories were compiled.

### Owner Stories


-   The site owner wants to showcase music & culture in an easy simple way.
-   The site owner wants site visitors to be able to post their choice of content on the site.
-   The site owner wants to be able to edit and delete posts.
-   The site owner wants users to be able to upload their own profile pictures.

### User Stories

-   The site user wants to be able to see that all parts of the site function well.
-   The site user wants to be able to read the latest on music & culture in a clear and concise format.
-   The site user wants the overall user experience to be smooth and modern.
-   The site user wants to be able to figure out the structure of the site quickly and easily.
-   The site user wants to be able to search for words to find posts.
-   The site user wants to be able to view the site on their mobile devices comfortably.
-   The site user wants to be able to easily post content.
-   The site user wants to be able to images to indicate who posted which content.
-   The site user wants to be able to learn more about the main collective in charge of the posts.
-   The site user wants to easily be able to contact the main collective in charge of the posts

### Scope

Based on the user stories and project aims, the following features were considered & graded on difficulty and importance in order to decide which ones would be included in the app (5 being high & 1 being low):

![screenshot of feature selection table](https://res.cloudinary.com/ivanprojects/image/upload/v1614899536/send-it-images/Screenshot_2021-03-05_at_00.11.45_gsoapx.png)

The selected features include:

-   Ability to make an account to post content.
-   Ability to create new posts & upload image for post.
-   All users posts available on home page.
-   Small profile picture on each posted showing which user created it.
-   Can edit or delete posts from home page (must be logged in as post creator).
-   An about page with information on collective and each member.
-   A contact page with a form for emailing collective.
-   A profile page showing users most recent posts.
-   Ability to update user profile picture.
-   A page where all logged in user's posts are collected.
-   Search functionality


The project was then split into sprints to ensure an even workload spread over time.
-   Sprint 1 – Development environment and DB set up & Wire frames.
-   Sprint 2 – Python & Flask with HTML templates.
-   Sprint 3 – HTML & CSS fill in.
-   Sprint 4 - Testing & Debugging.

### Structure

I researched different blogs online & from experience, I had an idea of how I wanted the general structure of the site to look like.
-   Interaction design – The site should have a consistent flow of information, with the nav being at the top/off-canvas and footer at the bottom & main page specific content in the middle of each page. This flow if information is carried out through each page so the user will get used to important content being in one place.
-   Information Design – The content is structured so that content is always easily accessible and the user should not have to scroll or zoom unnecessarily.

### Skeleton

Wire frames were created to ensure that initial design and structure ideas were actually functional & in keeping with UI & UX design principles.

### Wire frames

#### HOME PAGE

- [HERE](https://res.cloudinary.com/ivanprojects/image/upload/v1614900718/send-it-images/Screenshot_2021-03-05_at_00.30.45_ecuv28.png)

This page keeps a very simple layout of a hero article followed by a grid of blog posts. Easy to understand and everything is accessible for the user. The header and footer section is kept the same throughout the site

#### ABOUT PAGE

- [HERE](https://res.cloudinary.com/ivanprojects/image/upload/v1614902245/send-it-images/Screenshot_2021-03-05_at_00.33.51_p7ivvm.png)

This page contains a relevant main image of the followed by relevant text about the team. This information flow of image and text is used throughout the site and continues on this page with each team member having their image shown plus a small description of themselves.

#### CONTACT PAGE

- [HERE](https://res.cloudinary.com/ivanprojects/image/upload/v1614902312/send-it-images/Screenshot_2021-03-05_at_00.34.05_bb36wk.png)

#### LOGIN PAGE

- [HERE](https://res.cloudinary.com/ivanprojects/image/upload/v1614902408/send-it-images/Screenshot_2021-03-05_at_00.38.15_nidro5.png)

This page along with the sign up page has not much information so it was important to keep things simple and try to have the form in the middle of the viewport.

#### SIGN UP PAGE

- [HERE](https://res.cloudinary.com/ivanprojects/image/upload/v1614902313/send-it-images/Screenshot_2021-03-05_at_00.39.30_mzizp8.png)

#### PROFILE PAGE

- [HERE](https://res.cloudinary.com/ivanprojects/image/upload/v1614902313/send-it-images/Screenshot_2021-03-05_at_00.49.47_rpcijr.png)

This page is roughly split in two down the middle with the left side being the user create and update picture side and the right being the users post previews. I wanted to separate the call to actions so there aren't too many buttons calling for attention.

#### CREATE/EDIT POST PAGE

- [CREATE](https://res.cloudinary.com/ivanprojects/image/upload/v1614902313/send-it-images/Screenshot_2021-03-05_at_00.53.16_txzrii.png)
- [EDIT](https://res.cloudinary.com/ivanprojects/image/upload/v1614902313/send-it-images/Screenshot_2021-03-05_at_00.53.05_jdovak.png)

These pages are virtually identical with the main form content being in the middle of the page.

#### YOUR POSTS PAGE

- [HERE](https://res.cloudinary.com/ivanprojects/image/upload/v1614902313/send-it-images/Screenshot_2021-03-05_at_00.52.52_q94qsf.png)

This page is laid out similarly to the index page jus without the hero section and with all posts being created by the user. The similarity will allow for easy of use..

### Surface

The final look of the web app as a whole was decided at this point. Colours, typography, animations and other design elements were considered with all decisions based on the requirement that they reinforce the meaning or value of the content.

At this point, I decided to confirm the final look of the site. This meant confirming the colour palette, Imagery choices, typography and other design elements. All decisions were made with the intention of enforcing more value to the structure and skeleton of the site.

## Design Choices

### Typography

There are two fonts being used for this site. Both are quite modern but they differ in styling, with the idea that one be used for headers & titles and the other be used for most other use cases. The fonts compliment each other quite well.

![screenshot of philosopher font](https://res.cloudinary.com/ivanprojects/image/upload/v1614904039/send-it-images/Screenshot_2021-03-05_at_01.26.47_mjrtpf.png)

![screenshot of roboto slab](https://res.cloudinary.com/ivanprojects/image/upload/v1614904040/send-it-images/Screenshot_2021-03-05_at_01.27.02_vb5efk.png)

![screenshot of font pairing](https://res.cloudinary.com/ivanprojects/image/upload/v1614903514/send-it-images/Screenshot_2021-03-05_at_01.18.18_unldsf.png)

### Color

I wanted the colors to be quite simple and understated but still provide enough contrast, vibrancy and really give a contemporary look. I chose black and white as accent, then chose a kind of off white and pastel/off black to be used as the main colors on the site. The secondary accent color was the lime green which would be used to really catch attention off the user.

![screenshot of color palette](https://res.cloudinary.com/ivanprojects/image/upload/v1614911314/send-it-images/dto625em2gftggplvagl.png)

### Imagery

The imagery of the site very much relates to the content and the users. Each post contains an image relevant to what that post is about. The user can also upload a profile image which will be shown on their profile and also on the blog post content cards on the home and profile pages.

### Framework

I decided to use the UI Kit framework to develop the front end of the site. This framework is class-based and seemed to be quite encapsulating in terms of having most components needed for what I wanted the site to do. The thing that convinced me to try this over Bootstrap or Bulma was that it had a very minimalistic but still timeless look to it which i thought really resonated with what I wanted to do with the site with regards to the design.

I go into the issues I had with it within the testing document.

### Design Wrap-Up

At this point I was happy with the ideas for the design but due to the nature of the project, I proceeded with caution and decided to work with the back-end to make sure the functionality was working before really adding in the necessary HTML & CSS to get the site looking the wau i wanted it to. Up until that point, it was a "lite" version which acted as a testing ground for the design and functionality.

-----

## Existing Features

### Create an account

This is one of the main features of the site, to be able to register an account. This would be needed to create, edit and delete posts so it was one of the top priority features.

### Create a post

Another one of the top priority features, creating a post that will end up on the home page for other users and site visitors to read.

### Uploading a picture when creating post

This feature is married to the create a post feature but was a bit more difficult to implement. After attempting to save the image uploads to the app file path, I decided it would be easier to use a cloud option, "Cloudinary". It took some time to figure out how to implement it well enough with python & flask but now it works great.

### All posts available on home page

This is another core feature of the site, having all the posts that have been created available to access on the home page.

### Specific blog post creator image on blog post card

This was a not so easy but important feature to implement. Within each blog post card on the home or user profile page, there will be a small thumbnail image at the bottom of the card which will be the blog post creators profile image. It gives an easy method of identification for who wrote what post.

### Can edit or delete posts from home page

This feature allows a user who is logged in and has created posts, to see buttons to edit and delete on those specific posts that they have created. Its a simple easy, user friendly way of avoiding going to the all user posts section if a user just wanted to quickly edit something. The delete button also opens a modal to confirm deletion to prevent accidental post removal.

### About page

The about page was very easy to implement and does a good job of informing readers about the collective as a group and as individuals.

### Contact page

This was another simple to implement but quite important page when it comes to providing value for the collective because if the contact page is easy to access and to use, site visitors are more likely to want to use it.

### Profile page

The profile page is another core feature of the site, each user has one and will find links there to create new posts, update their profile picture and see all posts they have created.

### Update profile picture

This was not a core feature but an easy to implement and a good to have one, initially there were issues due to problems with the cloudinary SDK but those were soon solved and now it works great.

### Search functionality

This was a great to have feature and not so difficult to implement either. Searching for specific words within the title or main post content will really make it easy for users and visitors to find the content they want.


-----

## Features Left To Implement

### Use a rich text editor for post creation.
This would have been great to have as at the moment the posts do not have any formatting so they are hard to read however it was quite hard to implement this feature in the time I had, but it will be something I will include in a future update for sure.

### Admin super user permissions to edit and delete posts from all users.
This feature was another good to have but was simply not high enough in priority. It would allow an admin account to edit and delete all posts, and also update the hero post.

### Ability to see if/when a post has been edited.
This was a feature I tried to implement but complications and time issues meant I had to leave it for another time. It would allow site visitors to see the date when a user first posted a blog post and also the date they last edited it if any.

### Comment on posts & edit comments.
This feature was in my wishlist when initially speaking to the collective about the project as it would really enhance the "conversation" feeling of the site but time constraints and high difficulty for implementation meant I had to leave it for the time being.

### Like posts & be able to access liked posts in profile.
Another feature on the wishlist, this would not have been as hard to implement as comments and I had an idea of the logic for how it would work but as is becoming the pattern here, time did not allow for me to explore the possibility of adding this feature.

### Related blog post links on blog post page.
I liked the idea of this feature but it was not of high importance since it is still early days for the project. It would make more sense to implement it when there are potentially more users.

### Custom 404 & 500 error page.
This feature I really wanted to have but again did not have time to implement. It would really help with making the site more professional and understandable.

### Defensive programming.
There is definite room for improvement when it comes to this feature, more secure log ins, error handling & fallbacks & some way to handle form resubmission. This is something that will definitely be implemented in the future.

### Display no results for search.
At the moment if you search for a word that brings no results, the section for posts is blank. Ideally there would be a header displaying no results found but when I tried to implement this, I got a cursor error that indicated there was an issue further down the rabbit hole which I did not have time to investigate. Again, something that will be included in a future version of the site.

-----

## Database

### Structure

```
{
  "_id":                   <ObjectId>,
  "post_title":            <string>,
  "post_date":             <string>,
  "edited_on":             <string>,
  "post_preview":          <string>,
  "post_content":          <string>,
  "created_by":            <string>,
  "photo_url":             <string>,
  "profile_url":           <string>
}
```

```
{
  "_id":                   <ObjectId>,
  "firstname":             <string>,
  "lastname":              <string>,
  "username":              <string>,
  "email":                 <string>,
  "password":              <string>,
  "photo_url":             <string>
}
```

For this project I used MongoDB Atlas as the database choice since it is document oriented and serves the purpose of this site well. I had two collections within the database:

#### Users
This collection contains everything needed to identify a user. Their username and a link to their profile picture. The username is the main method of user authentication on the site.

![screenshot of users mongoDB collection](https://res.cloudinary.com/ivanprojects/image/upload/v1614908539/send-it-images/Screenshot_2021-03-05_at_02.33.25_myeedt.png)

#### Posts
This collection contains everything that about a post, queried in most of the Flask views and used on most pages of the site. This collection goes hand in hand with the users collection to provide all the data for the site.

![screenshot of posts mongoDB collection](https://res.cloudinary.com/ivanprojects/image/upload/v1614908539/send-it-images/Screenshot_2021-03-05_at_02.33.04_civq97.png)



-----

## Technologies Used

- UI Kit – Front-end Framework
- Google Fonts – Font choice.
- tobiasahlin.com – Loading animation code.
- MongoDB Atlas - Cloud Database.
- GitHub Pages – Deployment.
- Tinypng.com - Image compression.
- Cloudinary - Cloud image hosting.
- Python - Main Back-end language alongside:
```click==7.1.2
cloudinary==1.24.0
dnspython==2.1.0
Flask==1.1.2
Flask-PyMongo==2.3.0
itsdangerous==1.1.0
pymongo==3.11.2
Werkzeug==1.0.1
```
- Git - Version control
- Heroku - Deployment
- Gitpod - IDE of choice for this project.
- email.js - Sending emails on contact form

-----

## Testing

Testing documentation can be found [HERE](testing.md)

-----

## Deployment

### My Set Up
My IDE of choice for this project was GitPod. I used the [Code Institute template](https://github.com/louparker/gitpod-full-template), by clicking on the green "use this template" link.

After being directed to the create new repository from template page, I typed in the project name and clicked the create repository from template button. I then clicked on the GitPod button which was on the newly created repository page I was directed to. This created a GitpPd workspace based on the repository.

### Run Project Locally

If you want to get this project up and running locally, you can follow these steps.
#### Requirements:
- Python 3
- Git
- An IDE
- A MongoDB Atlas Account

#### Step One, clone repository into local environment:

1. Click this link to open the main repository page: [HERE](https://github.com/louparker/send-it-blog).
2. click the code button
3. copy the link you are given to your clipboard
4. On your IDE of choice, open terminal and navigate to whichever directory you want the repository cloned to. Once in the desired directory, type `git clone`, then paste the URL copied from the Github repository. The command should look something like this:

`git clone https://github.com/louparker/send-it-blog.git`

5. press enter & you should have a local cloned version of the repository.



#### Step 2, Install requirements:
1. While you are still in the terminal, type `pip3 install -r requirements.txt`, this will install all the required softwares to run the project.
2. You now need to set up the database with environment variables. Create a file titled `env.py` and make sure it is placed in the of this file structure, on the same level as the `app.py` file. Open the file and type the following lines:


```import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "")
 os.environ.setdefault("MONGO_URI", "")
os.environ.setdefault("MONGO_DBNAME", "")
```

The `SECRET_KEY` is a value key of your own choice but it is recommended to be as secure as possible to password generators can be used. The `MONGO_URI` is to be taken from your mongo account. To find it, click on the overview button, then connect, then connect your application, its important to select the relevant python version for you. You can always check which version you are running within your IDE. The `MONGO_DBNAME` is whatever name you have given your database.

3. Once the database is set up, you are now ready to run the app. in the terminal, type `python3 app.py]` (depending on python version), this will run the python file and depending on your IDE should open a port and give you a link to access it through either an in-window preview or your browser. If that does not happen you can type `http://127.0.0.1:5000` in a browser window.

#### Heroku deployment:

1. Go to heroku.com & sign in or create a user if you haven't got one already.
2. Press the new button & click create a new app.
3. Choose your app name and region (closest to where you live).
4. At this stage you will want to set up the heroku app with the github repository. Click on the deploy tab and choose connect to github.
5. From the search input that opens, search for your repository by name and click the search button.
6. Once the desired repo has been found, press the connect button.
7. You will then need to set the environment variables since the env.py file is not pushed to github. To do this, open the settings menu and click on the reveal config vars button.
8. If you still have your IDE open, you can just copy the variables from the env.py file one by one. They would be:
```key: IP, value: 0.0.0.0
key: PORT, value: 5000
key: MONGO_DBNAME, value: ""
key: MONGO_URI, value: ""
key: SECRET_KEY, value: ""
```

Make sure the values are exactly the same as the ones you have in the `env.py` file.
9. At this stage you are ready to enable automatic deployment. You will want to push any changes you have made to github for convenience sake before you do this.
10. Click on the deploy tab.
11. Go down to the automatic deploy section & select the branch you intend to deploy.
12. click enable automatic deploys. This will mean github is talking to heroku and whatever you push to github will be in you deployed heroku app.
13. If there were any errors with the deployment, double check you have your Procfile and requirements file, if the requirements file is not there, you can type in your terminal `pip3 freeze > requirements.txt`. This will also make sure you have the most recent requirements pushed to GitHub & Heroku. If the Procfile is missing, you can type `echo web: python3 app.py > Procfile` (with a capital P).

### Forking

This is how you can "fork" the project without affecting the main branch. Which means you can change & edit it as a repository on your own GitHub profile.

1. Log in to GitHub.
2. Click on the following link to be taken to this repository's main page: [HERE](https://github.com/louparker/send-it-blog).
3. To the right of the repository name, you will see a "fork" button, click it.
4. You will now have a copy of this repository on your own GitHub account.
5. When you are done editing to your hearts content, you can click the "new pull request" button which allows the repository owner (me!) to include your work in the original project.

-----

## Credits

### Content
All design, content and code (unless specified below) were created by myself.

Specified code usage includes:
- [MongoDB Documentation](https://docs.mongodb.com/manual/reference/)
- [Python3 Documentation](https://docs.python.org/3/contents.html)
- [UI Kit Components & Documentation](https://getuikit.com/docs/introduction)
- [EmailJS Documentation](https://www.emailjs.com/docs/)
- [Google Fonts CSS import code](https://fonts.googleapis.com/css2?family=Philosopher:ital,wght@0,400;0,700;1,400;1,700&family=Roboto+Slab:wght@100;200;300;400;500;600;700;800;900&display=swap)
- Code Institute Course Content

The following sites were used for beautifying, optimizing images and adding correct vendor prefixes to my code:
- [Autoprefixer CSS](https://autoprefixer.github.io/)
- [Code Beautify](https://codebeautify.org/)
- [TinyPNG](https://tinypng.com/)

Blog content & Images from these links:

- https://pitchfork.com/news/dave-chappelle-tests-positive-for-covid-19-cancels-texas-shows/
- https://pitchfork.com/news/king-krule-covers-john-lennons-imagine-listen/
- https://pitchfork.com/news/jazmine-sullivan-and-eric-church-to-sing-national-anthem-at-super-bowl-2021/
- https://www.okayplayer.com/music/sza-new-album-interview.html
- https://www.okayplayer.com/music/snoop-dogg-eminem-beef.html
- https://www.okayplayer.com/music/jazmine-sullivan-heaux-tales-ep.html
- https://www.okayplayer.com/music/best-verses-in-34-35-remix-ariana-grande-megan-thee-stallion-doja-cat.html
- https://www.okayplayer.com/music/listen-dangelo-feverish-fantazmagoria-radio-show-stream.html
- https://www.okayplayer.com/music/j-dilla-welcome-to-detroit-think-twice.html
- https://www.okayplayer.com/music/joe-biden-inauguration-playlist.html
- https://www.okayplayer.com/music/a-rare-instrumental-marvin-gaye-album-has-surfaced.html
- https://pitchfork.com/news/watch-dangelos-verzuz-battle-live-at-the-apollo-theater/

All other images from Unsplash:
- [Clay Banks](https://unsplash.com/photos/LjqARJaJotc?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)
- [Nikolai Chernichenko](https://res.cloudinary.com/ivanprojects/image/upload/v1614918078/send-it-images/hello_zsb4pf.jpg)
- [Atikh Bana](https://unsplash.com/photos/2c0midsQKe0?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)
- [Brooke Cagle](https://res.cloudinary.com/ivanprojects/image/upload/v1614918165/send-it-images/member4_a6pwyj.jpg)
- [Anh Nguyen](https://unsplash.com/photos/z6PZ7ZH9MMQ?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)
- [Eye for Ebony](https://res.cloudinary.com/ivanprojects/image/upload/v1614820188/send-it-images/laura.jpg)
- [Julian Myles](https://unsplash.com/photos/JRPu9rnNgH8?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)
- [Clay Banks](https://unsplash.com/photos/LjqARJaJotc?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)
- [Chase Fade](https://unsplash.com/photos/XOLIrILp-vI?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink)


### Acknowledgements

- Stack Overflow as always was a massive help.
- Special thanks to my mentor Maranatha for regular words of wisdom and helping guide me to the right conclusions.
