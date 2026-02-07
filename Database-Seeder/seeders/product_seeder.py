import random
from sqlalchemy import text
from config.database import engine
from utils.randomizer import fake

def seed_products(n=50):
    with engine.connect() as conn:
        category_ids = [r[0] for r in conn.execute(text("SELECT category_id FROM category"))]

        for _ in range(n):
            conn.execute(text("""
                INSERT INTO product (product_name, price, stock, category_id, created_at)
                VALUES (:name, :price, :stock, :cat_id, :created)
            """), {
                "name": fake.catch_phrase(),
                "price": round(random.uniform(10000, 500000), 2),
                "stock": random.randint(1, 100),
                "cat_id": random.choice(category_ids),
                "created": fake.date_time_this_year()
            })
        conn.commit()
