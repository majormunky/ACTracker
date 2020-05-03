from django.urls import path
from home import views


urlpatterns = [
	path('', views.index),
	path('fish/', views.fish),
	path('fish/<int:pk>/', views.fish_detail),
	path('fish/json/', views.fish_json),
	path('bugs/', views.bugs),
	path('bugs/<int:pk>/', views.bug_detail),
	path('bugs/json/', views.bugs_json),
]
