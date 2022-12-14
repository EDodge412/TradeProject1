from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name="home"),
    path('login_user', views.login_user, name='login'),
    path('register_user', views.register_user, name='register'),
    path('mylistings', views.my_listings, name='my_listings'),
    path('listings', views.view_listings, name='view_listings'),
    path('logout_user', views.logout_user, name='log_out'),
    path('create', views.create_list, name='create'),
    path('search/', views.search_listing, name='search_listing'),
    path('delete/<int:listing_id>', views.delete_listing, name="delete_listing"),
    path('update/<int:listing_id>', views.update_listing, name='update_listing'),
    path('comment/', views.comment, name='comment'),
    path('comments/', views.view_comments, name='view_comments'),
    path('buy/', views.buy, name='buy_item'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
