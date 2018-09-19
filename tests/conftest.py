import sys
import pytest
from os.path import join, dirname
sys.path.append(join(dirname(__file__), "..", "src"))


@pytest.fixture
def automated_testing_db():
    db_path = join(dirname(__file__), "..", "automated_testing_db")
    return db_path
