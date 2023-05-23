from django.shortcuts import render, HttpResponse
from .models import BasicAdminActionDB, AdminHelperCls
import json


def showUpdateUserPassw(request):
    if get_session_userid(request):
        return render(request, "adminapp/update-passw.html")
    else:
        return render(request, "adminapp/login.html")


def showIndependentBikes(request, bikeid):
    if get_session_userid(request):
        actionObj = BasicAdminActionDB()
        return render(
            request,
            "adminapp/each-sales-view.html",
            {"payload": actionObj.getParticularBikeData(bikeid)},
        )
    else:
        return render(request, "adminapp/login.html")


def showSuperUsers(request):
    if get_session_userid(request):
        actionObj = BasicAdminActionDB()
        return render(
            request,
            "adminapp/view-superusers.html",
            {"payload": actionObj.getSuperUserData()},
        )
    else:
        return render(request, "adminapp/login.html")


def showIndependentServices(request, serviceid):
    if get_session_userid(request):
        actionObj = BasicAdminActionDB()
        return render(
            request,
            "adminapp/each-service-view.html",
            {"payload": actionObj.getPraticularServiceData(serviceid)},
        )
    else:
        return render(request, "adminapp/login.html")


# Create your views here.
def adminHome(request):
    if get_session_userid(request):
        actionObj = BasicAdminActionDB()
        return render(request, "adminapp/index.html")
    else:
        return render(request, "adminapp/login.html")


def showFeedbackhistory(request):
    if get_session_userid(request):
        actionObj = BasicAdminActionDB()
        return render(
            request,
            "adminapp/view-feedbacks.html",
            {"payload": actionObj.getServiceFeedbackData(get_session_userid(request))},
        )
    else:
        return render(request, "adminapp/login.html")


def showServiceCenters(request):
    if get_session_userid(request):
        actionObj = BasicAdminActionDB()
        return render(
            request,
            "adminapp/view-service-centers.html",
            {"payload": actionObj.getServiceCenterData()},
        )
    else:
        return render(request, "adminapp/login.html")


def logout(request):
    request.session.clear()
    return render(request, "adminapp/login.html")


def addBikeBrand(request):
    if get_session_userid(request):
        actionObj = BasicAdminActionDB()
        return render(
            request,
            "adminapp/add-bike-brand.html",
            {"brand_data": actionObj.getBikeBrandData()},
        )
    else:
        return render(request, "adminapp/login.html")


def showUsersList(request):
    if get_session_userid(request):
        actionObj = BasicAdminActionDB()
        return render(
            request, "adminapp/view-users.html", {"payload": actionObj.getUserData()}
        )
    else:
        return render(request, "adminapp/login.html")


def login(request):
    if get_session_userid(request):
        return render(request, "adminapp/index.html")
    else:
        return render(request, "adminapp/login.html")


def register(request):
    if get_session_userid(request):
        return render(request, "adminapp/index.html")
    else:
        return render(request, "adminapp/register.html")


def forgotPassword(request):
    if get_session_userid(request):
        return render(request, "adminapp/index.html")
    else:
        return render(request, "adminapp/forgot-password.html")


def showResetPassPage(request, otpstring, userid):
    actionObj = AdminHelperCls()
    if actionObj.validateResetPassRequest(otpstring, userid):
        return render(
            request,
            "adminapp/reset-password.html",
            {"payload": actionObj.validateResetPassRequest(otpstring, userid)},
        )
    else:
        return render(request, "adminapp/forgot-password.html")


def apiAdminActions(request):
    actionObj = BasicAdminActionDB()
    if request.method == "POST":
        if int(request.POST["action"]) == 1:
            # if request for admin registration
            return HttpResponse(actionObj.createUserfnc(request.POST))
        elif int(request.POST["action"]) == 2:
            return HttpResponse(actionObj.validateUserLogin(request.POST, request))
        elif int(request.POST["action"]) == 27:
            return HttpResponse(actionObj.sendResetMail(request.POST, request))
        elif int(request.POST["action"]) == 28:
            return HttpResponse(actionObj.updateUserForgotPass(request.POST, request))
        else:
            if get_session_userid:
                if int(request.POST["action"]) == 29:
                    return HttpResponse(actionObj.getNotifications(request))
                elif int(request.POST["action"]) == 3:
                    return HttpResponse(actionObj.enableDisableCenters(request.POST))
                elif int(request.POST["action"]) == 4:
                    return HttpResponse(actionObj.enableDisableUsers(request.POST))

                elif int(request.POST["action"]) == 5:
                    return HttpResponse(
                        actionObj.updateUserPass(
                            request.POST, get_session_userid(request)
                        )
                    )
                elif int(request.POST["action"]) == 30:
                    return HttpResponse(actionObj.activateSerivceCenter(request.POST))
                elif int(request.POST["action"]) == 6:
                    return HttpResponse(actionObj.verifyNewAdminUsers(request.POST))
                elif int(request.POST["action"]) == 7:
                    return HttpResponse(actionObj.enableDisableAdmins(request.POST))
                elif int(request.POST["action"]) == 31:
                    return HttpResponse(
                        actionObj.rejectDeleteSerivceCenter(request.POST)
                    )
                else:
                    return HttpResponse(
                        return_data_pop(0, "Unauthorized requests", 2.0)
                    )
            else:
                return HttpResponse(return_data_pop(0, "Unauthorized requests", 2.0))
    else:
        return HttpResponse(return_data_pop(0, "Unauthorized requests", 0.0))


def return_data_pop(status, msg, error_code):
    return_data = {"status": status, "msg": msg, "error_code": error_code}
    return json.dumps(return_data)


def get_session_userid(request):
    if (
        request.session.get("is_logged") == True
        and request.session.get("data")["type"] == 2
    ):
        return str(request.session.get("data")["user_id"])
    else:
        return False
