class Bomb:
    armed: bool
    exploded: bool

    def __init__(self) -> None:
        self.armed = False
        self.exploded = False

    @property
    def is_unarmed(self) -> bool:
        return self.armed == False

    @property
    def is_armed(self) -> bool:
        return self.armed == True

    @property
    def is_exploded(self) -> bool:
        return self.exploded == True

class Passenger:
    name: str
    is_alive: bool

    def __init__(self, name: str) -> None:
        self.name = name
        self.is_alive = True

    @property
    def is_hero(self) -> bool:
        return self.name == "Keanu Reeves"

    @property
    def is_dead(self) -> bool:
        return self.is_alive == False

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
            if self.speed <= 50 and self.bomb.is_armed:
                self.bomb.exploded = True
                if any(passenger.is_hero for passenger in self.passengers):
                    pass
                else:
                    for passenger in self.passengers:
                        passenger.is_alive = False