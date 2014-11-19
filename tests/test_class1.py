from mean.class_1 import Car
import pytest

class TestClass:

    @pytest.fixture(scope='function')
    def prius(self):                                                      
        return Car("Prius", "2004", "white")

    def test_cond_1(self, prius):
        assert prius.condition('test') == "New"

    def test_cond_2(self, prius):
        prius.drive(1000)
        assert prius.condition('test') == "Used"

    def test_drive(self, prius):
        prius.drive(1000)
        assert prius.mileage == 1000

