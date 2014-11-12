pytest_simple_example
=====================

Simple example of a good project structure with pytest and sphinx implemented

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

