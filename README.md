python_project_example
=====================

Simple example of a good project structure with pytest and sphinx implemented

Resources
---------

* Good pytest practises: http://pytest.org/latest/goodpractises.html
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

Building Documentation
----------------------

* The documentation is built on Sphinx.
* The Car class contains docstrings in 3 different styles:
    * Googley
    * Sphinxy
    * numpydoc
* To build HTML documentation:
```
cd doc
make html
```
* To build LaTeX documentation:
```
cd doc
make latex
cd build/latex
make
```

Importing into another project
------------------------------

The main project directory contains two files called `func_1.py` and 
`func_2.py`. They contain two useless functions called `avg` and `dim` which 
give the mean and shape of a given vector, respectively. In order to use these 
functions in other projects the `__init__.py` file requires the following lines

```
from .func_1 import *                                                           
from .func_2 import *
```

The `__init__.py` file is executed when the project is imported so these 
functions become available.

The steps are as follows:

* Install the package by running `$ pip install -e .` in the root directory.
* In your project/iPython, import as normal: `import mean as mean`.
* Can now use these function as `mean.avg([1,2,3])` which returns `3.0`.















