from sqlalchemy import create_engine

# DB_URL = "postgresql://[nama username database]:[password database]@localhost:5432/[nama database]"
DB_URL = "postgresql://postgres:admin@localhost:5432/smart_retail"

engine = create_engine(DB_URL)  
