from mean.class_1 import Car
import pytest

class TestClass:

    def test_cond_1(self):
        prius = Car("Prius", "2004", "white")
        assert prius.condition('test') == "New"

    def test_cond_2(self):
        prius = Car("Prius", "2004", "white")
        prius.drive(1000)
        assert prius.condition('test') == "Used"

    def test_drive(self):
        prius = Car("Prius", "2004", "white")
        prius.drive(1000)
        assert prius.mileage == 1000

