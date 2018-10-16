from django.conf.urls import include, url
from django.contrib import admin
from webapp import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', views.index, {"template_name": "index.html"},  name="index"),
    # url(r'^search/paper/$', views.search_paper, {"template_name": "search_paper.html"},  name="search_paper"),

]
