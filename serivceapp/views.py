from django.shortcuts import render, HttpResponse
from . models import BasicServiceCenterActionDB,ServiceHelperCls
import json
# Create your views here.

# normail template return


def adminHome(request):
    if (request.session.get('is_logged') == True):
        return render(request, 'serivceapp/index.html', context={'request': request})
    else:
        return render(request, 'serivceapp/login.html')


def login(request):
    return render(request, 'serivceapp/login.html')

def showForgotpassPage(request):
    return render(request, 'serivceapp/forgot-password.html')

def showResetPassPage(request,otpstring,userid):
    actionObj = ServiceHelperCls()
    if(actionObj.validateResetPassRequest(otpstring,userid)):
        return render(request,'serivceapp/reset-password.html',{'payload':actionObj.validateResetPassRequest(otpstring,userid)})
    else:
        return render(request,'serivceapp/forgot-password.html')
def register(request):
    actionObj = BasicServiceCenterActionDB()
    return render(request, 'serivceapp/register.html', {'state_data': actionObj.getStateData()})





def logout(request):
    request.session.clear()
    return render(request, 'serivceapp/login.html')


def addService(request):
    if (request.session.get('is_logged') == True):
        return render(request, 'serivceapp/add-service.html')
    else:
        return render(request, 'serivceapp/login.html')

def getStateData(self):
        self.dbConn.execute(
            "SELECT `states`.`id`,`states`.`name` FROM `states`")
        return self.dbConn.fetchall

def getCityData(self, state_id):
    self.dbConn.execute(
            "SELECT `id`, `city` FROM `cities` WHERE `cities`.`state_id` = '"+state_id+"'")
    result = self.dbConn.fetchall()
    if not result:
        return self.return_data_pop(0, 'Error: No results found', 0.1)
    else:
        return json.dumps({'status': 1, 'data': result})

def viewServices(request):
    if (request.session.get('is_logged') == True):
        actionObj = BasicServiceCenterActionDB()
        return render(request, 'serivceapp/view-service-booking.html',{'service_data': actionObj.getServiceListData()})
    else:
        return render(request, 'serivceapp/login.html')
    
# service api logic

def editServicesget(request,service_id):
    if (request.session.get('is_logged') == True):
        actionObj = BasicServiceCenterActionDB()
        if(actionObj.getvalidateServiceData(service_id)):
            return render(request, 'serivceapp/edit-service.html',{'payload':actionObj.getvalidateServiceData(service_id)})
        else:
            return render(request, 'serivceapp/service_lists.html',{'service_data': actionObj.getServiceListData()})
    else:
        return render(request, 'serivceapp/login.html')
    

def addNewBikes(request):
    if (request.session.get('is_logged') == True):
        actionObj = BasicServiceCenterActionDB()
        return render(request, 'serivceapp/add-new-bikes.html',{'brand_data':actionObj.getBikeBrandData()})
    else:
        return render(request, 'serivceapp/login.html')
    
def addBikeBrand(request):
    if (request.session.get('is_logged') == True):
        actionObj = BasicServiceCenterActionDB()
        return render(request, 'serivceapp/add-bike-brand.html',{'brand_data':actionObj.getBikeBrandData()})
    else:
        return render(request, 'serivceapp/login.html')
    
def viewBikes(request):
    if (request.session.get('is_logged') == True):
        actionObj = BasicServiceCenterActionDB()
        return render(request, 'serivceapp/sales-bike-list.html',{'bike_data':actionObj.getSalesBikeData()})
    else:
        return render(request, 'serivceapp/login.html')

def editSalesBikeget(request,bike_id):
    if (request.session.get('is_logged') == True):
        actionObj = BasicServiceCenterActionDB()
        if(actionObj.getvalidateBikeData(bike_id)):
            return render(request, 'serivceapp/edit-sales-bike.html',{'payload':actionObj.getvalidateBikeData(bike_id),'brand_data':actionObj.getBikeBrandData()})
        else:
            return render(request, 'serivceapp/sales-bike-list.html',{'bike_data':actionObj.getSalesBikeData()})
    else:
        return render(request, 'serivceapp/login.html')
    
def editSalesBikeImageget(request,bike_id):
    if (request.session.get('is_logged') == True):
        actionObj = BasicServiceCenterActionDB()
        if(actionObj.getvalidateBikeData(bike_id)):
            return render(request, 'serivceapp/edit-sales-bikeimg.html',{'payload':actionObj.getvalidateBikeImgData(bike_id),'bike_id':bike_id})
        else:
            return render(request, 'serivceapp/sales-bike-list.html',{'bike_data':actionObj.getSalesBikeData()})
    else:
        return render(request, 'serivceapp/login.html')
    
def updatePassword(request):
    if (request.session.get('is_logged') == True):
        return render(request, 'serivceapp/update-password.html')
    else:
        return render(request, 'serivceapp/login.html')
    
def updateProfile(request):
    if (request.session.get('is_logged') == True):
        actionObj = BasicServiceCenterActionDB()
        return render(request, 'serivceapp/update-profile.html',{'payload':actionObj.getCurrentUserData(get_session_userid(request))})
    else:
        return render(request, 'serivceapp/login.html')
    
def mangaeApi(request):
    # currently not checking the session exist for each api request. if want use get_session_data()
    if (request.method == 'POST'):
        actionObj = BasicServiceCenterActionDB()
        if (int(request.POST['action']) == 4):
            # if request for client registration
            return HttpResponse(actionObj.createServiceCenterfnc(request.POST, request.FILES))
        elif (int(request.POST['action']) == 2):
            # request passe for current global session acess
            return HttpResponse(actionObj.validateUserLogin(request.POST, request))
        elif (int(request.POST['action']) == 3):
            state_id = request.POST['state_id']
            return HttpResponse(actionObj.getCityData(state_id))
        elif (int(request.POST['action']) == 1):
            return HttpResponse(actionObj.addNewService(request.POST, request.FILES, get_session_userid(request)))
        elif (int(request.POST['action']) == 5 or int(request.POST['action']) == 6):
            return HttpResponse(actionObj.updateServiceData(request.POST, request.FILES, get_session_userid(request)))
        elif (int(request.POST['action']) == 7):
            service_id = request.POST['service_id']
            return HttpResponse(actionObj.enableDisableService(service_id,get_session_userid(request)))
        elif (int(request.POST['action']) == 8):
            service_id = request.POST['service_id']
            return HttpResponse(actionObj.removeService(service_id,get_session_userid(request)))
        elif (int(request.POST['action']) == 9):
            brandName = request.POST['brandName']
            return HttpResponse(actionObj.addBrandData(brandName,get_session_userid(request)))
        elif (int(request.POST['action']) == 10):
            brand_id = request.POST['brand_id']
            action_type = request.POST['type']
            return HttpResponse(actionObj.enableDisableDeleteBrand(brand_id,action_type,get_session_userid(request)))
        elif (int(request.POST['action']) == 11):
            editBrandName = request.POST['editBrandName']
            editBrandID = request.POST['editBrandID']
            return HttpResponse(actionObj.updateBrandData(editBrandName,editBrandID))
        elif (int(request.POST['action']) == 12):
            return HttpResponse(actionObj.createNewSalesBike(request.POST, request.FILES, get_session_userid(request)))
        elif (int(request.POST['action']) == 13):
            return HttpResponse(actionObj.updateSalesBikeMeta(request.POST,get_session_userid(request)))
        elif (int(request.POST['action']) == 14):
            bikeID = request.POST['bikeID']
            action_type = request.POST['type']
            return HttpResponse(actionObj.enableDisableDeleteSalesBike(bikeID,action_type,get_session_userid(request)))
        elif (int(request.POST['action']) == 15):
            bikeID = request.POST['bike_id']            
            return HttpResponse(actionObj.updateSalesBikeImage(bikeID,request.FILES,get_session_userid(request)))
        elif (int(request.POST['action']) == 16):
            imageID = request.POST['imageID']            
            return HttpResponse(actionObj.removeSalesBikeImage(imageID,get_session_userid(request)))
        elif (int(request.POST['action']) == 17):
            return HttpResponse(actionObj.updatePassword(request.POST,get_session_userid(request)))
        elif (int(request.POST['action']) == 18):
            return HttpResponse(actionObj.updateUserProfile(request.POST, request.FILES, get_session_userid(request),request))
        elif (int(request.POST['action']) == 19):
            return HttpResponse(actionObj.updateServiceBookingData(request.POST, get_session_userid(request)))
        elif (int(request.POST['action']) == 20):
            return HttpResponse(actionObj.updateServiceBookingData1(request.POST, get_session_userid(request)))
        elif (int(request.POST['action']) == 21):
            return HttpResponse(actionObj.updateServiceBookingData2(request.POST, get_session_userid(request)))
        elif (int(request.POST['action']) == 22):
            return HttpResponse(actionObj.updateServiceBookingData3(request.POST, get_session_userid(request)))
        elif (int(request.POST['action']) == 23):
            return HttpResponse(actionObj.updateServiceBookingData4(request.POST, get_session_userid(request)))
        elif (int(request.POST['action']) == 24):
            return HttpResponse(actionObj.updateSalesPruchaseData(request.POST, get_session_userid(request)))
        elif (int(request.POST['action']) == 25):
            return HttpResponse(actionObj.updateSalesPruchaseData1(request.POST, get_session_userid(request)))
        elif (int(request.POST['action']) == 26):
            return HttpResponse(actionObj.updateSalesPruchaseData2(request.POST, get_session_userid(request)))
        elif (int(request.POST['action']) == 27):
            return HttpResponse(actionObj.sendResetMail(request.POST, request))
        elif (int(request.POST['action']) == 28):
            return HttpResponse(actionObj.updateUserForgotPass(request.POST, request))
        else:
            return HttpResponse(return_data_pop(0, 'Unauthorized requests', 0.1))
    else:
        return HttpResponse(return_data_pop(0, 'Unauthorized requests', 0.0))


def return_data_pop(status, msg, error_code):
    return_data = {
        'status': status,
        'msg': msg,
        'error_code': error_code
    }
    return json.dumps(return_data)

def get_session_userid(request):
    if (request.session.get('is_logged') == True):
        return str(request.session.get('data')['user_id'])
    else:
        return False

def showServiceBokkings(request):
    if (request.session.get('is_logged') == True):
        actionObj = BasicServiceCenterActionDB()
        return render(request, 'serivceapp/view-service-booking.html',{'payload':actionObj.getServiceBookingData(get_session_userid(request))})
    else:
        return render(request, 'serivceapp/login.html')
    
def showAcceptedBokkings(request):
    if (request.session.get('is_logged') == True):
        actionObj = BasicServiceCenterActionDB()
        return render(request, 'serivceapp/view-accepted-booking.html',{'payload':actionObj.getServiceBookingData1(get_session_userid(request))})
    else:
        return render(request, 'serivceapp/login.html')
    
def showRejectedBokkings(request):
    if (request.session.get('is_logged') == True):
        actionObj = BasicServiceCenterActionDB()
        return render(request, 'serivceapp/view-rejected-booking.html',{'payload':actionObj.getServiceBookingData2(get_session_userid(request))})
    else:
        return render(request, 'serivceapp/login.html')
    
def showCompletedBokkings(request):
    if (request.session.get('is_logged') == True):
        actionObj = BasicServiceCenterActionDB()
        return render(request, 'serivceapp/view-completed-booking.html',{'payload':actionObj.getServiceBookingData3(get_session_userid(request))})
    else:
        return render(request, 'serivceapp/login.html')
    
def showServiceDetails(request,servicebookid):
    if (request.session.get('is_logged') == True):
        actionObj = BasicServiceCenterActionDB()
        actionObj1 = ServiceHelperCls()
        if(actionObj1.validateServiceBookID(servicebookid)):
            return render(request, 'serivceapp/view-service-details.html',{'payload':actionObj.getServiceDetailsData(servicebookid),'servicebookid':servicebookid})
        else:
            return render(request, 'serivceapp/view-completed-booking.html',{'payload':actionObj.getServiceBookingData3(get_session_userid(request))})
    else:
        return render(request, 'serivceapp/login.html')
    
def showServiceFeedbacks(request):
    if (request.session.get('is_logged') == True):
        actionObj = BasicServiceCenterActionDB()
        return render(request, 'serivceapp/view-service-feedback.html',{'payload':actionObj.getServiceFeedbackData(get_session_userid(request))})
    else:
        return render(request, 'serivceapp/login.html')
    
def showSalesNewBokkings(request):
    if (request.session.get('is_logged') == True):
        actionObj = BasicServiceCenterActionDB()
        return render(request, 'serivceapp/view-sales-new-booking.html',{'payload':actionObj.getBikeSalesData(get_session_userid(request))})
    else:
        return render(request, 'serivceapp/login.html')
    
def showPurchaseDetails(request,purchasebookid):
    if (request.session.get('is_logged') == True):
        actionObj = BasicServiceCenterActionDB()
        actionObj1 = ServiceHelperCls()
        if(actionObj1.validatePurchaseBookID(purchasebookid)):
            return render(request, 'serivceapp/view-purchase-details.html',{'payload':actionObj.getPurchaseDetailData(purchasebookid),'purchasebookid':purchasebookid})
        else:
            return render(request, 'serivceapp/view-sales-new-booking.html',{'payload':actionObj.getBikeSalesData(get_session_userid(request))})
    else:
        return render(request, 'serivceapp/login.html')
    
def showSalesPendingBokkings(request):
    if (request.session.get('is_logged') == True):
        actionObj = BasicServiceCenterActionDB()
        return render(request, 'serivceapp/view-sales-pending-booking.html',{'payload':actionObj.getpurchaseBookingData1(get_session_userid(request))})
    else:
        return render(request, 'serivceapp/login.html')
    
def showSalesCompletedBokkings(request):
    if (request.session.get('is_logged') == True):
        actionObj = BasicServiceCenterActionDB()
        return render(request, 'serivceapp/view-sales-completed-booking.html',{'payload':actionObj.getpurchaseBookingData2(get_session_userid(request))})
    else:
        return render(request, 'serivceapp/login.html')
    
    

def showSalesAnalysis(request):
    if (request.session.get('is_logged') == True):
        actionObj = BasicServiceCenterActionDB()
        return render(request, 'serivceapp/sales-analysis.html',{'payload':actionObj.getpurchaseBookingData2(get_session_userid(request))})
    else:
        return render(request, 'serivceapp/login.html')