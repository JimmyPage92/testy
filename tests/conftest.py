#folder ktory zawiera kod ktory mozna importowac jak mamy testyktore wykorzystuja ten kod wiele razy
# komenda do uruchamiania testow: 'pytest .\tests\'
from typing import List

import pytest

@pytest.fixture
def todos_fixture() -> List[str]:
    return ["Clean my room", "Make my bed", "Go to school", "Do school homework"]