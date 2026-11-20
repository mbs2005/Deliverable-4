class Temperature:
    """
    Represents a temperature in Celsius, Fahrenheit, or Kelvin.

    Supports temperature conversion, validation against absolute zero,
    and comparison operations across different temperature units.
    """

    TOLERANCE = 1e-9

    def __init__(self, value: float, unit: str) -> None:
        """
        Initialize a Temperature object.

        Args:
            value (float): The temperature value.
            unit (str): The temperature unit ('C', 'F', or 'K').

        Raises:
            ValueError: If the unit is invalid.
            ValueError: If the temperature is below absolute zero.
        """
        self._value = float(value)
        self._unit = unit.upper()

        if self._unit not in ["C", "F", "K"]:
            raise ValueError("Invalid unit")

        if self.to_kelvin() < -self.TOLERANCE:
            raise ValueError("Temperature below absolute zero")

    @property
    def value(self) -> float:
        """
        Return the temperature value.

        Returns:
            float: The temperature value.
        """
        return self._value

    @property
    def unit(self) -> str:
        """
        Return the temperature unit.

        Returns:
            str: The temperature unit ('C', 'F', or 'K').
        """
        return self._unit

    def to_celsius(self) -> float:
        """
        Convert the temperature to Celsius.

        Returns:
            float: Temperature in degrees Celsius.
        """
        if self._unit == "C":
            return self._value

        if self._unit == "F":
            return (self._value - 32) * 5 / 9

        if self._unit == "K":
            return self._value - 273.15

    def to_fahrenheit(self) -> float:
        """
        Convert the temperature to Fahrenheit.

        Returns:
            float: Temperature in degrees Fahrenheit.
        """
        if self._unit == "F":
            return self._value

        if self._unit == "C":
            return self._value * 9 / 5 + 32

        if self._unit == "K":
            return (self._value - 273.15) * 9 / 5 + 32

    def to_kelvin(self) -> float:
        """
        Convert the temperature to Kelvin.

        Returns:
            float: Temperature in Kelvin.
        """
        if self._unit == "K":
            return self._value

        if self._unit == "C":
            return self._value + 273.15

        if self._unit == "F":
            return (self._value - 32) * 5 / 9 + 273.15

    def convert_to(self, target_unit: str) -> "Temperature":
        """
        Convert the temperature to the specified unit.

        Args:
            target_unit (str): The target unit ('C', 'F', or 'K').

        Returns:
            Temperature: A new Temperature object in the target unit.

        Raises:
            ValueError: If the target unit is invalid.
        """
        target_unit = target_unit.upper()

        if target_unit == "C":
            return Temperature(self.to_celsius(), "C")

        if target_unit == "F":
            return Temperature(self.to_fahrenheit(), "F")

        if target_unit == "K":
            return Temperature(self.to_kelvin(), "K")

        raise ValueError("Invalid target unit")

    def __repr__(self) -> str:
        """
        Return an unambiguous representation of the object.

        Returns:
            str: Developer-friendly representation.
        """
        return f"Temperature({self._value}, '{self._unit}')"

    def __str__(self) -> str:
        """
        Return a human-readable representation of the temperature.

        Returns:
            str: Temperature formatted with two decimal places.
        """
        return f"{self._value:.2f} °{self._unit}"

    def __eq__(self, other: object) -> bool:
        """
        Check whether two temperatures are equal.

        Args:
            other (object): Object to compare with.

        Returns:
            bool: True if the temperatures are equal.
        """
        if not isinstance(other, Temperature):
            return NotImplemented

        return abs(self.to_kelvin() - other.to_kelvin()) <= self.TOLERANCE

    def __ne__(self, other: object) -> bool:
        """
        Check whether two temperatures are not equal.

        Args:
            other (object): Object to compare with.

        Returns:
            bool: True if the temperatures are different.
        """
        if not isinstance(other, Temperature):
            return NotImplemented

        return not self == other

    def __lt__(self, other: object) -> bool:
        """
        Check whether this temperature is less than another.

        Args:
            other (object): Object to compare with.

        Returns:
            bool: True if this temperature is lower.
        """
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_kelvin() < other.to_kelvin()

    def __le__(self, other: object) -> bool:
        """
        Check whether this temperature is less than or equal to another.

        Args:
            other (object): Object to compare with.

        Returns:
            bool: True if this temperature is less than or equal.
        """
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_kelvin() <= other.to_kelvin()

    def __gt__(self, other: object) -> bool:
        """
        Check whether this temperature is greater than another.

        Args:
            other (object): Object to compare with.

        Returns:
            bool: True if this temperature is greater.
        """
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_kelvin() > other.to_kelvin()

    def __ge__(self, other: object) -> bool:
        """
        Check whether this temperature is greater than or equal to another.

        Args:
            other (object): Object to compare with.

        Returns:
            bool: True if this temperature is greater than or equal.
        """
        if not isinstance(other, Temperature):
            return NotImplemented

        return self.to_kelvin() >= other.to_kelvin()