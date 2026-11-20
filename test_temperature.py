import pytest
from temperatur import Temperature

def test_case_insensitive() -> None:
    """
    Test that temperatures unites are handled in a case-insensitive manner
    """
    assert Temperature(25, "c").unit == "C"
    assert Temperature(25, "f").unit == "F"
    assert Temperature(25, "k").unit == "K"

def test_invalid_unit() -> None:
    """
    Test that an invalid temperature unit raises ValueError
    """
    with pytest.raises(ValueError):
        Temperature(25, "X")
        
def test_below_absolute_zero_kelvin() -> None:
    """
    Test that temperature below absolute zero raise ValueError
    """
    with pytest.raises(ValueError):
        Temperature(-1, "K")
        
def test_freezing_point() -> None:
    """
    Test converisons for the freezingpoint for water
    """
    temp = Temperature(0, "C")

    assert temp.to_fahrenheit() == 32
    assert temp.to_kelvin() == 273.15
    
def test_equality() -> None:
    """
    Test equality between equivalent temperatures in different units
    """
    assert Temperature(0, "C") == Temperature(32, "F")
    
def test_str() -> None:
    """
    Test the human readable string representation
    """
    assert str(Temperature(25, "C")) == "25.00 °C"
    
def test_repr() -> None:
    """
    Test the unambigous string representation
    """
    assert repr(Temperature(25, "C")) == "Temperature(25.0, 'C')"
    
def test_boiling_point() -> None:
    """
    Test conversions for the boiling point for water
    """
    temp = Temperature(100, "C")

    assert temp.to_fahrenheit() == 212
    assert temp.to_kelvin() == 373.15

def test_round_trip() -> None:
    """
    Test that converting between units and back preserves the original temperatures
    """
    temp = Temperature(25, "C")

    result = temp.convert_to("F").convert_to("K").convert_to("C")

    assert temp == result
    
def test_ordering() -> None:
    """
    Test comparison operators across temperatures
    """
    assert Temperature(0, "C") < Temperature(100, "C")
    assert Temperature(100, "C") > Temperature(0, "C")
    assert Temperature(0, "C") <= Temperature(32, "F")
    assert Temperature(0, "C") >= Temperature(32, "F")
