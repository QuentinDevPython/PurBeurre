import requests
from tqdm import tqdm


class Downloader:
    def __init__(self):

        self.all_data = list()
        self.request_url = "https://fr.openfoodfacts.org/cgi/search.pl"
        index = 1
        max_pages = 10
        try:
            for index in tqdm(range(max_pages)):
                self.params_for_request = {
                    "action": "process",
                    "page_size": 100,
                    "page": index + 1,
                    "json": 1,
                }
                response = requests.get(
                    self.request_url,
                    self.params_for_request
                )
                if response.status_code == 200:
                    self.all_data.extend(response.json()["products"])

        except requests.ConnectionError:
            print("Unable to connect")

    def get_all_data(self):
        return self.all_data
