from seeders import seed_categories, seed_users, seed_products, seed_employees, seed_orders, seed_order_details 

def run():
    print("Seeding categories...")
    seed_categories()

    print("Seeding users...")
    seed_users()

    print("Seeding employees...")
    seed_employees()

    print("Seeding products...")
    seed_products()

    print("Seeding orders...")
    seed_orders()

    print("Seeding order details...")
    seed_order_details()

    print("Seeding completed successfully!")

if __name__ == "__main__":
    run()
