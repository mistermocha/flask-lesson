# Flask Tutorial

The lessons here will show you how to the following:
* Set up a clean working virtualenv with flask
* Get your flask demo up and running
* Start hacking on flask

# Set up your environment

In a clean working directory, do the following:

```
mkdir flask-lesson
cd flask-lesson
virtualenv .
source bin/activate
pip install flask gunicorn
```

This will make a working directory that contains a local python environment which is separate
from the rest of your laptop. In it, we install flask and gunicorn

# What is Flask?

*Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. And before you
ask: It's BSD licensed!* 

# What is gunicorn?

*Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model ported
from Ruby's Unicorn project. The Gunicorn server is broadly compatible with various web frameworks,
simply implemented, light on server resources, and fairly speedy.*

# What do they do together?

* Gunicorn is a standalone app that hands off to one or more web services
* Flask is a framework that executes as a single app
* incoming -> `[gunicorn]` -> `[flask]`

# OK let's write some code
