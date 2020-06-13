# Recipe Shack

For my Data-centric milestone project I decided to take one of the modeled example ideas and creat a recipe sharing website, 
my main goal was to have a platform where people can come and share their favourite recipes with one another, rate eachothers recipes and comment on them.
In some eyes like a recipe "facebook" of sorts.

I wanted the design to be simple and easily navigated, looking sleek and crisp. I'm using bootstrap as a template due to it having a 
proffesional finish and it saves time while im tackling the newly learnt python arguements.

Here is a link to the Deployed Site: [Recipe Shack](http://recipe-shack.herokuapp.com/home)

 
## UX

I want this website to be accesible to anyone of an age that would understand the basic funtionality of the website, and for people interested in food.
so putting it into the perspective of a user: "I am a food lover, who loves to share food recipes, so i can share and enjoy learning of my own and others
food". Therefor my interface need to have a function to be able to add recipes, edit them, and remove them if the user wishes. For this functionality
to be feasible I will need to use a JSON based database platform, which is why im using MongoDB.

Here is a link to an early wireframe of my [App.py layout for pages and DB Schema](https://imgur.com/gallery/WaHCx9c)

I also had sketched out a few idea of what I wanted my pages to look like, which I will list below:

[Homepage:](link)

The early concept of the homepage had a seperate link on the nav bar for 'editing recipes' but after a meeting with my mentor we decided
it doesnt need to be that crowded and a simple button on the individual recipe should suffice and be more efficient to code. I also thought about
having a recently added section using something like a timestamp or value to arrange them to update automaticly, but i ran out of time before being
able to implement this, so I settled for a clean title page for the home page.

[Catergories Page:](link)

My catergories page turned out basically as expected on the site, though i did make some changes during development, instead of the entirel
card being clickable as it is now, they used to all have buttons on them, but after dicussing with my mentor, he suggested to have the card 
itself as the link as it will look sharper.

[Individual Category Page:](link)

Much like the catergory page, the initial design is pretty much the final outcome visually, I had originally intended the backend code for 
this to be more stream line and not include as many templates, but by the time i realised this point and spoke to my mentor about it I had 
run out of realistic time to implement it with full testing, so it has been left as 3 seperate templates. Future ideas to implement would be 
the addition to create new categories.

[Recipe page](link)

The recipe page came out the same as the initial sketch, though with the edition of the 'edit' button and 'delete' function. 

[Add / Edit Recipe page](link)

Very similar to the sketched wireframe, though there isnt much detail on my original idea in comparison. during development I initially used 
normal text inputs for the boxes, but they're a hassle to keep scrolling to look what you've typed and the formatting meant that if you switched
browser tabs it would revvery to the start of each input box, so after a chat with my mentor we landed on the idea of using the 'textarea' attribute,
allowing certain boxes to expand and become easier for the user to use and read. I've also linked up the database's category collection to give the
option of what category it is.
 
### Existing Features

- View recipes: All recipes open up into an individual page, easy to read and record.

- Add a recipe: You can fill out the form online to add a recipe straight onto the site.

- Edit a recipe: Take an all ready existing recipe and update the information of it.

- Delete recipe: If there is a recipe you do not like or wnat on there anymore then with a click of a button it will be removed from the site
               and the database.

### Features Left to Implement

- Rate a feature: I wanted to implement a system on the site that would allow users to rate each recipes and have a top 10 or 5 section to group
                  them together, but due to my lack of knowledge and time constraints at this present moment, I did not feel I had enough time to 
                  have it fully funcitonal for submission.

- Comments:       I also wanted to implement a feature where users could comment on recipes, but after looking into it the scope for me currently was too
                  great and I didnt want to commit to something I felt I couldnt deliver on time.

- Time of Posts:  Another thing I originally wanted to implement but again had a bigger scope than I anticipated, have a time of posting on all
                  recipes and be able to filter that to show which recipes were recently added by users.

- Delete warning: I would have liked to add a modal or warning message to confirm that they want to delete the recipe to avoid users accidently clicking 
                  delete.

## Technologies Used

- [BootstrapCND](https://getbootstrap.com/)
    - The project uses Bootstrap for most of the framework, as this project focuses more on the data side, I felt for time saving reasons using
      Bootstrap would be an effective method of quickly building the html elements and not having to spend lots of time on the CSS. (proved to be
      a good idea as I did struggle with the backend aspect.)

- JavaScript
    - Built into the BootstrapCND

- HTML

- CSS 
    - I would like to note that while I did have a static CSS file in here, I used inline styles due to ease and also difficulty getting it to work 
      over the bootstrap Css, I know this isn't good practice but it worked to produce the small changes I needed.

- Python (Flask, Pymongo, DnsPython)
    - Using flask as a framework for the backend and using pymongo to link my python code and mongoDB together, and DnsPython for the JSON format reading.

- [MongoDB](https://www.mongodb.com/)

## Testing

Testing throughout this project has been frequent, constant refreshing and editing code to get it functional.

1. Add Recipe Form:
    1. Go to the "Add a Recipe" page
    2. Try to submit the empty form and verify that no recipe has been added to any category page.
    3. Try to submit the form with the information filled out and check which category you have added it to for its addition.

2. Edit Recipe Form:
    1. Click on the recipe you added in the previous test and click on the edit button at the bottom of the page.
    2. Change what ever information you like and submit.
    3. Re-check the recipe to see if the changes have been made.

3. Delete Function:
    1. Revist the recipe you have just edited, scroll back to the bottom and click on the delete button.
    2. From the homepage try to revisit the recipe where it was, if it has disappeared the function has worked and it has been 
       wiped from the database.

Using the inspect tool on the chrome browser I've looked at how the site looks on multiple different devices i.e: Tablets, smartphones ect...
and have adjusted the code to responsively adapt to the change in screen resolution.

One bug I have noticed is on initial loading of the pages the images flicker slightly on load, small lag, i believe this is due to the images
being sourced through links, but I need to still change this to try and prevent it.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

I have deployed my site using Heroku, I set up the linking of accounts between heroku and github to automaticly update to the current build.
I connected also through the console in gitpod loging directly into the heroku CLI. I used the command `$ git push heroku master` to initialise 
the first build.

I also edited the config variables in the settings on heroku, the ip was set to 0.0.0.0 and the port to 8080. I also loged my Mongo URI in there too.

You can `git clone` the repository to run it locally on your machine, the requirements.txt will have all the packages required to run. 
   - Just to note, if you run it through the repository cloning method, my env.py is not included as it contains log ins for my database,
     so as a template this method is fine and then to install your own mongodb account to it to use, otherwise for testing and using this
     method is not advised.
# Credits
### Content
- Some are custom, but most of the recipes I used to fill the site have come from the BBC's recipe website. [BBC Recipes](https://www.bbc.co.uk/food/recipes)

### Media
- The photo for the category cards have been taken from google searches which i will list below:
    - [breakfast photo](https://www.google.com/search?tbs=simg:CAQSsgIJXBo481A1haEapgILELCMpwgaYgpgCAMSKKMWoRbJCaAWrRamFrQFqRalFqwWzCmkIqgnpyeQK8spzynSN6UglycaMN0uaiAg2elZL7RmSDIJaOOeY62M0bU19N4AvEHVaw4EbyQpET4h1SSRGO4ctgLL6SAEDAsQjq7-CBoKCggIARIEWkMcVwwLEJ3twQkangEKIgoOZnVsbCBicmVha2Zhc3TapYj2AwwKCi9tLzAycWh3YzQKJAoRYnJlYWtmYXN0IHNhdXNhZ2XapYj2AwsKCS9tLzAxeGcwagoYCgZicnVuY2japYj2AwoKCC9tLzBkd19tChgKBXRvYXN02qWI9gMLCgkvbS8wMTd6MHYKHgoLcG9hY2hlZCBlZ2fapYj2AwsKCS9tLzBiMHk0MQw&sxsrf=ALeKk02ZqFC3RjWG4KXafQ24FArSen-Law:1592057315856&q=greasy+spoon&tbm=isch&sa=X&ved=2ahUKEwi08pfW-_7pAhVPXsAKHd-dCq0Qwg4oAHoECBAQKA&biw=1536&bih=731#imgrc=j6AiHMi6ZXIBdM)
    - [lunch photo](https://www.google.com/search?tbs=simg:CAQStQIJRlojb75mBIMaqQILELCMpwgaYgpgCAMSKOQLyhbMHvwf2AvLFtgWoha1HN8LyymkIqwimyCKIo4ikyLMKZk4zikaMNqtTxu-k7bNBris8jNmLzi7W93-1ELt_1E-RDMC-G8oPInR1fdJ-h_11dxXa3O2fcWSAEDAsQjq7-CBoKCggIARIEFwxiIAwLEJ3twQkaoQEKIgoPY2hpbmVzZSBub29kbGVz2qWI9gMLCgkvbS8wMmh6M3AKIAoNZnJpZWQgbm9vZGxlc9qliPYDCwoJL20vMDljbHgyCh8KC2JlZXQgZ3JlZW5z2qWI9gMMCgovbS8wNDQ2YnliCh0KCXN1cGVyZm9vZNqliPYDDAoKL20vMDRqZGh4eQoZCgVu4buZbdqliPYDDAoKL20vMHBiOHRmOAw&sxsrf=ALeKk03rH-js8UPuyM8pFIR0ZILXqKPRvg:1592057374980&q=vegan+restaurants+venice+italy&tbm=isch&sa=X&ved=2ahUKEwicy7Dy-_7pAhWoQEEAHRxbDq4Qwg4oAHoECAkQKA&biw=1536&bih=731)
    - [dinner photo](https://www.google.com/search?tbs=sbi:AMhZZiu9vgSVDbRqTSJX_1K5ECqdeNUsdJ74JY2iDWSA7Xo4GsLj56-1wNpinePE4nzxroru_1Xl3u_15D0nwuoztNGp3D0LssMrSVvNLOHzdjDXR6nNakfX6Mka8fHVbECAHgkMvAl-91slJfwnO-bHvGOGBH8PPFDtqP_1tTDKcalZz44XLR8QplEz6NFT838AoqaxLU4aDIJv5dPaRNmhXO1V7a4AQBwt9lkGqxkxj-Wq46fYzo7cObcpPGrglASofUrdvbkbLoxs6TOEKu9IdZ4U5ADbV4vol-KsSzG-2-_1uB7NzP9-ZFynnLMFXuuWNj2ZGrKOdWty8Hhc0oil78JIJxyYvLMX7kg)



# Thank you for reading and assessing my work!