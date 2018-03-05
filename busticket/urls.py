from django.conf.urls import url
from django.contrib import admin

from myapp import views
from myapp.views import FeedbackView, BusCompanyView, BusView, OrderView, LocationView, RouteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^api/v1/routes', RouteView.as_view(), name='routes_route'),
    url(r'^api/v1/locations', LocationView.as_view(), name='locations_route'),
    url(r'^api/v1/orders', OrderView.as_view(), name='orders_route'),
    url(r'^api/v1/customers', views.customers_route, name='customers_route'),
    url(r'^api/v1/buses', BusView.as_view(), name='buses_route'),
    url(r'^api/v1/bus_companys', BusCompanyView.as_view(), name='bus_companys_route'),
    url(r'^api/v1/feedbacks', FeedbackView.as_view(), name='feedback'),
]
