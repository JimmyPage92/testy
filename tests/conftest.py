from typing import List

import pytest


@pytest.fixture
def todos_fixture() -> List[str]:
    return ["Clean my room", "Make my bed", "Go to school", "Do school homework"]