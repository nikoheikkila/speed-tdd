from speed_tdd.bus import Bus, Passenger

def test_bus_accepts_passengers() -> None:
    bus = Bus()
    passenger = Passenger()

    bus.pick(passenger)

    assert passenger in bus.passengers
