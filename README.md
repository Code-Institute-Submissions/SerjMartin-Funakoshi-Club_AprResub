# Funakoshi club
## About
Funakoshi Club is a very friendly website for all people who practise Shotokan Karate or those who want to take an interest in it. This website has a few different functions, you can read a bit about the history of Shotokan Karate on the home page, you can find links to suggested books from different websites on the Books Library page. We also have a blog to share your thoughts, experiences and view other people's, ability to book your place at the seminars. to use the blog you have to create an account. Ability to book your place at the seminars.

## Table of Contents
  - [How to use](#how-to-use)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [Acknowledgement](#acknowledgement)
## How to use


## Features

### Existing Features
 ### Home
  The home page split into 2 parts from the header and footer
  - ### About
  This section describes what is about this website and how to use it.

  - ### History
  This section tells us a little bit of the history of this sport, by who and when was created.

s

## Technologies Used
 - For the account registration used Django-allauth library
 - For the feature images and CSS support used the Cloudinary library
 - For the comments used Crispy forms library
 - For the login/logout templates used default account templates from Allauth library

## Testing

 ### Validator Testing

## Deployment

  - ### Create the Heroku app
    On the Heroku, dashboard click on the "Create new app" button then give the app a name, choose a region and click on the "Create app" button.

  - ### Attach the PostgreSQL database
    On the Heroku, menu clicks on the "Resources" tab then in "Add-ons" search for "Postgres" to add Heroku Postgres to the project.

  - ### Prepare our environment and [settings.py](https://github.com/SerjMartin/Funakoshi-Club/blob/main/funakoshi/settings.py) files
    In the project's [settings.py](https://github.com/SerjMartin/Funakoshi-Club/blob/main/funakoshi/settings.py) add the app name in "INSTALET_APP".
    Create the [env.py](https://github.com/SerjMartin/Funakoshi-Club/blob/main/env_sample.py) file to store the URL from DATABASE, CLAUDINARY and SECRET_KEY then add them in the Heroku "Config Vars".

  - ### Get our static and media files stored on Cloudinary
    In the project's [settings.py](https://github.com/SerjMartin/Funakoshi-Club/blob/main/funakoshi/settings.py) by adding followings lines (STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    MEDIA_URL = '/media/'
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage') we telling Django to store my static and media files in Cloudinare.

 - ### Deployment to Heroku
    Add Heroku's app name followed by herokuapp.com to ALLOWED_HOST from [setings.py](https://github.com/SerjMartin/Funakoshi-Club/blob/main/funakoshi/settings.py).
    Add a file named "Procfile" for Heroku to know how to run my project.
    In the Heroku, dashboard click on the "Deploy" tab then click on GitHub to connect GitHub account after that searching for a repo to connect it to the Heroku.


### Cloning

## Acknowledgement

