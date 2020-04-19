from appliances.kitchen import DishWasher, CoffeeMaker, Refrigerator, Stove
from appliances.laundry import Dryer, Washer

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red", "warm")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

magic_chef_stove = Stove("mint")
magic_chef_stove.make_tea()