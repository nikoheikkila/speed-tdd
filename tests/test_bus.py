from speed_tdd.bus import Bus, Passenger

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