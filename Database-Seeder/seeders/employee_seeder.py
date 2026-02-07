from sqlalchemy import text
from config.database import engine
from utils.randomizer import fake, random_employee_role

def seed_employees(n=10):
    with engine.connect() as conn:
        for _ in range(n):
            conn.execute(text("""
                INSERT INTO employee (employee_name, employee_role, hire_date)
                VALUES (:name, :role, :hire)
            """), {
                "name": fake.name(),
                "role": random_employee_role(),
                "hire": fake.date_between(start_date='-3y', end_date='today')
            })
        conn.commit()
