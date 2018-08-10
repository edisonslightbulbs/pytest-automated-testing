from app import main


def test_apple():
    assert main.eat() == 'eaten'
