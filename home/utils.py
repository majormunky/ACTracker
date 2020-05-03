import csv
import os
import time
from django.conf import settings
from home import models


def get_csv_contents(filepath):
	result = []
	with open(filepath, "r") as f:
		reader = csv.DictReader(f)
		for row in reader:
			result.append(row)
	return result


def get_month_data(item):
	result = {
		"january": item["Jan"] == "X",
		"february": item["Feb"] == "X",
		"march": item["Mar"] == "X",
		"april": item["Apr"] == "X",
		"may": item["May"] == "X",
		"june": item["Jun"] == "X",
		"july": item["Jul"] == "X",
		"august": item["Aug"] == "X",
		"september": item["Sep"] == "X",
		"october": item["Oct"] == "X",
		"november": item["Nov"] == "X",
		"december": item["Dec"] == "X",
	}
	return result


def import_fish_from_csv():
	results = {"created": 0, "skipped": 0}
	filepath = os.path.join(settings.BASE_DIR, "data", "fish.csv")
	fish_data = get_csv_contents(filepath)
	for fish in fish_data:
		existing_fish = models.Fish.objects.filter(name=fish["Name"])
		if existing_fish:
			results["skipped"] += 1
			continue

		fish_month_data = get_month_data(fish)
		
		if fish["Price"] == "" or fish["Price"] == " ":
			price = 0
		else:
			price = fish["Price"]

		new_fish = models.Fish(
			name=fish["Name"],
			location=fish["Where"].lower(),
			price=price,
			january=fish_month_data["january"],
			february=fish_month_data["february"],
			march=fish_month_data["march"],
			april=fish_month_data["april"],
			may=fish_month_data["may"],
			june=fish_month_data["june"],
			july=fish_month_data["july"],
			august=fish_month_data["august"],
			september=fish_month_data["september"],
			october=fish_month_data["october"],
			november=fish_month_data["november"],
			december=fish_month_data["december"],
		)
		new_fish.save()
		results["created"] += 1

	print("Finished")
	print("Created: {}".format(results["created"]))
	print("Skipped: {}".format(results["skipped"]))


def import_bugs_from_csv():
	results = {"created": 0, "skipped": 0}
	filepath = os.path.join(settings.BASE_DIR, "data", "bugs.csv")
	bug_data = get_csv_contents(filepath)
	for bug in bug_data:
		existing_bug = models.Bug.objects.filter(name=bug["Name"])
		if existing_bug:
			results["skipped"] += 1
			continue

		bug_month_data = get_month_data(bug)
		
		if bug["Price"] == "" or bug["Price"] == " ":
			price = 0
		else:
			price = bug["Price"]

		new_bug = models.Bug(
			name=bug["Name"],
			price=price,
			january=bug_month_data["january"],
			february=bug_month_data["february"],
			march=bug_month_data["march"],
			april=bug_month_data["april"],
			may=bug_month_data["may"],
			june=bug_month_data["june"],
			july=bug_month_data["july"],
			august=bug_month_data["august"],
			september=bug_month_data["september"],
			october=bug_month_data["october"],
			november=bug_month_data["november"],
			december=bug_month_data["december"],
		)
		new_bug.save()
		results["created"] += 1

	print("Finished")
	print("Created: {}".format(results["created"]))
	print("Skipped: {}".format(results["skipped"]))
