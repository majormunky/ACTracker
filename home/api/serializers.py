from rest_framework import serializers
from home import models


class FishSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Fish
		fields = [
			"id",
			"name",
			"price",
			"location",
			"all_day",
			"start_time",
			"end_time",
			"january",
			"february",
			"march",
			"april",
			"may",
			"june",
			"july",
			"august",
			"september",
			"october",
			"november",
			"december"
		]


class BugSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Bug
		fields = [
			"id",
			"name",
			"price",
			"all_day",
			"start_time",
			"end_time",
			"january",
			"february",
			"march",
			"april",
			"may",
			"june",
			"july",
			"august",
			"september",
			"october",
			"november",
			"december"
		]
