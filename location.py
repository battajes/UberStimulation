"""Locations for the simulation"""

from __future__ import annotations


class Location:
    """A two-dimensional location.

    Attributes:
        row: the number of blocks the location is from the bottom\
             edge of the grid.
        column: is the number of blocks the location is from the \
                left of the grid.

    """
    row: int
    column: int

    def __init__(self, row: int, column: int) -> None:
        """Initialize a location."""

        self.row = row
        self.column = column

    def __str__(self) -> str:
        """Return a string representation.

        """
        return "(%d, %d)" % (self.row, self.column)

    def __eq__(self, other: Location) -> bool:
        """Return True if self equals other, and false otherwise.

        """
        return self.row == other.row and self.column == other.column


def manhattan_distance(origin: Location, destination: Location) -> int:
    """Return the Manhattan distance between the origin and the destination.

    """
    length_x = abs(destination.row - origin.row)
    length_y = abs(destination.column - origin.column)
    return int(length_x + length_y)


def deserialize_location(location_str: str) -> Location:
    """Deserialize a location.

    location_str: A location in the format 'row,col'
    """

    x_y = location_str.split(',')
    x, y = int(x_y[0]), int(x_y[1])
    deserialize = Location(x, y)
    return deserialize


if __name__ == '__main__':
    import python_ta
    python_ta.check_all()
