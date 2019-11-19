from django.conf.urls import url
from . import views #.is current folder, views import

urlpatterns = [
    url(r'^$', views.index), #index function run
    url(r'^line_chart/json/m/$', views.line_chart_json_m, name='line_chart_json_m'),
    url(r'^line_chart/json/f/$', views.line_chart_json_f, name='line_chart_json_f'),
    url(r'^choices/category/$', views.choices),
    url(r'^choices/location/$', views.choicelocations),
]
