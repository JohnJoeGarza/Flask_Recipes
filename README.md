# Flask Recipes
## About the project
Flask Recipes is an exploration personal project into using the Flask Web Framework to store cooking recipes on a website. It is designed to follow a blog type structure for entering cooking recipes. The recipes are stored on a simple SQLite database.

### The Welcome Page
![alt-text](https://github.com/JohnJoeGarza/Flask_Recipes/blob/master/design_elements/welcome_page.JPG)
The welcome page has a welcoming design and prompts for the user to log in so that the recipes may be viewed.

### Logging In
![alt-text](https://github.com/JohnJoeGarza/Flask_Recipes/blob/master/design_elements/login_page.JPG)

Once log in has been clicked, the user is taken to the login page. Currently only the admin account is available. If the username/password does not match the account, flask will handle this and provide a flash message for this situation shown below:

![alt-text](https://github.com/JohnJoeGarza/Flask_Recipes/blob/master/design_elements/login_page_error.JPG)


### The Show Recipes Page
![alt-text](https://github.com/JohnJoeGarza/Flask_Recipes/blob/master/design_elements/layout.JPG)


Once login credentials are verified, the user is taken to the main page where stored recipes are shown at the bottom.



The user has the ability to store new recipes that they like as well as a description of the recipe. This process and resulting page are shown below: 
![alt-text](https://github.com/JohnJoeGarza/Flask_Recipes/blob/master/design_elements/adding_recipe.JPG)
![alt-text](https://github.com/JohnJoeGarza/Flask_Recipes/blob/master/design_elements/recipe_added.JPG)


Progress as of 3/1/2017
