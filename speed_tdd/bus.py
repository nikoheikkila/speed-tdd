class Passenger:
    pass

class Bus:
    speed: int
    passengers: set[Passenger]

    def __init__(self) -> None:
        self.speed = 0
        self.passengers = set()

    def pick(self, passenger: Passenger) -> None:
        self.passengers.add(passenger)

    def accelerate(self, speed: int) -> None:
        self.speed = speed