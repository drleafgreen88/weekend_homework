# WRITE YOUR FUNCTIONS HERE

#function to retrieve the name of the Pet Shop

def get_pet_shop_name(x):
    pet_shop = x["name"]
    return pet_shop

#function to retrieve the total amount of cash the Pet Shop is holding (admin)
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

#function to allow money to be added or subtracted from the Pet Shop's total cash
def add_or_remove_cash(pet_shop, money):
    pet_shop["admin"]["total_cash"] += money

#function to retrieve the total number of pets sold (admin)
def get_pets_sold(pet_shop):
    sold_pets = pet_shop["admin"]["pets_sold"]
    return sold_pets

#function to increase the number of pets sold
def increase_pets_sold(pet_shop, new_pet):
    pet_shop["admin"]["pets_sold"] += new_pet

#function to retrieve the stock count figure
def get_stock_count(pet_shop):
    count = len(pet_shop["pets"])
    return count

#function to retrieve how many pets are a particular breed
def get_pets_by_breed(pet_shop, pet_breed):
    matching_pets = []
    for pet in pet_shop["pets"]:
        if pet_breed == pet["breed"]:
            matching_pets.append(pet)
    return matching_pets

#function to find pet by name or return None
def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

#function to remove pet by name
def remove_pet_by_name(pet_shop, pet_name):
    pet = find_pet_by_name (pet_shop, pet_name)
    pet_shop["pets"].remove(pet)
        
#function to add a new pet to stock
def add_pet_to_stock (pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

#function to get customer cash
def get_customer_cash (customer):
    return customer["cash"]

#function to remove customer cash
def remove_customer_cash (customer, cash):
    customer["cash"] -= cash

#function to find customer's pet count
def get_customer_pet_count (customer):
    return len(customer["pets"])

#function to add pet to customer
def add_pet_to_customer (customer, new_pet):
    customer["pets"].append(new_pet)

#function to determine whether a customer can afford a pet
def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    else:
        return False

#function to sell pet to customer
#def sell_pet_to_customer(pet_shop, pet, customer):
