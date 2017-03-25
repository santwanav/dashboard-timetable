# Contribution Guidelines

This document is designed to get you setup to contribute to this repository. 

You need to setup a virtual environment for the best development experience.

1. Set up a python virtual environment.
2. Install the packages detailed in requirements.txt using pip

	```sh
	pip install -r requirements.txt
	```
3. Make changes, and as you go, keep testing.

Some details about what each file of importance does:

* server.py : takes care of the REST API
* models.py : Event model (for SQLAlchemy as well) 
* config.py : this reads the config.yml file and gets a basic config

Contact our IRC channel (freenode, ##DashBoard) for any further info required.
