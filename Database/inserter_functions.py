"""Import the file creation_tables to insert the data
into the tables of the database"""
import Database.creation_tables


class Inserter_functions:
    """
    Class that defines how to insert the data into the database.
    This class is called by the class Inserter to insert the data.

    Args:
        None
    """

    def insert_products(self, data, Products):
        """
        Method that inserts the data collected and cleaned 
        into the table Products.
        """
        Products.get_or_create(
            name_product_fr=data["product_name_fr"],
            grade=data["nutriscore_grade"],
            store=data["stores"],
            url=data["url"],
        )

    def insert_categories(self, data, Categories):
        """
        Method that inserts the data collected and cleaned 
        into the table Categories.
        """
        categories = data["categories"].split(",")
        for item in categories:
            Categories.get_or_create(category=item.lstrip().capitalize())

    def insert_products_with_categories(
        self, data, Products_with_Categories, Products, Categories
    ):
        """
        Method that inserts the data collected and cleaned 
        into the table Products_with_Categories.
        """
        categories = data["categories"].split(",")
        for category in categories:
            categorized, created = Products_with_Categories.get_or_create(
                id_product=Products.get(
                    Products.name_product_fr == data["product_name_fr"]
                ),
                id_category=Categories.get(
                    Categories.category == category.lstrip().capitalize()
                ),
            )
