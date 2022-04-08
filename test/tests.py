import unittest
from src.core import Base
from src.formats import Format


class TestBase(unittest.TestCase):
    def setUp(self) -> None:
        self.base = Base
        self.storage = {}
        self.format = Format

    def test_add_storage(self):
        pass
