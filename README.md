# pytest project structure

 both the root and the test directories should not have an __init__
 
 from the project-root directory run python3 -m pytest  
 


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
