from Api.downloader import Downloader
from Api.cleaner import Cleaner
import Database.connector_database
from Database.creation_tables import (
    Products,
    Categories,
    Products_with_Categories,
    Favorites,
)
from Api.inserter import Inserter
from Interface.interface import Interface


if __name__ == "__main__":

    downloader = Downloader()
    all_data = downloader.get_all_data()
    cleaner = Cleaner(all_data)
    inserter = Inserter(
        cleaner.get_cleaned_data(),
        Products,
        Categories,
        Products_with_Categories
    )
    inserter.insert()
    interface = Interface(
        Products,
        Categories,
        Products_with_Categories,
        Favorites
    )
    interface.start()
    interface.choose_category()
