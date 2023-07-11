import sqlalchemy as sql, sqlalchemy.orm as sql_orm

Base = sql_orm.declarative_base()


class Publisher(Base):
    __tablename__ = "publisher"

    id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String(length=50))

class Book(Base):
    __tablename__ = "book"

    id = sql.Column(sql.Integer, primary_key=True)
    title = sql.Column(sql.String(length=100))
    id_publisher = sql.Column(sql.Integer, sql.ForeignKey("publisher.id"))

class Shop(Base):
    __tablename__ = "shop"

    id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String(length=30))

class Stock(Base):
    __tablename__ = "stock"

    id = sql.Column(sql.Integer, primary_key=True)
    id_book = sql.Column(sql.Integer, sql.ForeignKey("book.id"))
    id_shop = sql.Column(sql.Integer, sql.ForeignKey("shop.id"))
    count = sql.Column(sql.Integer)

class Sale(Base):
    __tablename__ = "sale"

    id = sql.Column(sql.Integer, primary_key=True)
    price = sql.Column(sql.Integer)
    date_sale = sql.Column(sql.Date)
    id_stock = sql.Column(sql.Integer, sql.ForeignKey("stock.id"))
    count = sql.Column(sql.Integer)
    