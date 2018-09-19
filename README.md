##### pytest project structure
# 

```
project
│   README.md
│   documentation.txt  
│   pytest.ini      
│
└───application
│   │   __init__.py
│   │    module.py
│   │
│   └───package
│       │   ...
│   
└───tests
    │   test_module.py
```
##### running pytest from terminal 
#
```
python3 -m pytest  
```

##### conftest.py - usage
#
conftest.py is primarily for defining fixtures where the defined fixtures are shared among all test suite tests. 

###### case: Fixtures
#
fixtures are defined for static data used by tests. This data can be accessed by all tests in the suite unless specified. 
This could be data as well as helpers of modules which will be passed to all tests.

###### case: External plugin loading
#
conftest.py is used to import external plugins or modules. By defining the following global variable, pytest will load the module and make it available for its test. 
Plugins are generally files defined in your project or other modules which might be needed in your tests. 

###### case: Hooks
#
You can specified hooks such as setup and teardown methods and much more to improve your tests


###### case: Test root path
#
This is a bit of a hidden feature. By defining conftest.py in your root path, 
you will have pytest recognizing your application modules without specifying PYTHONPATH. 
On the background, py.test modifies your sys.path by including all submodules which are found from the root path.
