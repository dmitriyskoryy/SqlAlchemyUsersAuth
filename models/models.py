from datetime import datetime


from sqlalchemy import MetaData, Table, Column, JSON, Integer, String, TIMESTAMP, ForeignKey, Boolean


from auth.database import User

# Эта переменная содержит данные о таблицах, данных и тд
metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("date_creation", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, ForeignKey("role.id")),
    Column("is_active", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False)
)



