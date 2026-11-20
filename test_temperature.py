import pytest
from temperatur import Temperature

def test_case_insensitive():
    assert Temperature(25, "c").unit == "C"
    assert Temperature(25, "f").unit == "F"
    assert Temperature(25, "k").unit == "K"

def test_invalid_unit():
    with pytest.raises(ValueError):
        Temperature(25, "X")
        
def test_below_absolute_zero_kelvin():
    with pytest.raises(ValueError):
        Temperature(-1, "K")
        
def test_freezing_point():
    temp = Temperature(0, "C")

    assert temp.to_fahrenheit() == 32
    assert temp.to_kelvin() == 273.15
    
def test_equality():
    assert Temperature(0, "C") == Temperature(32, "F")
    
def test_str():
    assert str(Temperature(25, "C")) == "25.00 °C"
    
def test_repr():
    assert repr(Temperature(25, "C")) == "Temperature(25.0, 'C')"
    
def test_boiling_point():
    temp = Temperature(100, "C")

    assert temp.to_fahrenheit() == 212
    assert temp.to_kelvin() == 373.15
    
def test_round_trip():
    temp = Temperature(25, "C")

    result = temp.convert_to("F").convert_to("K").convert_to("C")

    assert temp == result
    
def test_ordering():
    assert Temperature(0, "C") < Temperature(100, "C")
    assert Temperature(100, "C") > Temperature(0, "C")
    assert Temperature(0, "C") <= Temperature(32, "F")
    assert Temperature(0, "C") >= Temperature(32, "F")

