from sqlalchemy import text
from config.database import engine
from utils.randomizer import fake

def seed_categories():
    categories = ["Electronics", "Fashion", "Food", "Books", "Sports"]

    with engine.connect() as conn:
        for cat in categories:
            conn.execute(text("""
                INSERT INTO category (category_name, description)
                VALUES (:name, :desc)
                ON CONFLICT (category_name) DO NOTHING
            """), {
                "name": cat,
                "desc": fake.sentence()
            })
        conn.commit()
