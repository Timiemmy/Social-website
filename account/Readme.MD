# Purpose of the project

## To help improve my python and django programming skills

# What it is all about

## It is a website similar to pinterest where you can bookmark and save image you like from any website.

## It s fully authenticated. You can register an create account with email or social auth and all.

## You don't need to save image manually, you only need to deag the bookmark button to your browser bookmark bar and click on it when you're on any website and it will grab all images on that website. Then you click on the image you like and it will direct you back to create and save the image.

# How to run it.

## First install all dependencies by running "pip install -r requirements.txt"

## Register for the social account api if you want and include the keys

## Note that, If you run it without the development SSL certificate it won't grab any image, also it wont run without the redis server running.

# To run with development SSL certificate

## Type "python manage.py runserver_plus --cert-file cert.crt"

# To run the redis server on docker.

## Type "docker run -it --rm --name redis -p 6379:6379 redis" in your terminal or shell.

## You will need to create superuser to login to te admin panel.

# Feel free to fork and improve on it.

# Don't forget to follow my account and star the project.
