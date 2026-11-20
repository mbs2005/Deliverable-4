class Temperature:
    def __init__(self, value, unit):            
        self.value = float(value)
        self.unit = unit.upper()
        
        if self.unit not in ['C', 'F', 'K']:
            raise ValueError("Invalid unit")
    
    @property    
    def value(self):
        return self._value
    
    @property
    def unit(self):
        return self._unit
    
    
    def to_celsius(self):
        if self.unit =='C':
            return self.value
        
        if self.unit == 'F':
            return (self.value - 32) * 5/9
        
        if self.unit == 'K':
            return self.value - 273.15
        
        
    def to_fahrenheit(self):
        if self.unit == 'F':
            return self.value
        
        if self.unit == 'C':
            return self.value * 9/5 + 32
        
        if self.unit == 'K':
            return (self.value - 273.15) * 9/5 + 32
        
        
    def to_kelvin(self):
        if self.unit == 'K':
            return self.value
        
        if self.unit == 'C':
            return self.value + 273.15
        
        if self.unit == 'F':
            return (self.value - 32) * 5/9 + 273.15      
        
        if self.to_kelvin() < 0:
            raise ValueError("Temperatur below absolute zero")
