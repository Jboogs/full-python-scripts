from django.urls import path
from . import views

# this is my URL patterns
urlpatterns = [
    # django path module, with the url route, the view to render the page, name of page
    # using the primary key variable to pin-point database instances as <int:pk>
    path('search-trails/', views.mtb_trail_api, name='trailsearchapi'),
    path('mtb-news/', views.mtb_news_page, name='mountainbikenews'),
    path('about/', views.mtb_about, name='mtbabout'),
    path('ride-index/<int:pk>/details/delete_confirm', views.mtb_delete_confirm, name='confirmdelete'),
    path('ride-index/<int:pk>/details/update/', views.mtb_details_update, name='updatedetails'),
    path('ride-index/<int:pk>/details/', views.mtb_details, name='detailpage'),
    path('ride-index/', views.mtb_index_page, name='rideindex'),
    path('', views.mtb_home_page, name='mountainbikehome'),
    path('create-ride/', views.mtb_create_ride, name='createnewride')
]