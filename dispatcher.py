"""Dispatcher for the simulation"""

from __future__ import annotations
from typing import List
from typing import Optional
from driver import Driver
from rider import Rider, CANCELLED


class Dispatcher:
    """A dispatcher fulfills requests from riders and drivers for a
    ride-sharing service.

    When a rider requests a driver, the dispatcher assigns a driver to the
    rider. If no driver is available, the rider is placed on a waiting
    list for the next available driver. A rider that has not yet been
    picked up by a driver may cancel their request.

    When a driver requests a rider, the dispatcher assigns a rider from
    the waiting list to the driver. If there is no rider on the waiting list
    the dispatcher does nothing. Once a driver requests a rider, the driver
    is registered with the dispatcher, and will be used to fulfill future
    rider requests.

    Attributes:
        driver_fleet: Dispatcher registers the driver.
        drivers_waiting: List Drivers waiting for a rider.
        riders_waiting: Riders waiting for a driver.

    """
    driver_fleet: List
    drivers_waiting: List
    riders_waiting: List

    def __init__(self) -> None:
        """Initialize a Dispatcher.

        """
        self.driver_fleet = []
        self.drivers_waiting = []
        self.riders_waiting = []

    def __str__(self) -> str:
        """Return a string representation.

        """
        n_d = len(self.drivers_waiting)
        n_r = len(self.riders_waiting)
        r_d = len(self.driver_fleet)
        return "{} drivers waiting,{} riders waiting and" \
               " {} drivers registered".format(n_d, n_r, r_d)

    def request_driver(self, rider: Rider) -> Optional[Driver]:
        """Return a driver for the rider, or None if no driver is available.

        Add the rider to the waiting list if there is no available driver.

        """
        if not self.drivers_waiting:
            self.riders_waiting.append(rider)
            return None
        nearest = self.drivers_waiting[0]
        n_time = self.drivers_waiting[0].get_travel_time(rider.origin)
        for driver in self.drivers_waiting:
            if driver.get_travel_time(rider.origin) < n_time:
                n_time = driver.get_travel_time(rider.origin)
                nearest = driver
        driver = nearest
        return driver

    def request_rider(self, driver: Driver) -> Optional[Rider]:
        """Return a rider for the driver, or None if no rider is available.

        If this is a new driver, register the driver for future rider requests.

        """
        if driver not in self.driver_fleet:
            self.driver_fleet.append(driver)
        rider = None
        if driver.is_idle:
            if not self.riders_waiting:
                self.drivers_waiting.append(driver)
            else:
                rider = self.riders_waiting[0]
        return rider

    def cancel_ride(self, rider: Rider) -> None:
        """Cancel the ride for rider.

        """
        rider.status = CANCELLED

        # Remove the rider from waitlist if the rider is in the waitlist
        if rider in self.riders_waiting:
            self.riders_waiting.remove(rider)


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={'extra-imports': ['typing', 'driver', 'rider']})
