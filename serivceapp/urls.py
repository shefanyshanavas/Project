from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.adminHome, name="home"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name='logout'),
    path("register/", views.register, name="register"),
    path("forgot-password/", views.showForgotpassPage, name='forgot-password'),
    path("reset-password/<str:otpstring>/<str:userid>", views.showResetPassPage, name="reset-password/"),
    path("add-service/", views.addService, name="add-service"),
    
    path("add-new-bike/", views.addNewBikes, name="add-new-bike"),
    path("view-bikes/", views.viewBikes, name="view-bikes"),
    path("view-services/", views.viewServices, name="view-services"),
    path("view-services/edit/<str:service_id>", views.editServicesget, name="edit-services"),
    path('api-get-city/', views.mangaeApi, name='api-get-state'),
    path('api-register/', views.mangaeApi, name='api-register'),
    path("view-sales-bikes/edit/<str:bike_id>", views.editSalesBikeget, name="edit-services"),
    path("view-sales-bikes/edit-images/<str:bike_id>", views.editSalesBikeImageget, name="edit-services"),
    path("update-password/", views.updatePassword, name="update-password"),
    path("update-profile/", views.updateProfile, name="update-profile"),
    path("view-service-bookings", views.showServiceBokkings, name="view-service-bookings"),
    path("view-accepted-bookings", views.showAcceptedBokkings, name="view-accepted-bookings"),
    path("view-rejected-bookings", views.showRejectedBokkings, name="view-rejected-bookings"),
    path("view-completed-bookings", views.showCompletedBokkings, name="view-completed-bookings"),
    path("view-service-details/<str:servicebookid>", views.showServiceDetails, name="view-service-details"),
    path("view-service-feedbacks", views.showServiceFeedbacks, name="view-service-feedbacks"),
    path("view-sales-new-bookings", views.showSalesNewBokkings, name="view-sales-new-bookings"),
    path("view-purchase-details/<str:purchasebookid>", views.showPurchaseDetails, name="view-purchase-details"),
     path("view-sales-pending-booking", views.showSalesPendingBokkings, name="view-sales-pending-booking"),
    path("view-sales-completed-booking", views.showSalesCompletedBokkings, name="view-sales-completed-booking"),
     path("sales-analysis/", views.showSalesAnalysis, name="sales-analysis"),
]
