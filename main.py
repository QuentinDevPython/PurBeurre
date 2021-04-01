import Database.connector_database
from Database.creation_tables import (
    Products,
    Categories,
    Products_with_Categories,
    Favorites,
)
from Interface.interface import Interface


if __name__ == "__main__":

    interface = Interface(
        Products,
        Categories,
        Products_with_Categories,
        Favorites
    )
    interface.choose_download()
    interface.start()
    interface.choose_category()
