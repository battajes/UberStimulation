"""Drivers for the simulation"""

from location import Location, manhattan_distance
from rider import Rider


class Driver:
    """A driver for a ride-sharing service.

    Attributes:
        id: A unique identifier for the driver.
        location: The current location of the driver.
        destination: Possible destination.
        is_idle: True if the driver is idle and False otherwise.
        speed: The driver's car's speed, a constant.
    """

    id: str
    location: Location
    destination: Location
    is_idle: bool
    speed: int

    def __init__(self, identifier: str, location: Location, speed: int) -> None:
        """Initialize a Driver.

        """
        self.id = identifier
        self.location = location
        self.speed = speed
        self.destination = None
        self.is_idle = True

    def __str__(self) -> str:
        """Return a string representation.

        """
        return "Driver {}".format(self.id)

    def __eq__(self, other: object) -> bool:
        """Return True if self equals other, and false otherwise.

        """
        s_type = (isinstance(self, Driver) == isinstance(other, Driver))
        s_id = (self.id == other.id)
        return s_type and s_id

    def get_travel_time(self, destination: Location) -> int:
        """Return the time it will take to arrive at the destination,
        rounded to the nearest integer.

        """
        distance = manhattan_distance(self.location, destination)
        time = distance / self.speed
        return round(time)

    def start_drive(self, location: Location) -> int:
        """Start driving to the location.
        Return the time that the drive will take.

        """
        self.is_idle = False
        self.destination = location
        time = self.get_travel_time(self.destination)
        return int(time)

    def end_drive(self) -> None:
        """End the drive and arrive at the destination.

        Precondition: self.destination is not None.

        """
        self.is_idle = True
        if self.destination is not None:
            self.location, self.destination = self.destination, None

    def start_ride(self, rider: Rider) -> int:
        """Start a ride and return the time the ride will take.

        """
        self.is_idle = False
        self.destination, self.location = rider.destination, rider.origin
        time = self.get_travel_time(rider.destination)
        return int(time)

    def end_ride(self) -> None:
        """End the current ride, and arrive at the rider's destination.

        Precondition: The driver has a rider.
        Precondition: self.destination is not None.

        """
        if self.is_idle is False and self.destination is not None:
            self.location, self.destination = self.destination, None
            self.is_idle = True


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(
        config={'extra-imports': ['location', 'rider']})
