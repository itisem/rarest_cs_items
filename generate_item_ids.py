import requests
import json

def generate_ids():
	base_url = "https://float.skinport.com/api/items?limit=100"
	item_ids = []
	generate_more_pages = True
	page = 1
	while generate_more_pages:
		url = base_url + f"&page={page}"
		response = requests.get(url)
		data = response.json()
		if page == 1:
			max_pages = data["meta"]["last_page"]
		if page >= max_pages:
			generate_more_pages = False
		for item in data["data"]:
			item_ids.append({"id": item["id"], "item": item["name"]})
		page += 1
	with open("item_ids.json", "w", encoding = "utf-8") as f:
		json.dump(item_ids, f)

if __name__ == "__main__":
	generate_ids()