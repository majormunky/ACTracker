import datetime
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from home import models
from home import utils


def index(request):
	min_price = request.GET.get("min_price", None)
	now = timezone.now()
	current_tz = timezone.get_current_timezone()
	now = current_tz.normalize(now.astimezone(current_tz))
	month_name = now.strftime("%B").lower()
	month_filter = {month_name: True}
	midnight = datetime.time(0)

	fish_query = models.Fish.objects.filter(**month_filter)
	if min_price:
		fish_query = fish_query.filter(price__gt=min_price)
	fish_list = utils.get_things_active_now(fish_query, now.time())
	bug_query = models.Bug.objects.filter(**month_filter)
	if min_price:
		bug_query = bug_query.filter(price__gt=min_price)
	bug_list = utils.get_things_active_now(bug_query, now.time())
	return render(request, "home/index.html", {"fish_list": fish_list, "bug_list": bug_list, "now": now.time()})


def fish(request):
	fish_list = models.Fish.objects.all().order_by("name")
	return render(request, "home/fish.html", {"fish_list": fish_list})


def bugs(request):
	bug_list = models.Bug.objects.all().order_by("name")
	return render(request, "home/bugs.html", {"bug_list": bug_list})


def fish_detail(request, pk):
	fish_data = get_object_or_404(models.Fish, pk=pk)
	return render(request, "home/fish_detail.html", {"fish_data": fish_data})

def bug_detail(request, pk):
	bug_data = get_object_or_404(models.Bug, pk=pk)
	return render(request, "home/bug_detail.html", {"bug_data": bug_data})
