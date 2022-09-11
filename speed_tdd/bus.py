class Passenger:
    pass

class Bus:
    passengers: set[Passenger]

    def __init__(self) -> None:
        self.passengers = set()

    def pick(self, passenger: Passenger) -> None:
        self.passengers.add(passenger)