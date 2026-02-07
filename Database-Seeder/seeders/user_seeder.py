from sqlalchemy import text
from config.database import engine
from utils.randomizer import fake, random_gender

def seed_users(n=100):
    with engine.connect() as conn:
        for _ in range(n):
            conn.execute(text("""
                INSERT INTO users (customer_name, email, gender, city, join_date, is_active)
                VALUES (:name, :email, :gender, :city, :join, :active)
            """), {
                "name": fake.name(),
                "email": fake.unique.email(),
                "gender": random_gender(),
                "city": fake.city(),
                "join": fake.date_time_this_year(),
                "active": fake.boolean()
            })
        conn.commit()
