from django.urls import path
from . import views

app_name = 'adminapp'

urlpatterns = [
    path("home/",views.adminHome,name="tester"),  
    path("login/",views.login,name="login"),  
    path("logout/", views.logout, name='logout'),
    path("update-passw/", views.showUpdateUserPassw, name='update-passw'),
    path("register/",views.register,name="register"),  
    path("forgot-password",views.forgotPassword,name="forgot-password"),
    path("reset-password/<str:otpstring>/<str:userid>", views.showResetPassPage, name="reset-password/"),
    path("api-register/",views.apiAdminActions,name="api-register"),  
    path("view-service-centers/",views.showServiceCenters,name="view-service-centers"),  
    path("view-users-lists/",views.showUsersList,name="view-users-lists"),
    path("view-independent-services/<str:serviceid>",views.showIndependentServices,name="view-independent-services"),  
    path("view-independent-bikes/<str:bikeid>",views.showIndependentBikes,name="login"),  
    path("feedback-view/",views.showFeedbackhistory,name="feedback-view"),  
    path("add-bike-brand/", views.addBikeBrand, name="add-bike-brand"),
    path("view-super-users/", views.showSuperUsers, name="view-super-users"),
]