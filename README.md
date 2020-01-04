# django-rest-framework-DRF--venture task
**Setting up a virtualenv**

virtualenv is a nifty tool for creating virtual environments for Python projects

	cd ~
	virtualenv env
	source ~/env/bin/activate

If you find it tedious to do the above everytime you log in you can copy the snippet below in to a file named *~/.bash_profile* and You will automatically land in the project folder everytime you log in with the virtualenv activated.

	source ~/env/bin/activate
	cd ~/project

Try logging out from your ssh session and log in to see if the snippet above works.


**Install the Python dependencies for the project**

Make sure your virtualenv is active, the name of the env wrapped in round brackets should appear next to your username@hostname in the terminal.

	(env)johndoe@uduntu:~$

And then run

	pip install -r ~/project/requirements.txt

**Fresh migrations run for a project**

    python manage.py makemigrations 
    python manage.py migrate

**Fresh db run for a project for a specific api**

    rm -f tmp.db db.sqlite3
    rm -r apifolder/migrations
    python manage.py makemigrations apifolder
    python manage.py migrate

And then run

    python manage.py runserver