import random
from faker import Faker

fake = Faker("id_ID")

def random_gender():
    return random.choice(["Male", "Female"])

def random_payment():
    return random.choice(["Cash", "Credit Card", "E-Wallet", "Transfer"])

def random_status():
    return random.choice(["pending", "paid", "cancelled", "shipped"])

def random_employee_role():
    return random.choice(["Admin", "Cashier", "Manager", "Warehouse"])

def random_category():
    return random.choice(["Electronics", "Fashion", "Food", "Books", "Sports"])
