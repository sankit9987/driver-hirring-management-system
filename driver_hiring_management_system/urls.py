from django.contrib import admin
from django.urls import path
from driver_hiring import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView,SetPasswordForm
from django.contrib.auth import views as auth_views
from driver_hiring.form import Password_reset,Password_confirm
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('vehicle', views.vehicle,name="vehicle"),
    path('books', views.books,name="books"),
    path('register', views.register,name="register"),
    path('user_logout', views.user_logout,name="user_logout"),
    path('login', views.Login,name="Login"),
    path('in-city', views.city,name="city"),
    path('out-station', views.out_station,name="out_station"),
    path('my-booking', views.my_booking,name="my_booking"),
    path("password-reset",auth_views.PasswordResetView.as_view(template_name="password-reset.html",form_class=Password_reset),name="password_reset"),


    path("password-reset/Done",auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),name="password_reset_done"),

    path("password-reset-confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_Confirm.html"), name="password_reset_confirm"),


    path("password-reset-complete/",auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_Complete.html"),name="password_reset_complete"),

    # Admin URL
    path('dashboard', views.dashboard,name="dashboard"),
    path('all-customer', views.customer,name="customer"),
    path('all-driver', views.driver,name="driver"),
    path('all-booking', views.booking,name="booking"),
    path('delete-customer/<int:id>', views.delete_customer,name="delete_customer"),
    path('delete-driver/<int:id>', views.delete_driver,name="delete_driver"),
    

    #Driver URl
    path('vehicle-details', views.add_vehical_detail,name="add_vehical_detail"),
    path('driver-dashboard', views.driver_dashboard,name="driver_dashboard"),
    path('edit-vehicle-details', views.edit_vehical_detail,name="edit_vehical_detail"),
    path('book', views.book,name="book"),
    path('change-password', views.change_password,name="change_password"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)