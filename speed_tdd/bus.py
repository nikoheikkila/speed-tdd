from dataclasses import dataclass
from enum import IntEnum


class BombState(IntEnum):
    UNARMED = 1
    ARMED = 2
    EXPLODED = 3


@dataclass
class Bomb:
    state: BombState = BombState.UNARMED
    trigger_speed: int = 50

    def arm(self) -> None:
        self.state = BombState.ARMED

    def explode(self) -> None:
        self.state = BombState.EXPLODED

    @property
    def is_unarmed(self) -> bool:
        return self.state == BombState.UNARMED

    @property
    def is_armed(self) -> bool:
        return self.state == BombState.ARMED

    @property
    def is_exploded(self) -> bool:
        return self.state == BombState.EXPLODED


@dataclass(unsafe_hash=True)
class Passenger:
    name: str
    is_alive: bool = True

    def kill(self) -> None:
        self.is_alive = False

    @property
    def is_hero(self) -> bool:
        return self.name == "Keanu Reeves"

    @property
    def is_dead(self) -> bool:
        return not self.is_alive


class Bus:
    speed: int
    passengers: set[Passenger]
    bomb: Bomb

    def __init__(self) -> None:
        self.speed = 0
        self.passengers = set()
        self.bomb = Bomb()

    def pick(self, *passengers: Passenger) -> None:
        for passenger in passengers:
            self.passengers.add(passenger)

    def accelerate(self, to: int) -> None:
        if to > self.speed:
            self.speed = to

        if self.should_arm_bomb:
            self.bomb.arm()

    def decelerate(self, to: int) -> None:
        if to < self.speed:
            self.speed = to

        if self.should_explode:
            self.explode()

    def explode(self) -> None:
        self.bomb.explode()

        if not self.is_hero_onboard:
            self.kill_all_passengers()

    def kill_all_passengers(self) -> None:
        [passenger.kill() for passenger in self.passengers]

    def driving_at(self, speed: int) -> bool:
        return self.speed == speed

    @property
    def should_arm_bomb(self) -> bool:
        return self.bomb.is_unarmed and self.speed >= self.bomb.trigger_speed

    @property
    def should_explode(self) -> bool:
        return self.bomb.is_armed and self.speed <= self.bomb.trigger_speed

    @property
    def is_hero_onboard(self) -> bool:
        return any(passenger.is_hero for passenger in self.passengers)

    @property
    def can_explode(self) -> bool:
        return self.bomb.is_armed

    @property
    def is_exploded(self) -> bool:
        return self.bomb.is_exploded
