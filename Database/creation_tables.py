"""Import the module peewee to connect to MySQL and 
create the tables of the database"""
import peewee


mysql_database = peewee.MySQLDatabase(
    database="purBeurre",
    host="localhost",
    user="root",
    password="EMQG1371#psh9114S"
)


class BaseModel(peewee.Model):
    class Meta:
        database = mysql_database


class Products(BaseModel):
    id_product = peewee.AutoField(primary_key=True, unique=True)
    name_product_fr = peewee.CharField(150)
    grade = peewee.FixedCharField(1)
    store = peewee.CharField(150)
    url = peewee.CharField(150)


class Categories(BaseModel):
    id_category = peewee.AutoField(primary_key=True, unique=True)
    category = peewee.CharField(150, unique=True)


class Products_with_Categories(BaseModel):
    id_products_with_categories = peewee.AutoField(primary_key=True, unique=True)
    id_product = peewee.ForeignKeyField(Products)
    id_category = peewee.ForeignKeyField(Categories)


class Favorites(BaseModel):
    if_favorites = peewee.AutoField(primary_key=True, unique=True)
    id_product_to_substitute = peewee.ForeignKeyField(Products)
    id_product_substitute = peewee.ForeignKeyField(Products)


def create_tables():
    with mysql_database:
        mysql_database.create_tables(
            [Products, Categories, Products_with_Categories, Favorites]
        )


mysql_database.connect()

create_tables()
