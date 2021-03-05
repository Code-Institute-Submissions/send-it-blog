# Testing

### Table Of Contents
1. [Code Validation](#code-validation)
2. [Automated Testing](#automated-testing)
3. [Browser Compatibility](#browser-compatibility)
4. [Manual Testing](#manual-testing)
5. [User Story Testing](#user-story-testing)
6. [Peer Testing](#peer-testing)
7. [Bugs](#Bugs)

-----

Testing on this project was done proactively and thoroughly. Bugs and issues that have been found have been noted but mostly the site functions well. During early stages of development a continuous form of testing flask functions & views was used, simply by printing values and checking links and endpoints were correct. This constant testing meant that when the time came to do code validation, there were not many errors. Validation results are as follows:

-----

### Code Validation

#### W3C HTML Validator:
Markup passed through with errors to do with:
- lack of `<!DOCTYPE html>` declaration.
- lack of `lang="en"` declaration.
- lack of `<head>` element.
- Clashes in UI Kit classes & attributes
- Various other "Bad value", "Attribute" or "Element" errors due to clashes with Jinja template language.


#### Jigsaw CSS Validator
Code passed through without any errors.

styles.css
![screenshot of index page css validator](https://res.cloudinary.com/ivanprojects/image/upload/v1614921720/send-it-images/Screenshot_2021-03-05_at_06.20.40_q9uu9g.png)


#### PEP8 Validator
Code passed through without any errors.

app.py
![screenshot of PEP8 validator page](https://res.cloudinary.com/ivanprojects/image/upload/v1614920956/send-it-images/Screenshot_2021-03-05_at_06.08.56_dpjbov.png)


-----

### Automated Testing

#### LightHouse

Lighthouse scores were generally mixed, performance and accessibility results were high but best practice & SEO results were low. I using the home page result as an example here since it will be the most visited page. Some things mentioned were:
- Properly size images to improve load time.
- Serve static assets with an efficient cache policy as a long cache lifetime can speed up repeat visits on the page.
- Links to cross-origin destinations are unsafe, however this seems to be coming from UI Kit classes.
- Images displayed with incorrect aspect ratio & size. These are the small profile images on each blog post card. I should properly resize them to be smaller in the future to save on file size and display closer to natural aspect ratio.
- Browser errors were logged to the console, this is from deleted css & js files that have some remnant in the file directory or in the code.
- No meta tag, meta descriptions may be included in search results to concisely summarize page content, however at this station it is not completely necessary to have them so they can be added at a later date.

Desktop
![screenshot of index.html lighthouse score](https://res.cloudinary.com/ivanprojects/image/upload/v1614923371/send-it-images/Screenshot_2021-03-05_at_06.42.07_cunust.png)

On the mobile test, performance scores were really hurt by the lack of compression of the images (something that I did not make enough time for). Accessibility scores are still high while the SEO score increases. Best practice stays quite low with similar reasons as to the desktop site. But it is clear to see mobile users would be very much effected by the size of some images & so this would be a priority bug fix.

Mobile
![screenshot of index.html mobile lighthouse score](https://res.cloudinary.com/ivanprojects/image/upload/v1614923425/send-it-images/Screenshot_2021-03-05_at_06.49.13_smaobb.png)

-----

### Browser Compatibility

I went through a browser compatibility check using [BrowserStack](https://www.browserstack.com/live). I tested the compatibility on Chrome v87, Firefox v84, Safari, Edge v87. Details included in the table below.

|Criterea             |Galaxy S10+|Moto G4   |Galaxy S5 |Pixel 2   |Pixel 2 XL|iPhone SE |iPhone 6/7/8|iPhone 6/7/8 Plus|iPhone X  |iPad      |iPad Pro  |Surface Duo|Galaxy Fold|Laptop (+1024px)|Laptop (+1440px)|
|---------------------|-----------|----------|----------|----------|----------|----------|------------|-----------------|----------|----------|----------|-----------|-----------|----------------|----------------|
|Renders As Expected? |PASS       |PASS      |PASS      |PASS      |PASS      |PASS      |PASS        |PASS             |FAIL      |PASS      |PASS      |PASS       |PASS       |PASS            |PASS            |

Testing was also done on real life iphone 11 & 12 and while the experience was generally good, the iphone 12 (using safari), could not render the logo in the navbar as desired.
-----

|Criteria              |Chrome v87     |Firefox v84    |Safari v14.0.2  |Edge v87       |
|----------------------|:-------------:|:-------------:|:--------------:|:-------------:|
|Renders As Expected?  |PASS           |PASS           |PASS            |PASS           |

-----


### Manual Testing

I decided to test each page for general & specific functionality & responsiveness. Each test is answered yes or no, the no's will be investigated/explained. 

#### Register Page
Test 1:
- Can I register a user: Y

Test 2:
- Can I register a user with the same name as another username: N
FLASHED MESSAGE SAYING USERNAME ALREADY EXISTS

Test 3:
- Can I register a user with input values missing: N
A TOOLTIP SHOWS SAYING INPUT IS REQUIRED

Test 4:
- Can I register a user with less than 5 or no characters in the password field: N
A TOOLTIP SHOWS SAYING INPUT IS NOT ENOUGH

Test 5:
- Do all nav & footer links and the off-canvas menu work on this page: Y/N
SOCIAL LINKS IN OFF CANVAS NAV DO NOT OPEN IN NEW TAB

Test 6:
- Is the page responsive and all content visible: Y

#### About Page
Test 1:
- Do all nav & footer links and the off-canvas menu work on this page: Y

Test 2:
- Is the page responsive and all content visible: Y

#### Contact Page
Test 1:
- Do all nav & footer links and the off-canvas menu work on this page: Y/N
SOCIAL LINKS IN OFF CANVAS NAV DO NOT OPEN IN NEW TAB

Test 2:
- Is the page responsive and all content visible: Y

Test 3:
- Can I send message with less than 5 or no characters in any of the fields: N
A TOOLTIP SHOWS SAYING INPUT IS REQUIRED OR NOT ENOUGH

Test 4:
- If I send the form correctly, do I get a confirmation message: Y

#### Profile Page
Test 1:
- Do all nav & footer links and the off-canvas menu work on this page:Y/N
SOCIAL LINKS IN OFF CANVAS NAV DO NOT OPEN IN NEW TAB

Test 2:
- Is the page responsive and all content visible: Y

#### Create Page
Test 1:
- Do all nav & footer links and the off-canvas menu work on this page: Y/N
SOCIAL LINKS IN OFF CANVAS NAV DO NOT OPEN IN NEW TAB

Test 2:
- Is the page responsive and all content visible: Y

Test 3:
- Can I send message with less than 5 or no characters in any of the fields: N
A TOOLTIP SHOWS SAYING INPUT IS REQUIRED OR NOT ENOUGH

Test 4:
- Can I upload an unsupported image format: N
UPLOADER GRAYS OUT UNSUPPORTED FILES

Test 5:
- Once the upload is done, am I redirected to the homepage and can see my created post: Y

#### Uploader Page
Test 1:
- Do all nav & footer links and the off-canvas menu work on this page: Y/N
SOCIAL LINKS IN OFF CANVAS NAV DO NOT OPEN IN NEW TAB

Test 2:
- Is the page responsive and all content visible: Y

Test 3:
- Can I upload an unsupported image format: N
UPLOADER GRAYS OUT UNSUPPORTED FILES

Test 4:
- Once the upload is done, am I redirected to the profile page and can see my mew profile picture: N
PROBLEM WITH THIS FUNCTION, DID NOT HAVE TIME TO INVESTIGATE, PROBABLY TO DO WITH UPLOADER VIEW.

#### Your Posts Page
Test 1:
- Do all nav & footer links and the off-canvas menu work on this page: Y/N
SOCIAL LINKS IN OFF CANVAS NAV DO NOT OPEN IN NEW TAB

Test 2:
- Is the page responsive and all content visible: Y

Test 3:
- Am I taken to the edit post page when I click on the edit post button: Y

Test 4:
- Does the delete modal open on the press of the delete button and does the delete function work: Y

#### Login Page
Test 1:
- Do all nav & footer links and the off-canvas menu work on this page: Y/N
SOCIAL LINKS IN OFF CANVAS NAV DO NOT OPEN IN NEW TAB

Test 2:
- Is the page responsive and all content visible: Y

Test 3:
- Can I log in with less than 5 or no characters the password field: N
A TOOLTIP SHOWS SAYING INPUT IS REQUIRED OR NOT ENOUGH

Test 4:
- Can I log in with incorrect credentials: N
FLASHED MESSAGE SAYING USERNAME ALREADY EXISTS

Test 5:
- Am I redirected to the my profile page if I log in successfully: Y

#### Index Page
Test 1:
- Do all nav & footer links and the off-canvas menu work on this page: Y/N
SOCIAL LINKS IN OFF CANVAS NAV DO NOT OPEN IN NEW TAB

Test 2:
- Is the page responsive and all content visible: Y

Test 3:
- Can I see edit and delete buttons on posts for which I am the author: Y

Test 4:
- Am I taken to the edit post page when I click on the edit post button: Y

Test 5:
- Does the delete modal open on the press of the delete button and does the delete function work: Y

Test 6:
- If I click on a post image or title, am I taken to that specific post on the get_post template: Y

#### Get post Page
Test 1:
- Do all nav & footer links and the off-canvas menu work on this page: Y/N
SOCIAL LINKS IN OFF CANVAS NAV DO NOT OPEN IN NEW TAB

Test 2:
- Is the page responsive and all content visible: Y

Test 3:
- Am I being shown the relevant post for which I clicked on: Y

#### Create Page
Test 1:
- Do all nav & footer links and the off-canvas menu work on this page: Y/N
SOCIAL LINKS IN OFF CANVAS NAV DO NOT OPEN IN NEW TAB

Test 2:
- Is the page responsive and all content visible: Y

Test 3:
- Can I send message with less than 5 or no characters in any of the fields: N
A TOOLTIP SHOWS SAYING INPUT IS REQUIRED OR NOT ENOUGH

Test 4:
- Can I upload an unsupported image format: N
UPLOADER GRAYS OUT UNSUPPORTED FILES

Test 5:
- Once the upload is done, am I redirected to the homepage and can see my edited post: Y

Test 6:
- Is there content relevant to the post I am editing in the form fields: Y

#### Log Out Functionality
Test 1:
- If I click the log out link, am I logged out and returned to the log in page: Y

-----


### User Story Testing

#### Owner Stories


-   The site owner wants to showcase music & culture in an easy simple way.
The site owner feels the site is easy to use & they can easily catch up on the latest music & culture news.

-   The site owner wants site visitors to be able to post their choice of content on the site.
The site owner can make a profile and start posting content.

-   The site owner wants to be able to edit and delete posts.
The site owner can edit & delete their posts from the your posts or index pages.

-   The site owner wants users to be able to upload their own profile pictures.
The site owner can upload their profile picture.

#### User Stories

-   The site user wants to be able to see that all parts of the site function well.
The site user feels that 95% of the site functions as intended.

-   The site user wants to be able to read the latest on music & culture in a clear and concise format.
The site user finds it easy access the latest music & culture news & feels comfortable using the site.

-   The site user wants the overall user experience to be smooth and modern.
The site user is happy with the user experience, feels the site is simple and minimalistic.

-   The site user wants to be able to figure out the structure of the site quickly and easily.
The site user feels comfortable as a returning visitor since everything makes sense in the structure of the site, it is easy to get used to.

-   The site user wants to be able to search for words to find posts.
The site user can use the search functionality to search for words.

-   The site user wants to be able to view the site on their mobile devices comfortably.
The site user can see that the site is responsive, looks good and functions well on their phone.

-   The site user wants to be able to easily post content.
The site user knows they just need to register an account then posting content is very easy.

-   The site user wants to be able to images to indicate who posted which content.
The site user recognizes friends who have posted on the site from the profile pic thumbnail on each blog post card.

-   The site user wants to be able to learn more about the main collective in charge of the posts.
The site user feels content knowing that the about page is full of information on the collective as a group and as individuals.

-   The site user wants to easily be able to contact the main collective in charge of the posts
The site user is pleased that they can very easily send a message to the collective through the contact form on the contact page.

-----

### Bugs & Issues

During development & even now, there were and are still some issues that i could not or have not fix. I will list them below:

1. Using cloudinary uploader: STATUS: solved.
I had major issues figuring out how to get a url response when uploading to cloudinary. The issue was I had an asynchronous setting turned on which was causing the response I got to not include the url response. Once this setting was turned off, everything worked seamlessly. This I had to be told from cloudinary developers themselves since there were not much functioning solutions online or on slack at the time.

2. UI Kit issues: STATUS: ongoing.
Using UI Kit seemed like an interesting learning experience at the project inception. The process of using it however has been anything but clean sailing because since it is a class based framework, with a lot of utilities and components, you really have to be all in with it which I learned the hard way. There also seem to occasionally be some issues with white space since I am not so comfortable with everything on it yet, it seems some class or components could be causing some overflow issues.

3. Date Posted & Edited issues: STATUS: ongoing.
This is an issue that stems from the want for me to be able to see a posts original post date and the date they last edited it if any. I believe this issue is caused by the edit view needing to be a different HTTP method, perhaps PUSH or PATCH instead if POST. I could not figure out the way to implement this properly though, hence the issue is one that will have to be solved another day.

4. Uploader view issue: STATUS: ongoing.
This issue is specifically with the uploader for the profile picture, where in theory you should be able to update your profile picture as you will. However it seems that even though the file is being uploaded to cloudinary, the correct URL is not being sent to MongoDB therefore the correct image is not displayed and the profile image (on reload) stays the same. I think the issue is coming from the fact that I couldn't figure out which or how to use a MongoDB collection method to update one field in a document without affecting the others, which is a similar issue I have with the "date posted" problem above. This is another issue that will be tackled down in with time.

5. No search results issue: STATUS: ongoing.
I remembered late that if there was a search that returned no results, I should have a header stating "No Results Found", however when I tried to set up the if statement, I would get an error that the cursor has no length. I think it is down to the way I have my views set up and my methods of querying the database, I must have a cursor object where there shouldn't be and since cursor objects do not have a length attribute, I get the error. This will be solved in due time.

### Final Thoughts
In all this project has been one of the most challenging and time consuming but I have definitely learnt the most. Using UI Kit has really forced me to think wisely about using frameworks, whether it is wiser to just write my own CSS and use SASS. I had a lot of features I wanted to implement and I will continue this project after hand in since it really feels like i am not done with it. My mindset when it comes to prioritizing and working smart has improved from this experience.
