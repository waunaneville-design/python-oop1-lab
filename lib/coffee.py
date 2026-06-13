#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self._size = size
        self._price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        valid_sizes = ("Small", "Medium", "Large")
        if value not in valid_sizes:
            print("size must be Small, Medium, or Large")
        else:
            self._size = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self._price += 1.0



