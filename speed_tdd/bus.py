class Bomb:
    armed: bool

    def __init__(self) -> None:
        self.armed = False

    @property
    def is_unarmed(self) -> bool:
        return self.armed == False

    @property
    def is_armed(self) -> bool:
        return self.armed == True

class Passenger:
    pass

class Bus:
    speed: int
    passengers: set[Passenger]
    bomb: Bomb

    def __init__(self) -> None:
        self.speed = 0
        self.passengers = set()
        self.bomb = Bomb()

    def pick(self, passenger: Passenger) -> None:
        self.passengers.add(passenger)

    def accelerate(self, speed: int) -> None:
        if speed > self.speed:
            self.speed = speed
            if self.speed >= 50 and self.bomb.is_unarmed:
                self.bomb.armed = True

    def decelerate(self, speed: int) -> None:
        if speed < self.speed:
            self.speed = speed