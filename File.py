from enum import Enum


class File(Enum):
    cali = 1
    family = 2
    football = 3
    high_school = 4
    movie = 5
    shopping = 6
    snow = 7
    texas = 8
    weekend = 9

    def __str__(self):
        return f"{self.value} - {self.name}_tweets2014.txt"
