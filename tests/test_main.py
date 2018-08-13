import pytest
from app import main

""" basic assert statements for asserting return contents of functions
"""


def test_apple():  # assert string
    assert main.eat() == 'eaten'


def test_inc():  # assert int
    assert main.inc(3) == 4
    # assert main.inc(3) == 5


""" test if a particular exception is raised:
    here, pytest.raises is used as a context manager
"""


def test_raise_exc():  # assert exception
    with pytest.raises(SystemExit):
        main.raise_exc()


def test_zero_division():  # assert exception
    # with pytest.raises(ZeroDivisionError):
    with pytest.raises(ZeroDivisionError, message="Expecting ZeroDivisionError"):
            main.zero_division(0)  # this exception is raised upon division by 0


def test_recursion_depth():  # to gain access to actual exception information
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
        assert 'maximum recursion' in str(excinfo.value)
        ''' execinfo in a ExceptionInfo instance, which is a wrapper around the actual 
            exception raised. The main attributes of interest are:
            
             .type
             .value
             .traceback
        '''



