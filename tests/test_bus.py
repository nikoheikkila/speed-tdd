from speed_tdd.bus import Bus, Passenger, Explosion
from pytest import raises

def test_bus_accepts_passengers() -> None:
    bus = Bus()
    passenger = Passenger()

    bus.pick(passenger)

    assert passenger in bus.passengers

def test_bus_can_accelerate_to_given_speed() -> None:
    bus = Bus()
    bus.accelerate(20)

    assert bus.speed == 20

def test_bus_cannot_accelerate_to_lower_speed() -> None:
    bus = Bus()
    bus.accelerate(20)
    bus.accelerate(10)

    assert bus.speed == 20

def test_bus_can_decelerate_to_given_speed() -> None:
    bus = Bus()
    bus.accelerate(20)
    bus.decelerate(10)

    assert bus.speed == 10

def test_bus_cannot_decelerate_to_higher_speed() -> None:
    bus = Bus()
    bus.accelerate(20)
    bus.decelerate(30)

    assert bus.speed == 20

def test_bus_has_an_unarmed_bomb() -> None:
    bus = Bus()

    assert bus.bomb.is_unarmed

def test_when_the_bus_accelerates_to_50_mph_the_bomb_is_armed() -> None:
    bus = Bus()
    bus.accelerate(50)

    assert bus.bomb.is_armed

def test_when_the_bomb_is_armed_and_the_bus_decelerates_to_50_mph_the_bomb_explodes() -> None:
    bus = Bus()
    bus.accelerate(51)

    with raises(Explosion):
        bus.decelerate(50)
