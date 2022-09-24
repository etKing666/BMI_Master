# BMI MASTER
#### Video Demo: https://youtu.be/uwz3DHS1mM8

## Description
BMI Master is a web application developed using Flask framework.

### What is BMI Master?
BMI Master is an app developed to promote a healthier lifestyle by offering an easy-to-use BMI calculator.

BMI stands for "Body Mass Index". It is a value derived from person's height and weight and it is used to categorize people as:
- Underweight
- Normal weight
- Overweight
- Obese

### Basic functionality

BMI Master helps users to:
- Get basic information about the concept of BMI and its calculation
- Have their BMI value calculated
- Get recommendations according to their BMI category

## Development Methodology

The application was developed using Flask framework. The developer used the main navigation menu and styling options offered by Bootstrap. 

### Stylesheets

Apart from the Bootstrap CSS, a custom stylesheet was incorporated into the project for styling.

### Templates

A basic template (base.html) was developed and it was extended as needed. Apart from the base and index pages, the templates for:
- Getting user input
- Displaying the result of the calculation
- Returning an error in case the user is under 20 years old or the value entered is invalid
- Displaying detailed information about BMI

### Miscellaneous

Apart from the points above, it should be noted that:

- All information on the pages are taken from reputable public authorities (links can be found at the top of each page).
- Instead of hard coding the URLs, {{ url_for('pagename') }} format is used to generate URLs dynamically.

## Way ahead

The development plan for the application is as follows:
- Incorporating calculation option with imperial system.
- User management and connecting the app to a database. This way, the users will be able to register, log in and store their BMI values.
- Deployment of the app on Heroku.

## Developer Info

The BMI Master application is developed by Etkin Getir from Türkiye.

You may contact the developer by sending an emain to etkingetir@gmail.com

LinkedIn: http://www.etkingetir.com
GitHub: https://github.com/etKing666 


