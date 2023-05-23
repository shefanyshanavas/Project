from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
import json
from .models import BasicClientActionDB, BasicClientHelperCls

# Create your views here.

# basic template returning


def home(request):
    return render(request, "clientapp/index.html", context={"request": request})



def userAccountEmailActivate(request, otp, userid, user_type):
    actionObj = BasicClientActionDB()

    if actionObj.activateAccountByEmail(otp, userid, user_type):
        return render(
            request,
            "clientapp/login.html",
            {"status": 1},
        )
    else:
        return render(request, "clientapp/login.html", {"status": 2})


def showResetPassPage(request, otpstring, userid):
    actionObj = BasicClientHelperCls()
    if actionObj.validateResetPassRequest(otpstring, userid):
        return render(
            request,
            "clientapp/reset-password.html",
            {"payload": actionObj.validateResetPassRequest(otpstring, userid)},
        )
    else:
        return render(request, "clientapp/send-forgot-pass-mail.html")


def showForgotpassPage(request):
    return render(request, "clientapp/send-forgot-pass-mail.html")


def showProfile(request):
    if get_session_userid(request):
        actionObj = BasicClientActionDB()
        return render(
            request,
            "clientapp/profile.html",
            {
                "payload": actionObj.getUserProfileData(get_session_userid(request)),
                "address": actionObj.getUserProfileData(get_session_userid(request)),
                "state_data": actionObj.getStateData(),
            },
        )
    else:
        return render(request, "clientapp/login.html")



def showOneSalesBikeData(request, salesbikeid):
    if get_session_userid(request):
        actionObj = BasicClientActionDB()
        if actionObj.validateSalesBike(salesbikeid):
            return render(
                request,
                "clientapp/purcahse-form.html",
                {
                    "payload": actionObj.getSalesBikeData1(
                        get_session_userid(request), salesbikeid
                    )
                },
            )
        else:
            return render(
                request,
                "clientapp/sales.html",
                {
                    "payload": actionObj.getSalesBikeData(),
                    "recomended": actionObj.getRecomSalesBikeData(),
                    "states": actionObj.getStateData(),
                },
            )
    else:
        return render(request, "clientapp/login.html")


def showServiceDetails(request, servicebbookid):
    if get_session_userid(request):
        actionObj = BasicClientActionDB()
        if actionObj.validateServiceBook(servicebbookid):
            return render(
                request,
                "clientapp/service-detail.html",
                {
                    "payload": actionObj.getUserServiceData1(
                        get_session_userid(request), servicebbookid
                    )
                },
            )
        else:
            return render(
                request,
                "clientapp/service-history.html",
                {"payload": actionObj.getUserServiceData(get_session_userid(request))},
            )
    else:
        return render(request, "clientapp/login.html")


def showSalesBikeDetails(request, salesbikeid):
    if get_session_userid(request):
        actionObj = BasicClientActionDB()
        if actionObj.validateSalesBike(salesbikeid):
            return render(
                request,
                "clientapp/sales-bike-detail.html",
                {
                    "payload": actionObj.getSalesBikeData1(
                        get_session_userid(request), salesbikeid
                    ),
                    "recomended": actionObj.getRecomSalesBikeData(),
                },
            )
        else:
            return render(
                request,
                "clientapp/sales.html",
                {
                    "payload": actionObj.getSalesBikeData(),
                    "recomended": actionObj.getRecomSalesBikeData(),
                    "states": actionObj.getStateData(),
                },
            )
    else:
        return render(request, "clientapp/login.html")


def showServiceHistory(request):
    if get_session_userid(request):
        actionObj = BasicClientActionDB()
        return render(
            request,
            "clientapp/service-history.html",
            {"payload": actionObj.getUserServiceData(get_session_userid(request))},
        )
    else:
        return render(request, "clientapp/login.html")


def showPurchaseHistory(request):
    if get_session_userid(request):
        actionObj = BasicClientActionDB()
        return render(
            request,
            "clientapp/purchase-history.html",
            {"payload": actionObj.getUserPurchaseData(get_session_userid(request))},
        )
    else:
        return render(request, "clientapp/login.html")


def login(request):
    return render(request, "clientapp/login.html")


def showPurchaseDetails(request, purchaseid):
    if get_session_userid(request):
        actionObj = BasicClientActionDB()
        actionObj1 = BasicClientHelperCls()
        if actionObj1.validatePurchaseID(purchaseid):
            return render(
                request,
                "clientapp/purchase-details.html",
                {
                    "payload": actionObj.getPurchaseDetailsData(purchaseid),
                    "purchaseid": purchaseid,
                },
            )
        else:
            return render(
                request,
                "clientapp/purchase-history.html",
                {"payload": actionObj.getUserPurchaseData(get_session_userid(request))},
            )
    else:
        return render(request, "clientapp/login.html")


def showBookService(request, serviceid):
    if get_session_userid(request):
        actionObj = BasicClientActionDB()
        actionObj1 = BasicClientHelperCls()
        if actionObj1.validateServiceID(serviceid):
            return render(
                request,
                "clientapp/bookservice.html",
                {"bike_data": actionObj.getBikeBrandData(), "serviceid": serviceid},
            )
        else:
            return render(
                request,
                "clientapp/service.html",
                {
                    "payload": actionObj.getServiceCenterData(),
                    "recomended": actionObj.getRecomServiceCenterData(),
                    "states": actionObj.getStateData(),
                },
            )
    else:
        return render(request, "clientapp/login.html")


def about(request):
    return render(request, "clientapp/about.html")


def showContact(request):
    return render(request, "clientapp/contact.html")


def contact(request):
    return render(request, "clientapp/contact.html")


def showOneServiceProduct(request, serviceid):
    if get_session_userid(request):
        actionObj = BasicClientActionDB()
        return render(
            request,
            "clientapp/view-service.html",
            {
                "payload": actionObj.getParticularServiceData(serviceid),
                "recomended": actionObj.getRecomServiceCenterData(),
            },
        )
    else:
        return render(request, "clientapp/login.html")


def services(request):
    if get_session_userid(request):
        actionObj = BasicClientActionDB()
        return render(
            request,
            "clientapp/service.html",
            {
                "payload": actionObj.getServiceCenterData(),
                "recomended": actionObj.getRecomServiceCenterData(),
                "states": actionObj.getStateData(),
            },
        )
    else:
        return render(request, "clientapp/login.html")


def showPurchaseForm(request, salesbikeid):
    if get_session_userid(request):
        actionObj = BasicClientActionDB()
        if actionObj.validateSalesBike(salesbikeid):
            return render(
                request,
                "clientapp/purcahse-form.html",
                {
                    "payload": actionObj.getSalesBikeData1(
                        get_session_userid(request), salesbikeid
                    )
                },
            )
        else:
            return render(
                request,
                "clientapp/sales.html",
                {
                    "payload": actionObj.getSalesBikeData(),
                    "recomended": actionObj.getRecomSalesBikeData(),
                    "states": actionObj.getStateData(),
                },
            )
    else:
        return render(request, "clientapp/login.html")


def showSales(request):
    if get_session_userid(request):
        actionObj = BasicClientActionDB()
        return render(
            request,
            "clientapp/sales.html",
            {
                "payload": actionObj.getSalesBikeData(),
                "recomended": actionObj.getRecomSalesBikeData(),
                "states": actionObj.getStateData(),
            },
        )
    else:
        return render(request, "clientapp/login.html")


def team(request):
    return render(request, "clientapp/team.html")


def testimonial(request):
    return render(request, "clientapp/testimonial.html")


def userRegister(request):
    actionObj = BasicClientActionDB()
    return render(
        request, "clientapp/register.html", {"state_data": actionObj.getStateData()}
    )


def logout(request):
    request.session.clear()
    return render(request, "clientapp/login.html")


def showPaymentPage(request, orderid):
    if get_session_userid(request):
        actionObj = BasicClientActionDB()
        if actionObj.getPaymentSessionData(request):
            return render(
                request,
                "clientapp/payment-page.html",
                {
                    "payload": actionObj.getPaymentSessionData(request),
                    "orderid": orderid,
                },
            )
        else:
            return render(
                request,
                "clientapp/sales.html",
                {
                    "payload": actionObj.getSalesBikeData(),
                    "recomended": actionObj.getRecomSalesBikeData(),
                    "states": actionObj.getStateData(),
                },
            )
    else:
        return render(request, "clientapp/login.html")


# basic api logic


def mangaeApi(request):
    actionObj = BasicClientActionDB()
    if request.method == "POST":
        if int(request.POST["action"]) == 1:
            # if request for client registration
            return HttpResponse(actionObj.createUserfnc(request.POST))
        elif int(request.POST["action"]) == 2:
            return HttpResponse(actionObj.validateUserLogin(request.POST, request))
        elif int(request.POST["action"]) == 16:
            return HttpResponse(actionObj.submitContactForm(request.POST, request))
        elif int(request.POST["action"]) == 18:
            return HttpResponse(actionObj.sendResetMail(request.POST, request))
        elif int(request.POST["action"]) == 19:
            return HttpResponse(actionObj.updateUserForgotPass(request.POST, request))
        else:
            if get_session_userid(request):
                if int(request.POST["action"]) == 3:
                    stateID = request.POST["stateID"]
                    return HttpResponse(actionObj.getCityData(stateID))
                elif int(request.POST["action"]) == 4:
                    keyword = request.POST["keyword"]
                    return HttpResponse(actionObj.getSearchServiceData(keyword))
                elif int(request.POST["action"]) == 5:
                    cityID = request.POST["cityID"]
                    return HttpResponse(actionObj.getServiceDataByCity(cityID))
                elif int(request.POST["action"]) == 6:
                    return HttpResponse(
                        actionObj.updateProfile(
                            request.POST, get_session_userid(request)
                        )
                    )
                elif int(request.POST["action"]) == 7:
                    return HttpResponse(
                        actionObj.updatePasswrod(
                            request.POST, get_session_userid(request)
                        )
                    )
                elif int(request.POST["action"]) == 8:
                    return HttpResponse(
                        actionObj.generateServiceBook(
                            request.POST, request.FILES, get_session_userid(request)
                        )
                    )
                elif int(request.POST["action"]) == 9:
                    status = request.POST["userStatus"]
                    serviceBookid = request.POST["serviceBookid"]
                    if actionObj.validateServiceBook(serviceBookid):
                        return HttpResponse(
                            actionObj.cancellServiceBooking(
                                serviceBookid, status, get_session_userid(request)
                            )
                        )
                    else:
                        return HttpResponse(
                            return_data_pop(
                                0,
                                "Unauthorized requests. invalid service booking id",
                                0.1,
                            )
                        )
                elif int(request.POST["action"]) == 10:
                    cityID = request.POST["cityID"]
                    return HttpResponse(actionObj.getBikeSalesDataByCity(cityID))
                elif int(request.POST["action"]) == 11:
                    keyword = request.POST["keyword"]
                    return HttpResponse(actionObj.getSearchSalesBikeData(keyword))
                elif int(request.POST["action"]) == 12:
                    return HttpResponse(
                        actionObj.bikePurchaseInvoke(
                            request.POST,
                            request.FILES,
                            get_session_userid(request),
                            request,
                        )
                    )
                elif int(request.POST["action"]) == 13:
                    return HttpResponse(
                        actionObj.verifyPayment(
                            request.POST, get_session_userid(request), request
                        )
                    )
                elif int(request.POST["action"]) == 14:
                    status = request.POST["userStatus"]
                    purchase_id = request.POST["serviceBookid"]
                    if actionObj.validatePurchaseBook(purchase_id):
                        return HttpResponse(
                            actionObj.cancellBikeBooking(
                                purchase_id, status, get_session_userid(request)
                            )
                        )
                    else:
                        return HttpResponse(
                            return_data_pop(
                                0,
                                "Unauthorized requests. invalid service booking id",
                                0.1,
                            )
                        )
                elif int(request.POST["action"]) == 15:
                    return HttpResponse(
                        actionObj.submitFeedback(
                            request.POST, get_session_userid(request)
                        )
                    )
                elif int(request.POST["action"]) == 17:
                    return HttpResponse(
                        actionObj.verifyPayment1(
                            request.POST, get_session_userid(request), request
                        )
                    )

                else:
                    return HttpResponse(
                        return_data_pop(0, "Unauthorized requests", 0.1)
                    )
            else:
                return HttpResponse(return_data_pop(0, "Please login first.", 0.1))
    else:
        return HttpResponse(return_data_pop(0, "Unauthorized requests", 0.0))


def return_data_pop(status, msg, error_code):
    return_data = {"status": status, "msg": msg, "error_code": error_code}
    return json.dumps(return_data)


def get_session_userid(request):
    if (
        request.session.get("is_logged") == True
        and request.session.get("data")["type"] == 0
    ):
        return str(request.session.get("data")["user_id"])
    else:
        return False


def showFeedback(request, serviceid):
    if get_session_userid(request):
        actionObj = BasicClientActionDB()
        actionObj1 = BasicClientHelperCls()
        if actionObj1.validateServiceBookID(serviceid):
            return render(
                request,
                "clientapp/feedback.html",
                {"payload": actionObj1.validateServiceBookID(serviceid)},
            )
        else:
            return render(
                request,
                "clientapp/service-history.html",
                {
                    "payload": actionObj.getServiceCenterData(),
                    "recomended": actionObj.getRecomServiceCenterData(),
                    "states": actionObj.getStateData(),
                },
            )
    else:
        return render(request, "clientapp/login.html")


def showPayServiceFee(request, serviceid):
    if get_session_userid(request):
        actionObj = BasicClientActionDB()
        actionObj1 = BasicClientHelperCls()
        if actionObj1.validateServiceBookID(serviceid):
            return render(
                request,
                "clientapp/payment-page1.html",
                {
                    "payload": actionObj.createServicePaymentRequest(
                        serviceid, get_session_userid(request), request
                    )
                },
            )
        else:
            return render(
                request,
                "clientapp/service-history.html",
                {
                    "payload": actionObj.getServiceCenterData(),
                    "recomended": actionObj.getRecomServiceCenterData(),
                    "states": actionObj.getStateData(),
                },
            )
    else:
        return render(request, "clientapp/login.html")
