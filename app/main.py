import datetime

from app.path import *
from app.shop import Shop
from app.customer import Customer
from app.car import Car



def shop_trip():
    time_now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    shops_objects = []
    customers_objects = []
    for shop in shops:
        shops_objects.append(Shop(shop.get("name"), shop.get("location"), shop.get("products")))
    
    for customer in customers:
        car_data = customer.get("car")
        car_name = car_data.get("brand")
        car_fuel = car_data.get("fuel_consumption")
        customers_objects.append(Customer(customer.get("name"), customer.get("product_cart"), customer.get("location"), customer.get("money"), Car(car_name, car_fuel) ))
    for customer in customers_objects:
        total = {}
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops_objects:
            ride_cost = 2*customer.ride(shop.location)
            shop_cost = customer.shopping(shop)
            total_sum = ride_cost + shop_cost 
            total.update({shop: total_sum})
            formatted = f"{(total_sum):.2f}".rstrip("0").rstrip(".")
            print(f"{customer.name}'s trip to the {shop.name} costs {formatted}")
        chipest_place = min(total.items(), key=lambda item: item[1])
        chipest_shop_name = chipest_place[0]
        if customer.money >= chipest_place[1]:
            customer.money -= chipest_place[1]
            print(f"{customer.name} rides to {chipest_shop_name.name}\n")
            print(f"Date: {time_now}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            chipest_shop_cost = 0
            for name, quan in customer.product_cart.items():
                price_per_item = chipest_shop_name.products[name]
                chipest_shop_cost += quan*price_per_item
                if quan > 1:
                    name += "s"
                print(f"{quan} {name} for {str(quan*price_per_item).rstrip("0").rstrip(".")} dollars")
                    

            print(f"Total cost is {chipest_shop_cost} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money:.2f} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")



    





shop_trip()