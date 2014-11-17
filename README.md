pytest_simple_example
=====================

Simple example of a good project structure with pytest and sphinx implemented

Resources
---------

* Good pytest Practises: http://pytest.org/latest/goodpractises.html
* General Python testing information: http://pythontesting.net/start-here/
* Directory structure and getting started with writing a setup.py: 
https://pythonhosted.org/an_example_pypi_project/setuptools.html
* Writing a Python project from scratch: 
http://www.jeffknupp.com/blog/2013/08/16/open-sourcing-a-python-project-the-right-way/             
* Getting started with Sphinx: https://pythonhosted.org/an_example_pypi_project/sphinx.html

Getting Started
---------------

* Install the requirements by typing
```
pip install -r requirements.txt
```

Running Tests
-------------

* As recommended by http://pytest.org/latest/goodpractises.html: no 
```__init__.py``` file is included in the tests folder.
* To run the tests, you need to run the command:
```python
pip install -e .   # install package using setup.py in editable mode
```
* Then run the tests using 
```
py.test
``` 

