import random
from sqlalchemy import text
from config.database import engine

def seed_order_details(n=400):
    with engine.connect() as conn:
        orders = [r[0] for r in conn.execute(text("SELECT order_id FROM user_order"))]
        products = [(r[0], r[1]) for r in conn.execute(text("SELECT product_id, price FROM product"))]

        for _ in range(n):
            prod_id, price = random.choice(products)
            conn.execute(text("""
                INSERT INTO order_detail (order_id, product_id, quantity, unit_price)
                VALUES (:oid, :pid, :qty, :price)
            """), {
                "oid": random.choice(orders),
                "pid": prod_id,
                "qty": random.randint(1, 5),
                "price": price
            })
        conn.commit()
