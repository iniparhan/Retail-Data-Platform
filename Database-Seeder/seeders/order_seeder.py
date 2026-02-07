import random
from sqlalchemy import text
from config.database import engine
from utils.randomizer import fake, random_payment, random_status

def seed_orders(n=200):
    with engine.connect() as conn:
        users = [r[0] for r in conn.execute(text("SELECT customer_id FROM users"))]
        employees = [r[0] for r in conn.execute(text("SELECT employee_id FROM employee"))]

        for _ in range(n):
            conn.execute(text("""
                INSERT INTO user_order (customer_id, employee_id, order_date, payment_method, status)
                VALUES (:cust, :emp, :date, :pay, :status)
            """), {
                "cust": random.choice(users),
                "emp": random.choice(employees),
                "date": fake.date_time_this_year(),
                "pay": random_payment(),
                "status": random_status()
            })
        conn.commit()
