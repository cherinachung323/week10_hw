# Practice with Flask by using the notes
# Have something to demonstrate during your Tutor Session
#
# Practice with Git

# Pre-read next week's notes
# Create a few extra html routes and include <a> tags to other HTML route functions

from flask import Flask

# Importing Flask: The code starts by importing the Flask module, which is necessary to create a Flask application.
# Creating the Flask App: An instance of the Flask class is created with the name app.
app = Flask(__name__)


# Homepage route
# use <a> tags
# This route (@app.route('/')) defines the behavior of the homepage.
# It returns an HTML response containing a welcome message, information about me, and links to the "About Me" page
# (/about) and the "Projects" page (/projects).
@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>Welcome to My Homepage!</h1>
        <p>Hello, I'm Cherina. I'm now learning to code!</p>
        <p>Check out my <a href="/about">About Me</a> page.</p>
        <p>Explore my <a href="/projects">Projects</a>.</p>
    </body>
    </html>
    """


# About Me route
@app.route('/about')
def about():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About me</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>About me</h1>
        <p>I'm Cherina. I love coding and playing volleyball.</p>
        <p>Visit my <a href="/">Homepage</a>.</p>
        <p>Explore my <a href="/projects">Projects</a>.</p>
    </body>
    </html>
    """


# Projects route
@app.route('/projects')
def projects():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About me</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>Projects</h1>
        <p>Here are some of the projects I've worked on:</p>
        <ul>
            <li>Project 1</li>
            <li>Project 2</li>
            <li>Project 3</li>
         </ul>
         <p>Visit my <a href="/">Homepage</a></p>
         <p>Learn more about me on <a href="/about">About Me</a></p>
         <p>Contact me <a href="/contact">here</a></p>
    </body>
    </html>
    """


# Contact route
@app.route('/contact')
def contact():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About me</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>Contact Me</h1>
        <p>You can reach me via email: cherina.chung@gmail.com</p>
        <p>Visit my <a href="/">Homepage</a></p>
        <p>Learn more about me on <a href="/about">About Me</a></p>
    </body>
    </html>
    """


# Route for a dynamic page
# Dynamic Route (/user/<username>)
# This route (@app.route('/user/<username>')) defines a dynamic route for user profiles.
# It takes a username as a parameter and displays a simple profile page for that user,
# with a link back to the homepage (/).
@app.route('/user/<username>')
def user_profile(username):
    return f"""
    <h1>User Profile: {username}</h1>
    <p>This is the profile page for {username}.</p>
    <p>Go back to the <a href="/">homepage</a>.</p>
    """


if __name__ == '__main__':
    app.run(debug=True)
