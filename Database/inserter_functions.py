import Database.creation_tables


class Inserter_functions:
    def insert_products(self, data, Products):
        Products.get_or_create(
            name_product_fr=data["product_name_fr"],
            grade=data["nutriscore_grade"],
            store=data["stores"],
            url=data["url"],
        )

    def insert_categories(self, data, Categories):
        categories = data["categories"].split(",")
        for item in categories:
            Categories.get_or_create(category=item.lstrip().capitalize())

    def insert_products_with_categories(
        self, data, Products_with_Categories, Products, Categories
    ):
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
