from mean.class_1 import Car
import pytest

class TestClass:

    def test_desc(self):
        prius = Car("Prius", "2004", "white")
        assert type(prius.condition()) == str

