from django.shortcuts import render
from home import models


def index(request):
	return render(request, "home/index.html", {})


def fish(request):
	fish_list = models.Fish.objects.all().order_by("name")
	return render(request, "home/fish.html", {"fish_list": fish_list})
