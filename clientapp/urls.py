from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name='logout'),
    path("forgot-password/", views.showForgotpassPage, name='forgot-password'),
    path("register/", views.userRegister, name="register"),
    path("reset-password/<str:otpstring>/<str:userid>", views.showResetPassPage, name="reset-password/"),
    path("book-service/<str:serviceid>/", views.showBookService, name="book-service"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("services/", views.services, name="services"),
    path('payment-page/<str:orderid>/', views.showPaymentPage, name='payment-page'),    
    path("sales/", views.showSales, name="sales"),
    path("team/", views.team, name="team"),
    path("purchase/<str:salesbikeid>/", views.showPurchaseForm, name="purchase"),
    path("purchase-details/<str:purchaseid>/", views.showPurchaseDetails, name="purchase-details"),
    path("testimonial/", views.testimonial, name="testimonial"),
    path('api-register/', views.mangaeApi, name='api-request'),
    path('view-service/<str:serviceid>/', views.showOneServiceProduct, name='view-service'),
    path('view-service-detail/<str:servicebbookid>/', views.showServiceDetails, name='view-service-detail'),
    path('view-sales-bike/<str:salesbikeid>/', views.showSalesBikeDetails, name='view-sales-bike'),
    path('book-sales-bike/<str:salesbikeid>/', views.showOneSalesBikeData, name='book-sales-bike'),
    path("profile-view/", views.showProfile, name="profile-view"),
    path("service-history/", views.showServiceHistory, name="service-history"),
    path("purchase-history/", views.showPurchaseHistory, name="purchase-history"),
    path('feedback/<str:serviceid>/', views.showFeedback, name='feedback'),
    path("contact/", views.showContact, name="contact"),
    path("pay-service-fee/<str:serviceid>",views.showPayServiceFee,name="pay-service-fee"),
    path("account-activate/<str:otp>/<str:userid>/<int:user_type>", views.userAccountEmailActivate, name="account-activate-activaten"),
    
]
