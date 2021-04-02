"""Import the module tqdm to add a loading bar"""
from tqdm import tqdm

"""Import the class Inserter_functions to insert the data 
in the database"""
from Database.inserter_functions import Inserter_functions


class Inserter:
    """
    Class that inserts the data collected and cleaned into the database by 
    calling the functions defined in Inserter_functions class

    Args:
        cleaned_data (str dictionnary)
        Products (table of the database)
        Categories (table of the database)
        Products_with_Categories (table of the database)
    """

    def __init__(self, cleaned_data, Products, Categories, Products_with_Categories):
        self.cleaned_data = cleaned_data
        self.database_inserter = Inserter_functions()
        self.Categories = Categories
        self.Products = Products
        self.Products_with_Categories = Products_with_Categories

    def insert(self):
        """
        Method that inserts the data collected and cleaned into the database
        """
        for data in tqdm(self.cleaned_data):
            self.database_inserter.insert_products(data, self.Products)
            self.database_inserter.insert_categories(data, self.Categories)
            self.database_inserter.insert_products_with_categories(
                data,
                self.Products_with_Categories,
                self.Products,
                self.Categories
            )
