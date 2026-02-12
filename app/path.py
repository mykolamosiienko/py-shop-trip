import json
import os

path = os.path.join("app", "config.json")
with open(path, "r") as f:
    f=json.load(f)
fuel_price = f.get("FUEL_PRICE")
shops = f.get("shops")
customers = f.get("customers")
