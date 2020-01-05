from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('younger_user/<username>/', views.younger_user, name='younger_user'),
	path('elder_user/<username>/', views.elder_user, name='elder_user'),
	path('elder_profile/<username>/', views.elder_self_profile, name='elder_self_profile'),
	path('younger_profile/<username>/', views.younger_self_profile, name='younger_self_profile'),
    path('accounts/login/<type1>/', views.login_view, name='login'),
    path('accounts/register/<type1>/', views.register_view, name='register'),
    path('accounts/logout/', views.logout_view, name='logout'), 
    path('edit_profile_younger/<username>/', views.younger_edit_profile, name='younger_edit_profile'),
    path('edit_profile_elder/<username>/', views.elder_edit_profile, name='elder_edit_profile'),    
    path('number_of_oldies/<username>/<username1>/', views.number_of_oldies, name='number_of_oldies'),
    path('edit_current_status/<username>/',views.edit_current_status, name="edit_current_status"),
    path('remove/<username>/<username1>/', views.remove_user_from_current_status, name="remove_user_from_current_status"),
    path('add_elders/<username>/', views.add_elders_in_your_list, name="add_elders_in_your_list"),
    path('add_younger/<username>/', views.Add_younger_in_elder_table, name="Add_younger_in_elder_table"),
]