## Introduction 
This setup is provided for Linux OS (Debian flavor). python3 has to be
accessable via terminal.

## Preparing environment in Ubuntu/Debian

    $ git clone http://github.com/niekas/car_number_plates
    $ cd car_number_plates
    $ sudo apt-get install python3-pip nodejs
    $ python3 -m venv .
    $ bin/pip3 install -r requirements.txt  # Install Python dependencies
    $ # Install node.js v10.1.0 (npm is included, npm 5.6.0 version is needed)
    $ npm install
    $ npm run build
    $ cp plates/plates/build/static/css/*.css plates/plates/static/css/
    $ cp plates/plates/build/static/js/*.js plates/plates/static/js/
    $ cp plates/plates/build/index.html plates/plates/templates/index.html


## Usage

    $ source bin/activate
    $ ./plates/manage.py migrate            # Apply database migrations
    $ ./plates/manage.py createsuperuser    # Create admin user
    $ ./plates/manage.py collectstatic --noinput
    $ ./plates/manage.py runserver

Access the webpage at http://127.0.0.1:8000/

    $ deactivate
