"""Import the module peewee to access to the 
tables of the database"""
import peewee

"""Import the class Dowloader to download the data"""
from Api.downloader import Downloader
"""Import the class Dowloader to clean the data"""
from Api.cleaner import Cleaner
"""Import the class Dowloader to insert the data"""
from Api.inserter import Inserter


class Interface:
    """
    Class that allows to interact with the user and to follow 
    its choices.

    Args:
        Products (table of the database)
        Categories (table of the database)
        Products_with_Categories (table of the database)
        Favorites (table of the database)
    """

    def __init__(self, Products, Categories, Products_with_Categories, Favorites):
        self.Products = Products
        self.Categories = Categories
        self.Products_with_Categories = Products_with_Categories
        self.Favorites = Favorites

    def start(self):
        """
        Method that confirms the launch of the program
        """
        print()
        print("------------------------")
        print("|    Server started    |")
        print("------------------------")
        print()

    def end(self):
        """
        Method that confirms the closure of the program
        """
        print()
        print("------------------------")
        print("|    Server closed     |")
        print("------------------------")
        print()

    def choose_download(self):
        """
        Method that asks to the user if he wants to download
        the data or not.
        """
        
        loop = 1

        while loop == 1:

            download_choice = input(
                "Voulez-vous télécharger la base de donnée ?\n\n"
                "1 - Oui \n"
                "2 - Non \n \n"
            )

            if download_choice == '1':
                loop = 0
                downloader = Downloader()
                all_data = downloader.get_all_data()
                cleaner = Cleaner(all_data)
                inserter = Inserter(
                    cleaner.get_cleaned_data(),
                    self.Products,
                    self.Categories,
                    self.Products_with_Categories
                )
                inserter.insert()
                print("La base de donnée a correctement été importée")
            elif download_choice == '2':
                loop = 0
                print("La base de donnée utilisée est celle téléchargée précédemment")
            else:
                print('\nJe n\'ai pas compris votre demande \n')

    def choose_category(self):
        """
        Method that asks the user to choose a category
        """

        loop = 1

        while loop == 1:

            action_choice = input(
                    "Que souhaitez-vous faire ? \n \n"
                    "1 - Choisir une catégorie \n"
                    "2 - Parcourir votre liste de produits \n"
                    "3 - Quitter \n \n"
            )

            if action_choice == '1':

                loop = 0

                query_5_random_categories = (
                    self.Categories.select().order_by(
                        peewee.fn.Rand()
                    ).limit(5)
                )
                dict_5_categories = [
                    categories.category
                    for categories in query_5_random_categories
                ]

                loop = 1
                while loop == 1:

                    index = 1

                    print("\nVoici quelques catégories : \n")
                    for category in dict_5_categories:
                        print(index, "-", category.lstrip().capitalize())
                        index += 1
                    index_category_chosen = input(
                        "\nQuelle catégorie souhaitez-vous consulter ? \n \n"
                    )
                    if index_category_chosen.isdecimal():
                        loop = 0
                        index_category_chosen = int(index_category_chosen)
                    else:
                        print("\nJe n'ai pas bien compris votre demande\n")
                    
                Interface.choose_product(
                    self, dict_5_categories[index_category_chosen - 1]
                )

            elif action_choice == '2':

                loop = 0

                query_all_favorites = self.Favorites.select()
                product_to_substitute_dict = [
                    favorites.id_product_to_substitute.name_product_fr
                    for favorites in query_all_favorites
                ]
                produit_substitute_dict = [
                    favorites.id_product_substitute.name_product_fr
                    for favorites in query_all_favorites
                ]

                if product_to_substitute_dict != []:
                    print(
                        "\nVoici les produits que vous avez choisi "
                        "de substituer avec leur substitut :\n"
                    )
                    for index in range(len(product_to_substitute_dict)):
                        print(
                            index + 1,
                            "-",
                            product_to_substitute_dict[index].capitalize(),
                            "==>",
                            produit_substitute_dict[index].capitalize(),
                        )

                else:
                    print("\nVous n'avez pas de favoris pour le moment")

                Interface.end(self)

            elif action_choice == '3':

                loop = 0
                Interface.end(self)

            else:
                print("\nJe n'ai pas bien compris votre demande\n")

    def choose_product(self, index_category_chosen):
        query_id_category = self.Categories.select().where(
            self.Categories.category == index_category_chosen
        )
        id_category = [category.id_category for category in query_id_category]
        query_id_products_chosen = self.Products_with_Categories.select().where(
            self.Products_with_Categories.id_category == id_category[0]
        )

        loop = 1
        while loop == 1:
            products_chosen_dict = []
            grade_chosen_dict = []
            index = 1

            print("\nVoici quelques produits de cette catégorie : \n")
            for product_with_category in query_id_products_chosen:
                print(
                    index,
                    "-",
                    product_with_category.id_product.name_product_fr.lstrip().capitalize(),
                    "- Nutriscore =",
                    product_with_category.id_product.grade.lstrip(),
                )
                products_chosen_dict.append(
                    product_with_category.id_product.name_product_fr.lstrip().capitalize()
                )
                grade_chosen_dict.append(product_with_category.id_product.grade.lstrip())
                index += 1
            product_chosen = input(
                "\nLequel de ces produits voulez-vous substitué ? \n \n"
            )
            
            if product_chosen.isdecimal():
                loop = 0
                product_chosen = int(product_chosen)
            else: 
                print("\nJe n'ai pas bien compris votre demande\n")

        Interface.give_1_substitute(
            self,
            products_chosen_dict[product_chosen - 1],
            grade_chosen_dict[product_chosen - 1],
        )

    def give_1_substitute(self, product_chosen, grade_chosen):

        if grade_chosen == "A":

            print(
                "\nCe produit est déjà excellent pour la santé ! Pas besoin de substitut !"
            )
            Interface.end(self)

        else:

            query_id_product_chosen = self.Products.select().where(
                self.Products.name_product_fr == product_chosen
            )
            product_id_chosen = [
                product.id_product for product in query_id_product_chosen
            ]

            query_categories_chosen = self.Products_with_Categories.select().where(
                self.Products_with_Categories.id_product == product_id_chosen[0]
            )
            categories_chosen_dict = [
                categories.id_category.category
                for categories in query_categories_chosen
            ]

            categories_chosen_id_dict = []

            for item in categories_chosen_dict:
                query_id_categories_chosen = self.Categories.select().where(
                    self.Categories.category == item
                )
                categories_chosen_id_dict += [
                    categories.id_category for categories in query_id_categories_chosen
                ]

            counter_dict = []
            product_dict = []
            id_product_verif_grade = []
            categories__id_dict = []

            grade_verif = []

            query = self.Products_with_Categories.select().order_by(
                self.Products_with_Categories.id_product.desc()
            )
            query_dict = [id_max.id_product.id_product for id_max in query]

            for index in range(1, query_dict[0] + 1):

                counter = 0

                query_verif_grade = self.Products.select().where(
                    self.Products.grade < grade_chosen
                )
                id_product_verif_grade = [
                    product.id_product for product in query_verif_grade
                ]

                for index2 in range(len(id_product_verif_grade)):
                    if id_product_verif_grade[index2] == index:
                        query_id_category = (
                            self.Products_with_Categories.select().where(
                                self.Products_with_Categories.id_product == index
                            )
                        )
                        categories__id_dict = [
                            categories.id_category.id_category
                            for categories in query_id_category
                        ]

                if categories__id_dict != []:
                    for item in categories__id_dict:
                        for item2 in categories_chosen_id_dict:
                            if item == item2:
                                counter += 1
                        if counter != 0:
                            counter_dict.append(counter)
                            product_dict.append(index)

            maximum = 0
            if counter_dict != []:
                for index in range(len(product_dict)):
                    if counter_dict[index] > maximum:
                        index_chosen = index
                        maximum = counter_dict[index]

                query_substitute = self.Products.select().where(
                    self.Products.id_product == product_dict[index_chosen]
                )
                name_product_substitute = [
                    product.name_product_fr for product in query_substitute
                ]
                grade_product_substitute = [
                    product.grade for product in query_substitute
                ]
                store_product_substitute = [
                    product.store for product in query_substitute
                ]
                store_product_substitute = store_product_substitute[0].split(",")
                url_product_substitute = [
                    product.url for product in query_substitute
                ]

                loop = 1
                while loop == 1:

                    print(
                        "\nUn des meilleurs substitut à votre produit est :",
                        name_product_substitute[0].capitalize(),
                        "\nNutriscore :",
                        grade_product_substitute[0],
                        "\nMagasins où le trouver :",
                        [store.lstrip().capitalize() for store in store_product_substitute],
                        "\nURL :",
                        url_product_substitute[0],
                        "\n"
                    )
                    save = input(
                            "Voulez vous le sauvegarder ? \n \n"
                            "1 - Oui et quitter \n"
                            "2 - Non et quitter \n \n"
                    )
                    if save.isdecimal():
                        loop = 0
                        save = int(save)
                    else:
                        print("\nJe n'ai pas bien compris votre demande\n")

                if save == 1:
                    Interface.save(self, name_product_substitute[0], product_chosen)
                else:
                    Interface.end(self)

            else:
                print("Pas de substitut possible !")
                Interface.end(self)

    def save(self, name_product_substitute, product_chosen):

        self.Favorites.get_or_create(
            id_product_to_substitute=self.Products.get(
                self.Products.name_product_fr == product_chosen
            ),
            id_product_substitute=self.Products.get(
                self.Products.name_product_fr == name_product_substitute
            ),
        )
        Interface.end(self)
