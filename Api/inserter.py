from Database.inserter_functions import Inserter_functions
from tqdm import tqdm


class Inserter:
    def __init__(self, cleaned_data, Products, Categories, Products_with_Categories):
        self.cleaned_data = cleaned_data
        self.database_inserter = Inserter_functions()
        self.Categories = Categories
        self.Products = Products
        self.Products_with_Categories = Products_with_Categories

    def insert(self):
        for data in tqdm(self.cleaned_data):
            self.database_inserter.insert_products(data, self.Products)
            self.database_inserter.insert_categories(data, self.Categories)
            self.database_inserter.insert_products_with_categories(
                data,
                self.Products_with_Categories,
                self.Products,
                self.Categories
            )
