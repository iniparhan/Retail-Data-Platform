# Database-Seeder
DB Seeder Faker PostgreSQL

## Setup
```bash
pip install -r requirements.txt
```

## Run Seeder
```bash
python main.py
```


## Path File

```
db_seeder/
│
├── main.py
│
├── config/
│   └── database.py
│
├── seeders/
│   ├── __init__.py
│   ├── category_seeder.py
│   ├── user_seeder.py
│   ├── product_seeder.py
│   ├── employee_seeder.py
│   ├── order_seeder.py
│   └── order_detail_seeder.py
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── category.py
│   ├── product.py
│   ├── employee.py
│   ├── order.py
│   └── order_detail.py
│
├── utils/
│   └── randomizer.py
│
├── requirements.txt
└── README.md
```

## ERD

Use dbdiagram to define your database structure
https://dbml.dbdiagram.io/

```SQL
Project smart_retail {
  database_type: 'PostgreSQL'
  Note: 'Description of the project'
}

Table users {
  customer_id integer [primary key]
  name varchar(255) [not null]
  email varchar(255) [not null]
  gender varchar(1) [not null]
  city varchar(255) [not null]
  join_date timestamp [default: `now()`]
  is_active bool [default: null]
}

Table category {
  category_id integer [primary key]
  category_name varchar(255) [not null]
  description varchar(255) [not null]
}

Table product {
  product_id integer [primary key]
  product_name varchar(255) [not null]
  price varchar(255) [not null]
  stock varchar(255) [not null]
  category_id integer [primary key]
  created_at timestamp [default: `now()`]
}

Table employee {
  employee_id integer [primary key]
  name varchar(255) [not null]
  role varchar(255) [not null]
  hire_date timestamp [default: `now()`]
}

Table order {
  order_id integer [primary key]
  customer_id integer [primary key]
  employee_id integer [primary key]
  order_date timestamp [default: `now()`]
  payment_method varchar(255) [not null]
  status varchar(255) [not null]
}

Table order_detail {
  order_detail_id integer [primary key]
  order_id integer [primary key]
  product_id integer [primary key]
  quantity varchar(255) [not null]
  unit_price varchar(255) [not null]
}

// Ref user_posts: posts.user_id > users.id // many-to-one

// Ref: users.id < follows.following_user_id

// Ref: users.id < follows.followed_user_id


Ref: "category"."category_id" < "product"."category_id"

Ref: "employee"."employee_id" < "order"."employee_id"

Ref: "users"."customer_id" < "order"."customer_id"

Ref: "product"."product_id" < "order_detail"."product_id"

Ref: "order"."order_id" < "order_detail"."order_id"
```