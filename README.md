* pytest project structure

* both the root and the test directories should not have an __init__
* from the project-root directory run pytest or python3 pytest -m 


```
project
│   README.md
│   documentation.txt    
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

Plugin architecture.
Auto discovery of test modules and functions.
Due to pytest's assertion and introspection, only plain assert statements are used.
