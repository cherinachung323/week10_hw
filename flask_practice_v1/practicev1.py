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


# Group Home Page
@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Group Home Page </title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>Welcome to our Homepage!</h1>
        <a href='/rana'>
        <img src="/static/Rana.png" alt="Rana" width="300" height="200">
        </a>
        <a>
        <img src="/static/Katy.png" alt="Katy" width="300" height="200">
        </a>
        <a href='/cherina'>
        <img src="/static/cherina.png" alt="Cherina" width="300" height="200">
        </a>
    </body>
    </html>
    """


# use <a> tags
# This route (@app.route('/')) defines the behavior of the homepage.
# It returns an HTML response containing a welcome message, information about me, and links to the "About Me" page
# (/about) and the "Projects" page (/projects).
@app.route('/cherina')
def cherina():
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
        <p>Check out my <a href="/about-cherina">About Me</a> page.</p>
        <p>Explore my <a href="/projects-cherina">Projects</a>.</p>
        <p>Back to Group Homepage <a href="/">Group Homepage</a>.</p>
    </body>
    </html>
    """


# About Me route
@app.route('/about-cherina')
def about_cherina():
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
        <p>Visit my <a href="/cherina">Homepage</a>.</p>
        <p>Explore my <a href="/projects-cherina">Projects</a>.</p>
    </body>
    </html>
    """


# Projects route
@app.route('/projects-cherina')
def projects_cherina():
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
         <p>Visit my <a href="/cherina">Homepage</a></p>
         <p>Learn more about me on <a href="/about-cherina">About Me</a></p>
         <p>Contact me <a href="/contact-cherina">here</a></p>
    </body>
    </html>
    """


# Contact route
@app.route('/contact-cherina')
def contact_cherina():
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
        <p>Visit my <a href="/cherina">Homepage</a></p>
        <p>Learn more about me on <a href="/about-cherina">About Me</a></p>
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
    <p>Go back to the <a href="/cherina">homepage</a>.</p>
    """


@app.route('/rana')
def rana():
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
        <p>Hello, I'm Rana. I am passionate about fashion particularly shoes!</p>
        <p>Here are a few things other things I enjoy:</p>
        <ul>
            <li>Buying shoes</li>
            <li>Writing code</li>
            <li>Painting & Drawing</li>
            <li>Anime</li>
        </ul>
        <p>Visit my <a href="/Shoes-page">Shoes Page</a>.</p>
        <p>Explore my <a href="/anime">Favourite Anime</a>.</p>
        <p>Back to Group Homepage <a href="/">Group Homepage</a>.</p>
    </body>
    </html>
    """


@app.route('/Shoes-page')
def shoes():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Shoes!</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>Shoe's</h1>
        <p>This is the Shoe wall of Shame!</p>
        <p>And yes there are  more loose shoes in that bag</p>
        <img src="/static/Shoes.png" alt="Shoes.png" width="300" height="200">
        <p>Explore my <a href="/anime">Favourite Anime</a>.</p>
        <p>Return to my Homepage <a href="/rana">Homepage</a>.</p>
    </body>
    </html>
    """


@app.route('/anime')
def anime():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Anime</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>My Favourite Anime</h1>
        <p>These are my top rated Anime series!</p>
         <a href='/demon-slayer'>
        <img src="/static/Demon Slayer.png" alt="Demon Slayer" width="300" height="200">
        </a>
        <a href='/death-note'>
        <img src="/static/Death Note.png" alt="Death Note" width="300" height="200">
        </a>
        <a href='/attack-on-titan'>
        <img src="/static/Attack on Titan.png" alt="Attack on Titan" width="300" height="200">
        </a>
        <p>Return to my Homepage <a href="/rana">Homepage</a>.</p>
    </body>
    </html>
    """


@app.route('/demon-slayer')
def demon_slayer():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Demon Slayer</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>Demon Slayer</h1>
        <p>This is Demon Slayer</p>
        <p>A family is attacked by demons and only two members survive - Tanjiro and his sister Nezuko, 
            who is turning into a demon slowly. Tanjiro sets out to become a demon slayer to avenge his family 
            and cure his sister</p>
        <a href='https://www.imdb.com/title/tt9335498/'>
        <img src="/static/Demon Slayer.png" alt="Demon Slayer" width="300" height="200">
        </a>
        <br>
        <span>Page 1</span>
        <a href='/death-note'>Next</a>
        <p>Return to Anime Page <a href="/anime">Anime</a>.</p>    
    </body>
    </html>
    """


@app.route('/death-note')
def death_note():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Death note</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>Death Note</h1>
        <p>This is Death note</p>
        <p>Light is an extremely brilliant but bored school student. Until the strange day where he accidentally 
        encounters the Death Note; a mysterious notebook with the power to kill anyone whose name is written 
        inside it.</p>
        <a href='https://www.imdb.com/title/tt0877057/?ref_=fn_al_tt_1'>
        <img src="/static/Death Note.png" alt="Death Note" width="300" height="200">
        </a>
        <br>
        <span>Page 2</span>
        <a href='/demon-slayer'>Previous</a>
        <a href='/attack-on-titan'>Next</a>
        <p>Return to Anime Page <a href="/anime">Anime</a>.</p>
        
    </body>
    </html>
    """


@app.route('/attack-on-titan')
def attack_on_titan():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Death note</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>Attack on Titan</h1>
        <p>This is Attack on Titan</p>
        <p>It is set in a world where humanity is forced to live in cities surrounded by three enormous walls that 
        protect them from gigantic man-eating humanoids referred to as Titans; the story follows Eren Yeager, 
        who vows to exterminate the Titans after they bring about the destruction of his hometown and the death 
        of his family and friends </p>
        <a href='https://www.imdb.com/title/tt2560140/?ref_=fn_al_tt_4'>
        <img src="/static/Attack on Titan.png" alt="Attack on Titan" width="300" height="200">
        </a>
        <br>
        <span>Page 3</span>
        <a href='/death-note'>Previous</a>
        <p>Return to Anime Page <a href="/anime">Anime</a>.</p>
    </body>
    </html>
    """


if __name__ == '__main__':
    app.run(debug=True)
