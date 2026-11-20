class Temperature:
    """
    Represent a tempreture for Celsius, Fahrenheit and Kelvin
    
    Supports conversions between units and comparison operations
    """
    TOLERANCE = 1e-9
    
    def __init__(self, value: float, unit: str) -> None:            
        self._value = float(value)
        self._unit = unit.upper()
        
        if self._unit not in ['C', 'F', 'K']:
            raise ValueError("Invalid unit")
        
        if self.to_kelvin() < -self.TOLERANCE:
            raise ValueError("Temperatur below absolute zero")
    
    @property    
    def value(self) -> float:
        return self._value
    
    @property
    def unit(self) -> str:
        return self._unit
    
    
    def to_celsius(self) -> float:
        """
        Coverts the temperature to Celsius
        
        Returns temperature in celsius as float
        """
        if self._unit =='C':
            return self._value
        
        if self._unit == 'F':
            return (self._value - 32) * 5/9
        
        if self._unit == 'K':
            return self._value - 273.15
        
        
    def to_fahrenheit(self) -> float:
        if self._unit == 'F':
            return self._value
        
        if self._unit == 'C':
            return self._value * 9/5 + 32
        
        if self._unit == 'K':
            return (self._value - 273.15) * 9/5 + 32
        
        
    def to_kelvin(self) -> float:
        if self._unit == 'K':
            return self._value
        
        if self._unit == 'C':
            return self._value + 273.15
        
        if self._unit == 'F':
            return (self._value - 32) * 5/9 + 273.15      

#Testing if the calss works
#temp = Temperature(0, "C")

#print(temp.to_fahrenheit())  #Expected answer: 32.0
#print(temp.to_kelvin())      #Expected answer: 273.15

    def convert_to(self, target_unit: str) -> 'Temperature':
        """
        Convert the temperature to the specific unit
        
        target_unit (str): the target temperature unit
        
        returns temperature object in the target unit
        
        raises ValueError if the target unit is invalid
        """
        target_unit = target_unit.upper()
        
        if target_unit == 'C':
            return Temperature(self.to_celsius(), 'C')
        
        if target_unit == 'F':
            return Temperature(self.to_fahrenheit(), 'F')
        
        if target_unit == 'K':
            return Temperature(self.to_kelvin(), 'K')
        
        raise ValueError("Invalid target unit")
    
    def __repr__(self) -> str:
        return f"Temperature({self._value}, '{self._unit}')"
 
#Tests if the __repr__ method works   
#temp = Temperature(25, "C")
#print(repr(temp))               #Expected answer: Temperature(25.0, 'C')

    def __str__(self) -> str:
        return f"{self._value:.2f} °{self._unit}"
    
#Tests if the __str__ method works
#temp = Temperature(25, 'C')
#print(str(temp))            #Expected answer: 25.00 °C

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        
        return abs(self.to_kelvin() - other.to_kelvin()) < self.TOLERANCE   
    def __ne__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        
        return not self == other
    
    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented 
        
        return self.to_kelvin() < other.to_kelvin()
    
    def __le__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        
        return self.to_kelvin() <= other.to_kelvin()
    
    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        
        return self.to_kelvin() > other.to_kelvin()
    
    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        
        return self.to_kelvin() >= other.to_kelvin()
    
#Tests if the comparison methods are working
#temp1 = Temperature(0, "C")
#temp2 = Temperature(32, "F")
#temp3 = Temperature(100, "C")

#print(temp1 == temp2)   # Expected answer:True
#print(temp1 != temp3)   # Expected answer:True
#print(temp1 < temp3)    # Expected answer:True
#print(temp3 > temp2)    # Expected answer:True
#print(temp1 <= temp2)   # Expected answer:True
#print(temp3 >= temp1)   # Expected answer:True