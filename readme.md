
# MarsaMaroc Resource Manager
# Introduction

This is a prototype website to manage resources for Marsa Maroc Company, it's build based on Python (3.5) using the Django framework with other minor libraries and sql database.

The result is a dynamic, smooth and responsive website that allows entering and altering data easily with couple of other features.

### Main features

* User registration and logging in
* Supports resetting password via email
* Clean, modern and flat UI
* Dashboard to manage all the data
* Ability to add/modify/remove/view resources and other data
* Manage users and user's permissions
* Customize the site theme
* Translation supported


# Getting Started
## Clone repository


First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/MarsaMaroc.git
    $ cd MarsaMaroc

## Setup virtual environnement
Create the virtual environnement by running:

    $ pip install pipenv
    $ pipenv shell

Activate the virtualenv for your project.
  
Install project dependencies:

    $ pipenv install
    

## Setup server

Then simply apply the migrations:

    $ python manage.py migrate
    $ python manage.py loaddata initial_data.json


Collect static files by:

    $ python manage.py collectstatic


You can modify `ResourceManage/settings.py` file or modify environnement variables by creating `.env` file for example on the root folder

Important variables are :

* `DEBUG`

* `EMAIL_HOST`

* `EMAIL_PORT`

* `EMAIL_USE_TLS`

* `EMAIL_HOST_USER`

* `EMAIL_HOST_PASSWORD`

* `DEFAULT_FROM_EMAIL`

You can now run the development server:

    $ python manage.py runserver

The website should be live on [localhost:8000](localhost:8000)

## Creating a superuser

To be able to access the admin site and add other users you have to create a super user with the command:

    $ python manage.py createsuperuser

Then proceed to enter a valid :

* Username
* Email
* Password

## Sample data

To load sample data as an example and to display what the app is capable of, just run the command:

    $ python manage.py loaddata manager_resource_sample_data.json

This will load 100 resource entry and a superuser with username: `admin` and password: `admin`
# Deployement

The website project is already configured well to be deployed on **Heroku**. You can just create a new heroku app for this project and deploy it.

You need to specify the environnement variables on heroku, already mentioned above, for the app to work with no errors