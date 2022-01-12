"""
The rider module contains the Rider class. It also contains
constants that represent the status of the rider.

=== Constants ===
WAITING: A constant used for the waiting rider status.
CANCELLED: A constant used for the cancelled rider status.
SATISFIED: A constant used for the satisfied rider status
"""
from __future__ import annotations
from location import Location


WAITING = "waiting"
CANCELLED = "cancelled"
SATISFIED = "satisfied"


class Rider:

    """A rider for a ride-sharing service.

    Attributes:
        id: A unique identifier for a rider.
        patience: Number of time units the rider will wait to be picked up
                  before they cancel their ride.
        origin: Unique origin of a rider.
        destination: Unique destination of a rider.
        status: One of waiting to be picked up, cancelled or satisfied.

    """
    id: str
    patience: int
    origin: Location
    destination: Location
    status: WAITING or CANCELLED or SATISFIED

    def __init__(self, identifier: str, patience: int, origin: Location,
                 destination: Location) -> None:
        """Initialize a Rider.

        """
        self.id = identifier
        self.patience = patience
        self.origin = origin
        self.destination = destination
        self.status = WAITING

    def __str__(self) -> str:
        """Return a string representation.

        """
        return "Rider {}".format(self.id)

    def __eq__(self, other: Rider) -> bool:
        """Return True if self equals other, and false otherwise.

        """
        a = (isinstance(self, Rider) == isinstance(other, Rider))
        b = (self.id == other.id)
        c = (self.origin == other.origin)
        d = (self.destination == other.destination)
        e = (self.status == other.status)
        f = (self.patience == other.patience)
        return a and b and c and d and e and f


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={'extra-imports': ['location']})
