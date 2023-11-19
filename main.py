import requests
import json
import time
from datetime import datetime

def lookup_item(item_id):
	url = f"https://float.skinport.com/api/assets?item_id={item_id}"
	response = requests.get(url)
	data = response.json()
	return data["meta"]["count"]["total"]

def all_items():
	item_counts = {}
	i = 0 # used to pause after sending a bunch of requests
	with open("item_ids.json", encoding = "utf-8") as f:
		contents = json.load(f)
		total_items = len(contents)
		for item in contents:
			i += 1
			name = item["item"]
			count = lookup_item(item["id"])
			item_counts[name] = count
			if i % 50 == 0: # pause 10 seconds after every 50 items to not get ip banned / don't use up too many resources
				print(f"{i} / {total_items}")
				time.sleep(10)
	return dict(sorted(item_counts.items(), key=lambda item: item[1]))


if __name__ == "__main__":
	item_counts = all_items()
	current_day = datetime.today().strftime('%Y-%m-%d')
	with open("output/recent.json", "w", encoding = "utf-8") as f:
		json.dump(item_counts, f)
	with open(f"output/{current_day}.json", "w", encoding = "utf-8") as f:
		json.dump(item_counts, f)