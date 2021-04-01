class Cleaner:
    """
    Class that takes in input all the data collected by the class Downloader.
    It cleans the data by conserving only data that has some specific
    characteristics (a product name in french, categories, a grade,
    an url and stores associated to it).

    Args:
        all_data (str dictionnary)
    """

    def __init__(self, all_data):

        self.data = all_data
        self.cleaned_data = list()

        for data_to_clean in self.data:
            if (
                data_to_clean.get("categories")
                and data_to_clean.get("nutriscore_grade")
                and data_to_clean.get("product_name_fr")
                and data_to_clean.get("url")
                and data_to_clean.get("stores")
            ):
                self.cleaned_data.append(data_to_clean)

        for data in self.cleaned_data:
            data["nutriscore_grade"] = data.get("nutriscore_grade").upper()
            data["categories"] = data.get("categories").lower()
            data["stores"] = data.get("stores").lower()
            data["product_name_fr"] = data.get("product_name_fr").lower()

    def get_cleaned_data(self):
        """
        Method that returns the data cleaned (it means only
        the data that has the characterics specified previously).
        """
        return self.cleaned_data
