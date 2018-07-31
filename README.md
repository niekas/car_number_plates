=== Introduction ===
This setup is provided for Linux OS (Debian flavor). python3 has to be
accessable via terminal. Access to the Internet is needed when using the
website, since JavaScript libraries are included from remote sources.

=== Preparing environment in Ubuntu/Debian ===
Note: these commands may need ``sudo`` rights.

    $ apt-get install python3-pip
    $ pip3 install virtualenv
    $ python3 -m venv .
    $ bin/pip3 install -r requirements.txt  # Install Python dependencies
    $ ./plates/manage.py migrate            # Apply database migrations

=== Usage ===

    $ source bin/activate
    $ ./plates/manage.py runserver

Access the webpage http://127.0.0.1:8000/

    $ deactivate
