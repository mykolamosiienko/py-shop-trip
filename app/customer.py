from typing import List
from app.car import Car
from app.shop import Shop
class Customer():
    def __init__(self, name:str, product_cart: dict, location: List[int], money: int|float, car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def ride(self, end_location: List[int]):
        trip_cost = self.car.ride_cost(self.location, end_location)
        return trip_cost
    
    def shopping(self, shop: Shop):
        shopping_cost = shop.checkout(self.product_cart)
        return shopping_cost
    
    
        