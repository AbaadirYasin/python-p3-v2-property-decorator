# dog.py

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name='Fido', breed='Mastiff'):
        self._name = name.title()  # Initialize with a title-cased name
        self._breed = breed

    @property
    def name(self):
        """The name property"""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for the name property"""
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # Ensure the new name is title-cased
        else:
            raise ValueError("Name must be a string between 1 and 25 characters.")

    @property
    def breed(self):
        """The breed property"""
        return self._breed

    @breed.setter
    def breed(self, value):
        """Setter for the breed property"""
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            raise ValueError("Breed must be in the list of approved breeds.")
