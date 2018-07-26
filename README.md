=== Introduction ===
This setup is provided for Linux OS (Debian flavor). Python3 has to be
accessable via terminal.

=== Preparing environment in Ubuntu/Debian ===
Note: these commands may need ``sudo`` rights.

    $ apt-get install python3-pip
    $ pip3 install virtualenv
    $ python3 -m venv .
    $ bin/pip3 install -r requirements.txt  # Install dependencies
    $ ./plates/manage.py migrate            # Apply database migrations

    $ source bin/activate
    $ deactivate
