import sys
import os
import dotenv
import requests

class AllData:

	def __init__(self):

		dotenv.load_dotenv()
		self.all_data = list()
		index = 1
		self.request_url = "https://fr.openfoodfacts.org/cgi/search.pl"
		max_pages = int(os.getenv("P_MAX_PAGES"))

		try :
			for index in range(max_pages):
				self.params_for_request = {
					"action" : "process",
					"page_size" : os.gentenv("P_PAGE_SIZE"),
					"page" : index+1,
					"json" : 1
				}
				response = requests.get(self.request_url, self.params_for_request)
				if response.status_code == 200:
					self.all_data.extend(response.json()['products'])

		except requests.ConnectionError:
			print("Unable to connect")