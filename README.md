# Take Home Pay Calculator Web Application

A Flask web application containerised using Docker that calculates your take home pay for tax year 2020-21 based on salary and pension contributions as a percentage.

- app:
    - takehomepay: a python library to work out tax, pension and national insurance contributions
    - static: styling for the web application
    - templates: html webpages for the flask application
    - app.py: Flask application to run the application
- jenkins:
    - a jenkins project to explore using and automation server
- create_image_run_container: bash script to create and run the container
- quit_remove_containers: bash script to stop and remove the container
- vm_setup: bash script to install docker and prepare a VM to use this repository.

Instructions:
- Create Ubuntu VM using VMware
- Copy vm_setup.sh file to VM and run (bash vm_setup.sh)
- Clone repository (git clone url)
- Run the shell script to build and run the image (bash create_image_run_container.sh)