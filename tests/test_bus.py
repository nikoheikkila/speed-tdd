from pytest import fixture
from speed_tdd.bus import Bus, Passenger


@fixture
def bus() -> Bus:
    return Bus()


@fixture
def driver() -> Passenger:
    return Passenger(name="Sandra Bullock")


@fixture
def hero() -> Passenger:
    return Passenger(name="Keanu Reeves")


def test_bus_accepts_passengers(bus: Bus, driver: Passenger) -> None:
    bus.pick(driver)

    assert driver in bus.passengers


def test_bus_can_accelerate_to_given_speed(bus: Bus) -> None:
    bus.accelerate(to=20)

    assert bus.driving_at(speed=20)


def test_bus_cannot_accelerate_to_lower_speed(bus: Bus) -> None:
    bus.accelerate(to=20)
    bus.accelerate(to=10)

    assert bus.driving_at(speed=20)


def test_bus_can_decelerate_to_given_speed(bus: Bus) -> None:
    bus.accelerate(to=20)
    bus.decelerate(to=10)

    assert bus.driving_at(speed=10)


def test_bus_cannot_decelerate_to_higher_speed(bus: Bus) -> None:
    bus.accelerate(to=20)
    bus.decelerate(to=30)

    assert bus.driving_at(speed=20)


def test_bus_has_an_unarmed_bomb(bus: Bus) -> None:
    assert not bus.can_explode


def test_when_the_bus_accelerates_to_50_mph_the_bomb_is_armed(bus: Bus) -> None:
    bus.accelerate(to=50)

    assert bus.can_explode


def test_when_the_bomb_is_armed_and_the_bus_decelerates_to_50_mph_the_bomb_explodes(
    bus: Bus, driver: Passenger
) -> None:
    bus.pick(driver)

    bus.accelerate(to=51)
    bus.decelerate(to=50)

    assert bus.is_exploded
    assert driver.is_dead


def test_hero_can_save_the_day_from_bus_explosion(
    bus: Bus, driver: Passenger, hero: Passenger
) -> None:
    bus.pick(driver, hero)

    bus.accelerate(to=51)
    bus.decelerate(to=50)

    assert bus.is_exploded
    assert driver.is_alive
    assert hero.is_alive
