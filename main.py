import sqlalchemy, sqlalchemy.orm
import models
from datetime import date
import json as JSON

with open("config.json") as config:
    config = JSON.load(config)

author = input("Введите автора: ")

engine = sqlalchemy.create_engine(f"{config['dbType']}://{config['username']}:{config['password']}@{config['host']}:{config['port']}/{config['dbName']}")

session = sqlalchemy.orm.sessionmaker(engine)()

q = session.query(models.Book.title, models.Shop.name, models.Sale.price, models.Sale.date_sale)\
    .join(models.Stock, models.Stock.id == models.Sale.id_stock)\
    .join(models.Book, models.Stock.id_book == models.Book.id)\
    .join(models.Shop, models.Shop.id == models.Stock.id_shop)\
    .join(models.Publisher, models.Publisher.id == models.Book.id_publisher)\
    .filter(models.Publisher.name == author)

session.close()

if (len(q.all()) == 0):
    print("По вашему запросу ничего не найдено")
    exit(0)

print(f"{'Название':<10} | {'Название магазина':<17} | {'Цена':<4} | {'Дата продажи'}")
print("="*53, end="\n\n")

for i in q:
    print(f"{i[0]:<10} | {i[1]:<17} | {i[2]:<4} | {date.isoformat(i[3])}")
