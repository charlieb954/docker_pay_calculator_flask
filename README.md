# Take Home Pay Calculator Web Application

A Flask web application containerised using Docker that calculates your take home pay for tax year 2020-21 based on salary and pension contributions as a percentage.

Other features include a Mongo database to record the number of times the application has been run as well as a Jenkins server for CICD.

Repository explained:

- app:
    - takehomepay: a python library to work out tax, pension and national insurance contributions
    - metrics: a python library to record how many times there has been a POST request from the application.
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
- In order to review metrics:
    
        sudo docker exec -it <mongo_container_name> bash
        mongo
        show dbs
        use flask
        db.metrics.find()
        exit

Example images:
![query](examples/salary_home_small.png)
![result](examples/salary_result_small.png)
