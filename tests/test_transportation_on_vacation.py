import pytest
from katas.kyu8.transportation_on_vacation import rental_car_cost

def test_rental_car_cost():
    assert rental_car_cost(1) == 40
    assert rental_car_cost(2) == 80
    assert rental_car_cost(3) == 100  # 120 - 20
    assert rental_car_cost(5) == 180  # 200 - 20
    assert rental_car_cost(7) == 230  # 280 - 50
    assert rental_car_cost(10) == 350  # 400 - 50


