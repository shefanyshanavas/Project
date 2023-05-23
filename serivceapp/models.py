from django.db import models, connection
import hashlib
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import emoji
from textblob import TextBlob
import random
import string

# Create your models here.


class ServiceHelperCls:
    def __init__(self) -> None:
        self.dbConn = connection.cursor()

    def __del__(self):
        # closing the cursor by destroyer
        self.dbConn.close()

    def validateResetPassRequest(self, otp, userid):
        self.dbConn.execute(
            "SELECT * FROM `reset_pass_tbl` WHERE `reset_pass_tbl`.`reset_id` = '"
            + userid
            + "' AND `reset_pass_tbl`.`code` = '"
            + otp
            + "' AND `reset_pass_tbl`.`status` = 1"
        )
        data = self.dbConn.fetchone()
        if not data:
            return False
        else:
            return data

    def validateBrandID(self, brandID):
        self.dbConn.execute(
            "SELECT * FROM `bike_brand_tbl` WHERE `bike_brand_tbl`.`brand_id` = '"
            + brandID
            + "'"
        )
        data = self.dbConn.fetchone()
        if not data:
            return False
        else:
            return data

    def validateServiceCenterUser(self, userid):
        self.dbConn.execute(
            "SELECT * FROM `service_center_table` WHERE `service_center_table`.`service_center_id` = '"
            + userid
            + "'"
        )
        if not self.dbConn.fetchone():
            return False
        else:
            return True

    def validateBrandName(self, brandName):
        self.dbConn.execute(
            "SELECT * FROM `bike_brand_tbl` WHERE `bike_brand_tbl`.`brand_name` = '"
            + brandName
            + "'"
        )
        if not self.dbConn.fetchone():
            return True
        else:
            return False

    def validateServiceNameExist(self, serviceName):
        self.dbConn.execute(
            "SELECT * FROM `service_list_tbl` WHERE `service_list_tbl`.`service_name` = '"
            + serviceName
            + "'"
        )
        if not self.dbConn.fetchone():
            return True
        else:
            return False

    def validateSalesBikeName(self, bikeName):
        self.dbConn.execute(
            "SELECT * FROM `sales_bike_tbl` WHERE `sales_bike_tbl`.`bike_name` = '"
            + bikeName
            + "'"
        )
        if not self.dbConn.fetchone():
            return True
        else:
            return False

    def handle_uploaded_files(self, f):
        with open(f"static/image/service_centers/{f.name}", "wb+") as destination:
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
        return True

    def handle_uploaded_files1(self, f):
        with open(f"static/image/service_list_image/{f.name}", "wb+") as destination:
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
        return True

    def handle_uploaded_files2(self, f):
        with open(f"static/image/sales_bikes/{f.name}", "wb+") as destination:
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
        return True

    def isUserExistByPass(self, passw, userID):
        self.dbConn.execute(
            "SELECT * FROM `service_center_table` WHERE `service_center_table`.`service_center_id` = '"
            + userID
            + "' AND `service_center_table`.`passw` = '"
            + passw
            + "'"
        )
        if not self.dbConn.fetchone():
            return False
        else:
            return True

    def validateServiceBookID(self, bookid):
        self.dbConn.execute(
            "SELECT * FROM `service_book_tbl` WHERE `service_book_tbl`.`service_book_id` = '"
            + bookid
            + "'"
        )
        if not self.dbConn.fetchone():
            return False
        else:
            return True

    def validatePurchaseBookID(self, bookid):
        self.dbConn.execute(
            "SELECT * FROM `bike_purchase_tbl` WHERE `bike_purchase_tbl`.`purchase_id`  = '"
            + bookid
            + "'"
        )
        if not self.dbConn.fetchone():
            return False
        else:
            return True


class BasicServiceCenterActionDB(ServiceHelperCls):
    UPLOAD_FOLDER = os.getcwd() + "static/image/service_centers/"
    ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "pdf"])

    def __init__(self) -> None:
        super().__init__()
        self.dbConn = connection.cursor()

    # user account registration logic

    def getStateData(self):
        self.dbConn.execute(
            "SELECT `states`.`id`,`states`.`name` FROM `states`")
        return self.dbConn.fetchall

    def getCityData(self, state_id):
        self.dbConn.execute(
            "SELECT `id`, `city` FROM `cities` WHERE `cities`.`state_id` = '"
            + state_id
            + "'"
        )
        result = self.dbConn.fetchall()
        if not result:
            return self.return_data_pop(0, "Error: No results found", 0.1)
        else:
            return json.dumps({"status": 1, "data": result})

    def getServiceListData(self):
        self.dbConn.execute("SELECT * FROM `service_list_tbl`")
        return self.dbConn.fetchall()

    def getvalidateServiceData(self, serviceID):
        self.dbConn.execute(
            "SELECT * FROM `service_list_tbl` WHERE `service_list_tbl`.`service_id` = '"
            + serviceID
            + "'"
        )
        data = self.dbConn.fetchone()
        if not data:
            return False
        else:
            return data

    def getSalesBikeData(self):
        self.dbConn.execute(
            "SELECT `sales_bike_tbl`.`bike_id`,`sales_bike_tbl`.`bike_name`,`sales_bike_tbl`.`min_advance`,`sales_bike_tbl`.`price`,`sales_bike_tbl`.`stock`,`sales_bike_tbl`.`descr`,`sales_bike_tbl`.`created_at`,`sales_bike_tbl`.`status`,`bike_brand_tbl`.`brand_name` FROM `sales_bike_tbl` INNER JOIN `bike_brand_tbl` ON `sales_bike_tbl`.`brand_id` = `bike_brand_tbl`.`brand_id`;"
        )
        data = self.dbConn.fetchall()
        if not data:
            return False
        else:
            # return data
            data = list(data)
            newdata = []
            for key in data:
                key = list(key)
                self.dbConn.execute(
                    "SELECT * FROM `sales_bike_img_tbl` WHERE `sales_bike_img_tbl`.`sales_bike_id` = '"
                    + str(key[0])
                    + "'"
                )
                image_data = self.dbConn.fetchall()
                key.append(image_data)
                newdata.append(key)
            return newdata

    def getvalidateBikeData(self, bikeID):
        self.dbConn.execute(
            "SELECT * FROM `sales_bike_tbl` WHERE `sales_bike_tbl`.`bike_id` = '"
            + bikeID
            + "'"
        )
        data = self.dbConn.fetchone()
        if not data:
            return False
        else:
            return data

    def getvalidateBikeImgData(self, bikeID):
        self.dbConn.execute(
            "SELECT * FROM `sales_bike_img_tbl` WHERE `sales_bike_img_tbl`.`sales_bike_id` = '"
            + bikeID
            + "'"
        )
        data = self.dbConn.fetchall()
        if not data:
            return False
        else:
            return data

    def getvalidateBikeImgDataByID(self, imageID):
        self.dbConn.execute(
            "SELECT * FROM `sales_bike_img_tbl` WHERE `sales_bike_img_tbl`.`image_id` = '"
            + imageID
            + "'"
        )
        data = self.dbConn.fetchall()
        if not data:
            return False
        else:
            return data

    def getCurrentUserData(self, userID):
        self.dbConn.execute(
            "SELECT * FROM `service_center_table` WHERE `service_center_table`.`service_center_id` = '"
            + userID
            + "'"
        )
        data = self.dbConn.fetchone()
        if not data:
            return False
        else:
            return data

    def getServiceBookingData(self, userID):
        self.dbConn.execute(
            "SELECT `service_book_tbl`.`service_book_id`,`user_tbl`.`fullname`,`user_tbl`.`email`,`user_tbl`.`phone`,`user_tbl`.`address`,`service_book_tbl`.`complaints`,`service_book_tbl`.`bike_model`,`service_book_tbl`.`number_plate`,`service_book_tbl`.`alternate_phone`,`service_book_tbl`.`pickup_mode`,`service_book_tbl`.`created_at`,`service_book_tbl`.`estimate_delivery`,`service_book_tbl`.`bill_status`,`service_book_tbl`.`status` FROM `service_book_tbl` INNER JOIN `user_tbl` ON `service_book_tbl`.`user_id` = `user_tbl`.`user_id` WHERE `service_book_tbl`.`service_id` in (SELECT `service_list_tbl`.`service_id` FROM `service_list_tbl` WHERE `service_list_tbl`.`ser_center_id` = '"
            + userID
            + "' AND `service_book_tbl`.`status` = 0);"
        )
        data = self.dbConn.fetchall()
        if not data:
            return False
        else:
            return data

    def getServiceBookingData1(self, userID):
        self.dbConn.execute(
            "SELECT `service_book_tbl`.`service_book_id`,`user_tbl`.`fullname`,`user_tbl`.`email`,`user_tbl`.`phone`,`user_tbl`.`address`,`service_book_tbl`.`complaints`,`service_book_tbl`.`bike_model`,`service_book_tbl`.`number_plate`,`service_book_tbl`.`alternate_phone`,`service_book_tbl`.`pickup_mode`,`service_book_tbl`.`created_at`,`service_book_tbl`.`estimate_delivery`,`service_book_tbl`.`bill_status`,`service_book_tbl`.`status` FROM `service_book_tbl` INNER JOIN `user_tbl` ON `service_book_tbl`.`user_id` = `user_tbl`.`user_id` WHERE `service_book_tbl`.`service_id` in (SELECT `service_list_tbl`.`service_id` FROM `service_list_tbl` WHERE `service_list_tbl`.`ser_center_id` = '"
            + userID
            + "' AND `service_book_tbl`.`status` IN (1,2,3));"
        )
        data = self.dbConn.fetchall()
        if not data:
            return False
        else:
            return data

    def getServiceBookingData2(self, userID):
        self.dbConn.execute(
            "SELECT `service_book_tbl`.`service_book_id`,`user_tbl`.`fullname`,`user_tbl`.`email`,`user_tbl`.`phone`,`user_tbl`.`address`,`service_book_tbl`.`complaints`,`service_book_tbl`.`bike_model`,`service_book_tbl`.`number_plate`,`service_book_tbl`.`alternate_phone`,`service_book_tbl`.`pickup_mode`,`service_book_tbl`.`created_at`,`service_book_tbl`.`estimate_delivery`,`service_book_tbl`.`bill_status`,`service_book_tbl`.`status` FROM `service_book_tbl` INNER JOIN `user_tbl` ON `service_book_tbl`.`user_id` = `user_tbl`.`user_id` WHERE `service_book_tbl`.`service_id` in (SELECT `service_list_tbl`.`service_id` FROM `service_list_tbl` WHERE `service_list_tbl`.`ser_center_id` = '"
            + userID
            + "' AND `service_book_tbl`.`status` IN (5,6));"
        )
        data = self.dbConn.fetchall()
        if not data:
            return False
        else:
            return data

    def getServiceBookingData3(self, userID):
        self.dbConn.execute(
            "SELECT `service_book_tbl`.`service_book_id`,`user_tbl`.`fullname`,`user_tbl`.`email`,`user_tbl`.`phone`,`user_tbl`.`address`,`service_book_tbl`.`complaints`,`service_book_tbl`.`bike_model`,`service_book_tbl`.`number_plate`,`service_book_tbl`.`alternate_phone`,`service_book_tbl`.`pickup_mode`,`service_book_tbl`.`created_at`,`service_book_tbl`.`estimate_delivery`,`service_book_tbl`.`bill_status`,`service_book_tbl`.`status` FROM `service_book_tbl` INNER JOIN `user_tbl` ON `service_book_tbl`.`user_id` = `user_tbl`.`user_id` WHERE `service_book_tbl`.`service_id` in (SELECT `service_list_tbl`.`service_id` FROM `service_list_tbl` WHERE `service_list_tbl`.`ser_center_id` = '"
            + userID
            + "' AND `service_book_tbl`.`status` = 4);"
        )
        data = self.dbConn.fetchall()
        if not data:
            return False
        else:
            return data

    def updateUserProfile(self, data, imageFile, userID, request):
        if (
            self.dbConn.execute(
                "UPDATE `service_center_table` SET `center_name`='"
                + data["centerName"]
                + "',`address`='"
                + data["address"]
                + "',`phone`='"
                + data["phone"]
                + "',`gstin`='"
                + data["gstin"]
                + "' WHERE `service_center_table`.`service_center_id` = '"
                + userID
                + "'"
            )
            == 1
        ):
            if int(data["type"]) == 1:
                image = imageFile.get("file")
                if bool(image) == True:
                    if self.allowed_file(image.name):
                        path = (
                            "static/image/service_centers/"
                            + self.getCurrentUserData(userID)[7]
                        )
                        if os.path.exists(path):
                            os.remove(path)
                        path = "static/image/service_centers/" + image.name
                        if not os.path.exists(path):
                            self.handle_uploaded_files(image)
                        self.dbConn.execute(
                            "UPDATE `service_center_table` SET `id_proof`='"
                            + image.name
                            + "' WHERE `service_center_table`.`service_center_id` = '"
                            + userID
                            + "'"
                        )
                    else:
                        return self.return_data_pop(
                            0, "Error: File type is not allowed.", 0.1
                        )
                else:
                    return self.return_data_pop(
                        0,
                        "Error : Service image Missing , Please upload a valid image",
                        0.1,
                    )
            self.dbConn.execute(
                "SELECT * FROM `service_center_table` WHERE `service_center_id` = '"
                + userID
                + "'"
            )
            result = self.dbConn.fetchone()
            request.session["data"] = {
                "user_id": result[0],
                "name": result[1],
                "email": result[5],
                "phone": result[4],
                "address": result[3],
                "type": result[10],
                "gstin": result[8],
                "id_proof": result[7],
            }
            return self.return_data_pop(1, "Success : profile updated successfully.", 1)
        else:
            return self.return_data_pop(0, "Error: profile updation failed", 0.2)

    def updatePassword(self, data, userID):
        curr_pass = hashlib.md5(data["curr_pass"].encode()).hexdigest()
        passw = hashlib.md5(data["passw"].encode()).hexdigest()
        confpassw = hashlib.md5(data["confpassw"].encode()).hexdigest()
        if self.isUserExistByPass(curr_pass, userID):
            if (
                self.dbConn.execute(
                    "UPDATE `service_center_table` SET `service_center_table`.`passw` = '"
                    + passw
                    + "' WHERE `service_center_table`.`service_center_id` = '"
                    + userID
                    + "'"
                )
                == 1
            ):
                return self.return_data_pop(
                    1, "Success : New password updated successfully.", 1
                )
            else:
                return self.return_data_pop(0, "Error: password updation failed", 0.2)
        else:
            return self.return_data_pop(0, "Error: Current password wrong.", 0.4)

    def removeSalesBikeImage(self, imageID, userID):
        if self.getvalidateBikeData(imageID):
            if (
                self.dbConn.execute(
                    "DELETE FROM `sales_bike_img_tbl` WHERE `sales_bike_img_tbl`.`image_id` = '"
                    + imageID
                    + "'"
                )
                == 1
            ):
                return self.return_data_pop(1, "Operation Complete successfully.", 1)
            else:
                return self.return_data_pop(0, "Error: Operation failed", 0.2)
        else:
            return self.return_data_pop(0, "Error: Unauthorized request", 0.4)

    def updateSalesBikeImage(self, bikeID, imageFiles, userID):
        if self.getvalidateBikeData(bikeID):
            image = imageFiles.getlist("bike_images")
            for key in image:
                path = "static/image/sales_bikes/" + key.name
                if bool(key) == True:
                    if self.allowed_file(key.name):
                        if not os.path.exists(path):
                            self.handle_uploaded_files2(key)
                        self.dbConn.execute(
                            "INSERT INTO `sales_bike_img_tbl`(`image_name`, `sales_bike_id`, `created_at`, `status`) VALUES ('"
                            + key.name
                            + "','"
                            + bikeID
                            + "',now(),1)"
                        )
            return self.return_data_pop(1, "Success: new Image addedd successfully.", 1)
        else:
            return self.return_data_pop(0, "Error: Unauthorized request", 0.4)

    def enableDisableDeleteSalesBike(self, bikeID, action_type, userID):
        if self.getvalidateBikeData(bikeID):
            if int(action_type) == 0:
                # enableDisable
                status = 1 if self.getvalidateBikeData(bikeID)[9] == 0 else 0
                if (
                    self.dbConn.execute(
                        "UPDATE `sales_bike_tbl` SET `status`='"
                        + str(status)
                        + "' WHERE `sales_bike_tbl`.`bike_id` = '"
                        + bikeID
                        + "'"
                    )
                    == 1
                ):
                    return self.return_data_pop(
                        1, "Operation Complete successfully.", 1
                    )
                else:
                    return self.return_data_pop(0, "Error: Operation failed", 0.2)
            else:
                # delete
                if (
                    self.dbConn.execute(
                        "DELETE FROM `sales_bike_tbl` WHERE `sales_bike_tbl`.`bike_id` = '"
                        + bikeID
                        + "'"
                    )
                    == 1
                ):
                    return self.return_data_pop(1, "Brand removed successfully.", 1)
                else:
                    return self.return_data_pop(0, "Error: Failed to remove brand", 0.2)
        else:
            return self.return_data_pop(0, "Error: Unauthorized request", 0.4)

    def updateSalesBikeMeta(self, data, userID):
        if self.getvalidateBikeData(data["bike_id"]):
            if (
                self.dbConn.execute(
                    "UPDATE `sales_bike_tbl` SET `bike_name`='"
                    + data["bikeName"]
                    + "',`min_advance`='"
                    + data["adv_amt"]
                    + "',`price`='"
                    + data["mrp_price"]
                    + "',`stock`='"
                    + data["stock"]
                    + "',`descr`='"
                    + data["descr"]
                    + "' WHERE `sales_bike_tbl`.`bike_id` = '"
                    + data["bike_id"]
                    + "' AND `sales_bike_tbl`.`ser_center_id` = '"
                    + userID
                    + "'"
                )
                == 1
            ):
                return self.return_data_pop(1, "bike metadata updated successfully", 1)
            else:
                return self.return_data_pop(
                    0, "Error: bike metadata updation failed", 0.2
                )
        else:
            return self.return_data_pop(0, "Error: Unauthorized request, denied", 0.2)

    def createNewSalesBike(self, data, imageFiles, userID):
        if self.validateSalesBikeName(data["bikeName"]):
            if (
                self.dbConn.execute(
                    "INSERT INTO `sales_bike_tbl`(`bike_name`,`brand_id`, `ser_center_id`, `min_advance`, `price`, `stock`, `descr`, `created_at`, `status`) VALUES ('"
                    + data["bikeName"]
                    + "','"
                    + data["brandId"]
                    + "','"
                    + userID
                    + "','"
                    + data["adv_amt"]
                    + "','"
                    + data["mrp_price"]
                    + "','"
                    + data["stock"]
                    + "','"
                    + data["descr"]
                    + "',now(),1)"
                )
                == 1
            ):
                last_insertid = self.dbConn.lastrowid
                image = imageFiles.getlist("bike_images")
                for key in image:
                    path = "static/image/sales_bikes/" + key.name
                    if bool(key) == True:
                        if self.allowed_file(key.name):
                            if not os.path.exists(path):
                                self.handle_uploaded_files2(key)
                            self.dbConn.execute(
                                "INSERT INTO `sales_bike_img_tbl`(`image_name`, `sales_bike_id`, `created_at`, `status`) VALUES ('"
                                + key.name
                                + "','"
                                + str(last_insertid)
                                + "',now(),1)"
                            )
                return self.return_data_pop(
                    1, "Success: new bike addedd successfully.", 1
                )
            else:
                return self.return_data_pop(0, "Error: new bike creation failed", 0.2)
        else:
            return self.return_data_pop(0, "Error: bike name already exist", 0.4)

    def updateBrandData(self, editBrandName, editBrandID):
        if self.validateBrandID(editBrandID):
            if (
                self.dbConn.execute(
                    "UPDATE `bike_brand_tbl` SET `brand_name`='"
                    + editBrandName
                    + "' WHERE `bike_brand_tbl`.`brand_id` = '"
                    + editBrandID
                    + "'"
                )
                == 1
            ):
                return self.return_data_pop(1, "Brand name updated successfully", 1)
            else:
                return self.return_data_pop(0, "Error: Brand name updation failed", 0.2)
        else:
            return self.return_data_pop(
                0,
                "Error: Couldnt find a valid brand id, please provide a valid one",
                0.4,
            )

    def enableDisableDeleteBrand(self, brandID, action_type, userID):
        if self.validateBrandID(brandID):
            if int(action_type) == 0:
                # enableDisable
                status = 1 if self.validateBrandID(brandID)[3] == 0 else 0
                if (
                    self.dbConn.execute(
                        "UPDATE `bike_brand_tbl` SET `status`='"
                        + str(status)
                        + "' WHERE `bike_brand_tbl`.`brand_id` = '"
                        + brandID
                        + "'"
                    )
                    == 1
                ):
                    return self.return_data_pop(
                        1, "Operation Complete successfully.", 1
                    )
                else:
                    return self.return_data_pop(0, "Error: Operation failed", 0.2)
            else:
                # delete
                if (
                    self.dbConn.execute(
                        "DELETE FROM `bike_brand_tbl` WHERE `bike_brand_tbl`.`brand_id` = '"
                        + brandID
                        + "'"
                    )
                    == 1
                ):
                    return self.return_data_pop(1, "Brand removed successfully.", 1)
                else:
                    return self.return_data_pop(0, "Error: Failed to remove brand", 0.2)
        else:
            return self.return_data_pop(0, "Error: Unauthorized request", 0.4)

    def addBrandData(self, brandName, userID):
        if self.validateBrandName(brandName):
            if (
                self.dbConn.execute(
                    "INSERT INTO `bike_brand_tbl`(`brand_name`, `created_at`, `status`) VALUES ('"
                    + brandName
                    + "',now(),1)"
                )
                == 1
            ):
                return self.return_data_pop(1, "Brand name created successfully.", 1)
            else:
                return self.return_data_pop(0, "Error: Brand name creation failed", 0.2)
        else:
            return self.return_data_pop(0, "Error: Brand Name already exist!", 1.0)

    def getBikeBrandData(self):
        self.dbConn.execute("SELECT * FROM `bike_brand_tbl`")
        return self.dbConn.fetchall()

    def removeService(self, serviceID, userID):
        if self.getvalidateServiceData(serviceID) != False:
            path = (
                "static/image/service_list_image/"
                + self.getvalidateServiceData(serviceID)[2]
            )

            if (
                self.dbConn.execute(
                    "DELETE FROM `service_list_tbl` WHERE `service_id`='"
                    + serviceID
                    + "' AND `service_list_tbl`.`ser_center_id` = '"
                    + userID
                    + "'"
                )
                == 1
            ):
                if os.path.exists(path):
                    os.remove(path)
                return self.return_data_pop(1, "Service removed successfully.", 1)
            else:
                return self.return_data_pop(0, "Error: service removal failed", 0.2)
        else:
            return self.return_data_pop(
                0, "Error: request denied. access restricted", 0.4
            )

    def enableDisableService(self, serviceID, userID):
        if self.getvalidateServiceData(serviceID) != False:
            status = 1 if self.getvalidateServiceData(serviceID)[6] == 0 else 0
            if (
                self.dbConn.execute(
                    "UPDATE `service_list_tbl` SET `status`='"
                    + str(status)
                    + "' WHERE `service_id`='"
                    + serviceID
                    + "' AND `service_list_tbl`.`ser_center_id` = '"
                    + userID
                    + "'"
                )
                == 1
            ):
                return self.return_data_pop(1, "Operation completed successfully.", 1)
            else:
                return self.return_data_pop(0, "Error: Operation failed", 0.2)
        else:
            return self.return_data_pop(
                0, "Error: request denied. access restricted", 0.4
            )

    def updateServiceData(self, data, image_file, userid):
        if self.validateServiceCenterUser(userid):
            if self.getvalidateServiceData(data["service_id"]) != False:
                old_data = self.getvalidateServiceData(data["service_id"])
                if int(data["type"]) == 1:
                    image = image_file.get("file")
                    path = "static/image/service_list_image/" + old_data[2]
                    # image upload and update
                    if bool(image) == True:
                        if self.allowed_file(image.name):
                            if os.path.exists(path):
                                os.remove(path)
                            self.handle_uploaded_files1(image)
                            self.dbConn.execute(
                                "UPDATE `service_list_tbl` SET `image_name`='"
                                + image.name
                                + "' WHERE `service_list_tbl`.`service_id` = '"
                                + data["service_id"]
                                + "' AND `service_list_tbl`.`ser_center_id` = '"
                                + userid
                                + "'"
                            )
                        else:
                            return self.return_data_pop(
                                0, "Error: File type is not allowed.", 0.1
                            )
                    else:
                        return self.return_data_pop(
                            0,
                            "Error : Service image Missing , Please upload a valid image",
                            0.1,
                        )
                # normal update
                if (
                    self.dbConn.execute(
                        "UPDATE `service_list_tbl` SET `service_name`='"
                        + data["service_name"]
                        + "',`expected_cost`='"
                        + data["expec_fee"]
                        + "' WHERE `service_list_tbl`.`service_id` = '"
                        + data["service_id"]
                        + "' AND `service_list_tbl`.`ser_center_id` = '"
                        + userid
                        + "'"
                    )
                    == 1
                ):
                    return self.return_data_pop(
                        1, "Service data updated successfully", 1
                    )
                else:
                    return self.return_data_pop(
                        0, "Error: service data updation failed", 0.2
                    )
            else:
                return self.return_data_pop(
                    0, "Error: request denied. access restricted", 0.3
                )
        else:
            return self.return_data_pop(
                0, "Error: request denied. access restricted", 0.2
            )
        # return 0

    def addNewService(self, data, image_file, userid):
        image = image_file.get("file")
        if bool(image) == True:
            if self.allowed_file(image.name):  # checking file type
                service_name = data["service_name"]
                expec_fee = data["expec_fee"]
                descr = data["descr"]
                if self.validateServiceCenterUser(userid):
                    if self.validateServiceNameExist(service_name):
                        if (
                            self.dbConn.execute(
                                "INSERT INTO `service_list_tbl`(`ser_center_id`, `image_name`, `service_name`, `expected_cost`,`descr`, `date`, `status`) VALUES ('"
                                + userid
                                + "','"
                                + image.name
                                + "','"
                                + service_name
                                + "','"
                                + expec_fee
                                + "','"
                                + descr
                                + "',now(),'1')"
                            )
                            == 1
                        ):
                            self.handle_uploaded_files1(image)
                            return self.return_data_pop(
                                1, "New service created successfully", 1
                            )
                        else:
                            return self.return_data_pop(
                                0, "Error: New service creation failed", 0.2
                            )
                    else:
                        return self.return_data_pop(
                            0, "Error: provided service name already exist", 0.3
                        )
                else:
                    return self.return_data_pop(
                        0, "Error: request denied. access restricted", 0.2
                    )
            else:
                return self.return_data_pop(0, "Error: File type is not allowed.", 0.1)
        else:
            return self.return_data_pop(
                0, "Error : Service image Missing , Please upload a valid image", 0.1
            )

    def createServiceCenterfnc(self, data, image_file):
        image = image_file.get("file")
        if bool(image) == True:
            if self.allowed_file(image.name):  # checking file type
                center_name = data["center_name"]
                city = data["city"]
                address = data["address"]
                phone = data["phone"]
                email = data["email"]
                gstin = data["gstin"]
                password = hashlib.md5(data["pass"].encode()).hexdigest()
                self.dbConn.execute(
                    "SELECT * FROM `service_center_table` WHERE `email` = '"
                    + email
                    + "' OR `phone` = '"
                    + phone
                    + "'"
                )
                if not self.dbConn.fetchone():
                    if (
                        self.dbConn.execute(
                            "INSERT INTO `service_center_table`( `center_name`, `city_id`, `address`, `phone`, `email`, `passw`, `id_proof`, `gstin`, `create_date`,`type`, `status`) VALUES ('"
                            + center_name
                            + "','"
                            + city
                            + "','"
                            + address
                            + "','"
                            + phone
                            + "','"
                            + email
                            + "','"
                            + password
                            + "','"
                            + image.name
                            + "','"
                            + gstin
                            + "',now(),1,2)"
                        )
                        == 1
                    ):
                        self.handle_uploaded_files(image)
                        # sendMail()  call this if want to end mail
                        self.sendMail(
                            email,
                            "MotoLogic Account created.",
                            "Please be patient. your account will activated once the admin reviewed your details",
                        )
                        return self.return_data_pop(
                            1, "Account registration completed successfully", 1
                        )
                    else:
                        return self.return_data_pop(
                            0, "Error: Account registration failed", 0.2
                        )
                else:
                    return self.return_data_pop(
                        0, "Error: User already exist, Please login.", 0.1
                    )
            else:
                return self.return_data_pop(0, "Error: File type is not allowed.", 0.1)
        else:
            return self.return_data_pop(
                0, "Error : ID proof Missing , Please upload a valid image", 0.1
            )

    def validateUserLogin(self, data, request):
        password = hashlib.md5(data["password"].encode()).hexdigest()
        email = data["email"]
        self.dbConn.execute(
            "SELECT * FROM `service_center_table` WHERE `email` = '"
            + email
            + "' AND `passw` = '"
            + password
            + "'"
        )
        result = self.dbConn.fetchone()

        if not result:
            return self.return_data_pop(0, "Error: Email id or password error", 0.2)
        else:
            # set session
            if int(result[11]) == 1:
                request.session["is_logged"] = True
                request.session["data"] = {
                    "user_id": result[0],
                    "name": result[1],
                    "email": result[5],
                    "phone": result[4],
                    "address": result[3],
                    "type": result[10],
                    "gstin": result[8],
                    "id_proof": result[7],
                }
                return self.return_data_pop(
                    1, "Loggin completed. you will be redirected to home", 1
                )
            elif int(result[11]) == 2:
                return self.return_data_pop(
                    0, "Account is under review.. it will take some times", 0
                )
            else:
                return self.return_data_pop(
                    0, "Error: Account is deactivated. please contact admin", 0.2
                )

    def allowed_file(self, filename):
        return (
            "." in filename
            and filename.rsplit(".", 1)[1].lower() in self.ALLOWED_EXTENSIONS
        )

    def return_data_pop(self, status, msg, error_code):
        return_data = {"status": status, "msg": msg, "error_code": error_code}
        return json.dumps(return_data)

    def __del__(self):
        # closing the cursor by destroyer
        self.dbConn.close()

    def updateServiceBookingData(self, data, userID):
        # aaccpet service
        if self.validateServiceBookID(data["serviceBookID"]):
            if (
                self.dbConn.execute(
                    "UPDATE `service_book_tbl` SET `status`=1 WHERE `service_book_tbl`.`service_book_id` = '"
                    + data["serviceBookID"]
                    + "'"
                )
                == 1
            ):
                return self.return_data_pop(1, "Service Accepeted successfully", 1)
            else:
                return self.return_data_pop(
                    0, "Error: failed to accept the service", 0.1
                )
        else:
            return self.return_data_pop(
                0, "Error: unauthorized request. no service booking found", 0.1
            )

    def updateServiceBookingData1(self, data, userID):
        # reject service
        if self.validateServiceBookID(data["serviceBookID"]):
            if (
                self.dbConn.execute(
                    "UPDATE `service_book_tbl` SET `status` = 6,`worker_note` = '"
                    + data["worker_note"]
                    + "' WHERE `service_book_tbl`.`service_book_id` = '"
                    + data["serviceBookID"]
                    + "'"
                )
                == 1
            ):
                return self.return_data_pop(1, "Service rejected successfully", 1)
            else:
                return self.return_data_pop(0, "Error: failed to reject service", 0.1)
        else:
            return self.return_data_pop(
                0, "Error: unauthorized request. no service booking found", 0.1
            )

    def updateServiceBookingData2(self, data, userID):
        # reject service
        if self.validateServiceBookID(data["serviceBookID"]):
            if (
                self.dbConn.execute(
                    "UPDATE `service_book_tbl` SET `status` = 2 WHERE `service_book_tbl`.`service_book_id` = '"
                    + data["serviceBookID"]
                    + "'"
                )
                == 1
            ):
                return self.return_data_pop(
                    1, "Service bike recived by excutive successfully", 1
                )
            else:
                return self.return_data_pop(
                    0, "Error: failed to recive service bike service", 0.1
                )
        else:
            return self.return_data_pop(
                0, "Error: unauthorized request. no service booking found", 0.1
            )

    def updateServiceBookingData3(self, data, userID):
        # reject service
        if self.validateServiceBookID(data["serviceBookID"]):
            if (
                self.dbConn.execute(
                    "UPDATE `service_book_tbl` SET `status` = 3 WHERE `service_book_tbl`.`service_book_id` = '"
                    + data["serviceBookID"]
                    + "'"
                )
                == 1
            ):
                return self.return_data_pop(1, "Bike status marked as completed", 1)
            else:
                return self.return_data_pop(
                    0, "Error: failed to mark bike status as completed", 0.1
                )
        else:
            return self.return_data_pop(
                0, "Error: unauthorized request. no service booking found", 0.1
            )

    def updateServiceBookingData4(self, data, userID):
        # reject service
        if self.validateServiceBookID(data["serviceBookID"]):
            if (
                self.dbConn.execute(
                    "UPDATE `service_book_tbl` SET `status` = 4 WHERE `service_book_tbl`.`service_book_id` = '"
                    + data["serviceBookID"]
                    + "'"
                )
                == 1
            ):
                return self.return_data_pop(
                    1,
                    "Bike service completed and delivered to customer successfully",
                    1,
                )
            else:
                return self.return_data_pop(
                    0,
                    "Error: failed to update bike status as service completed and delivered",
                    0.1,
                )
        else:
            return self.return_data_pop(
                0, "Error: unauthorized request. no service booking found", 0.1
            )

    def getServiceDetailsData(self, servicebookid):
        self.dbConn.execute(
            "SELECT `service_book_tbl`.`service_book_id`,`service_book_tbl`.`complaints`,`service_book_tbl`.`worker_note`,`service_book_tbl`.`lat`,`service_book_tbl`.`lng`,`bike_brand_tbl`.`brand_name`,`service_book_tbl`.`bike_model`,`service_book_tbl`.`number_plate`,`service_book_tbl`.`alternate_phone`,`service_book_tbl`.`bill_amount`,`service_book_tbl`.`pickup_mode`,`service_book_tbl`.`created_at`,`service_book_tbl`.`estimate_delivery`,`service_book_tbl`.`bill_status`,`service_book_tbl`.`status`,`user_tbl`.`fullname`,`user_tbl`.`email`,`user_tbl`.`phone`,`user_tbl`.`address`,`cities`.`city`,`states`.`name` from `service_book_tbl` INNER JOIN `user_tbl` ON `service_book_tbl`.`user_id` = `user_tbl`.`user_id` INNER JOIN `bike_brand_tbl` ON `service_book_tbl`.`bike_brand_id` = `bike_brand_tbl`.`brand_id` INNER JOIN `cities` ON `user_tbl`.`city_id` = `cities`.`id` INNER JOIN `states` ON `cities`.`state_id` = `states`.`id`  WHERE `service_book_tbl`.`service_book_id` = '"
            + servicebookid
            + "';"
        )
        data = self.dbConn.fetchone()
        if not data:
            return False
        else:
            # return data
            data = list(data)
            self.dbConn.execute(
                "SELECT * FROM `service_book_img_tbl` WHERE `service_book_img_tbl`.`service_book_id` = '"
                + str(data[0])
                + "'"
            )
            data.append(self.dbConn.fetchall())
            return data

    def getServiceFeedbackData(self, userID):
        def getSubjectivity(text):
            return TextBlob(text).sentiment.subjectivity

        # Create a function to get the polarity
        def getPolarity(text):
            return TextBlob(text).sentiment.polarity

        def getAnalysis(score):
            if score < 0:
                return emoji.emojize("Negative :face_with_symbols_on_mouth:")
            elif score == 0:
                return emoji.emojize("Neutral :neutral_face:")
            else:
                return emoji.emojize("Positive :smiling_face_with_hearts:")

        self.dbConn.execute(
            "SELECT `service_feedback_tbl`.`feedback_id`,`service_feedback_tbl`.`rating`,`service_feedback_tbl`.`comment`,`user_tbl`.`fullname`,`user_tbl`.`email`,`service_feedback_tbl`.`created_at` FROM `service_feedback_tbl` INNER JOIN `user_tbl` ON `service_feedback_tbl`.`user_id` = `user_tbl`.`user_id` WHERE `service_feedback_tbl`.`service_book_id` IN (SELECT `service_book_tbl`.`service_book_id` FROM `service_book_tbl` WHERE `service_book_tbl`.`service_id` in (SELECT `service_list_tbl`.`service_id` FROM `service_list_tbl` WHERE `service_list_tbl`.`ser_center_id` = '"
            + userID
            + "'));"
        )
        data1 = self.dbConn.fetchall()
        new_data = []
        if not data1:
            return False
        else:
            for key in data1:
                # return data
                data = list(key)
                data.append(getAnalysis(getPolarity(key[2])))
                data.append(getPolarity(key[2]))
                data.append(getSubjectivity(key[2]))
                new_data.append(data)
        return new_data

    def getBikeSalesData(self, userID):
        self.dbConn.execute(
            "SELECT `bike_purchase_tbl`.`purchase_id`,`bike_purchase_tbl`.`bike_id`,`bike_purchase_tbl`.`bill_address`,`bike_purchase_tbl`.`bill_pincode`,`bike_purchase_tbl`.`contact_no`,`bike_purchase_tbl`.`purchase_type`,`bike_purchase_tbl`.`aadhar_no`,`bike_purchase_tbl`.`signature_img`,`bike_purchase_tbl`.`aadhar_img`,`bike_purchase_tbl`.`other_proof_img`,`bike_purchase_tbl`.`expected_delivery`,`bike_purchase_tbl`.`created_at`,`bike_purchase_tbl`.`status`,`bike_purchase_tbl`.`bill_name`,`bike_purchase_tbl`.`payment_status`,`sales_bike_tbl`.`bike_name`,if(`bike_purchase_tbl`.`purchase_type` = 0,`sales_bike_tbl`.`min_advance`,`sales_bike_tbl`.`price`) as paid_amount FROM `bike_purchase_tbl` INNER JOIN `sales_bike_tbl` ON `bike_purchase_tbl`.`bike_id` = `sales_bike_tbl`.`bike_id` WHERE `bike_purchase_tbl`.`bike_id` IN (SELECT `sales_bike_tbl`.`bike_id` FROM `sales_bike_tbl` WHERE `sales_bike_tbl`.`ser_center_id` = '"
            + userID
            + "') AND `bike_purchase_tbl`.`status` = 0;"
        )
        return self.dbConn.fetchall()

    def getPurchaseDetailData(self, purchasebookid):
        self.dbConn.execute(
            "SELECT `bike_purchase_tbl`.`purchase_id`,`bike_purchase_tbl`.`bike_id`,`bike_purchase_tbl`.`bill_address`,`bike_purchase_tbl`.`bill_pincode`,`bike_purchase_tbl`.`contact_no`,`bike_purchase_tbl`.`purchase_type`,`bike_purchase_tbl`.`aadhar_no`,`bike_purchase_tbl`.`signature_img`,`bike_purchase_tbl`.`aadhar_img`,`bike_purchase_tbl`.`other_proof_img`,`bike_purchase_tbl`.`expected_delivery`,`bike_purchase_tbl`.`created_at`,`bike_purchase_tbl`.`status`,`bike_purchase_tbl`.`bill_name`,`bike_purchase_tbl`.`payment_status`,`sales_bike_tbl`.`bike_name`,if(`bike_purchase_tbl`.`purchase_type` = 0,`sales_bike_tbl`.`min_advance`,`sales_bike_tbl`.`price`) as paid_amount,`sales_bike_tbl`.`min_advance`,`sales_bike_tbl`.`price`,`bike_brand_tbl`.`brand_name`,`user_tbl`.`fullname`,`user_tbl`.`email`,`user_tbl`.`phone`,`user_tbl`.`address` FROM `bike_purchase_tbl` INNER JOIN `sales_bike_tbl` ON `bike_purchase_tbl`.`bike_id` = `sales_bike_tbl`.`bike_id` INNER JOIN `bike_brand_tbl` ON `sales_bike_tbl`.`brand_id` = `bike_brand_tbl`.`brand_id` INNER JOIN `user_tbl` ON `bike_purchase_tbl`.`user_id` = `user_tbl`.`user_id` WHERE `bike_purchase_tbl`.`purchase_id` = '"
            + purchasebookid
            + "'"
        )
        data = self.dbConn.fetchone()
        if not data:
            return False
        else:
            # return data
            data = list(data)
            self.dbConn.execute(
                "SELECT `sales_bike_img_tbl`.`image_name` FROM `sales_bike_img_tbl` WHERE `sales_bike_img_tbl`.`sales_bike_id` = '"
                + str(data[1])
                + "'"
            )
            data.append(self.dbConn.fetchall())
            return data

    def updateSalesPruchaseData(self, data, userID):
        if self.validatePurchaseBookID(data["purchaseID"]):
            if (
                self.dbConn.execute(
                    "UPDATE `bike_purchase_tbl` SET `status`= 1 WHERE `bike_purchase_tbl`.`purchase_id` = '"
                    + data["purchaseID"]
                    + "'"
                )
                == 1
            ):
                return self.return_data_pop(1, "Bike Purchase request confirmed", 1)
            else:
                return self.return_data_pop(
                    0, "Error: failed to mark purchase status as confirmed", 0.1
                )
        else:
            return self.return_data_pop(
                0, "Error: unauthorized request. no purchase id found", 0.1
            )

    def updateSalesPruchaseData1(self, data, userID):
        if self.validatePurchaseBookID(data["purchaseID"]):
            if (
                self.dbConn.execute(
                    "UPDATE `bike_purchase_tbl` SET `status`= 4 WHERE `bike_purchase_tbl`.`purchase_id` = '"
                    + data["purchaseID"]
                    + "'"
                )
                == 1
            ):
                return self.return_data_pop(1, "Bike Purchase request rejected", 1)
            else:
                return self.return_data_pop(
                    0, "Error: failed to reject bike purchase", 0.1
                )
        else:
            return self.return_data_pop(
                0, "Error: unauthorized request. no purchase id found", 0.1
            )

    def updateSalesPruchaseData2(self, data, userID):
        if self.validatePurchaseBookID(data["purchaseID"]):
            if (
                self.dbConn.execute(
                    "UPDATE `bike_purchase_tbl` SET `status`= 2 WHERE `bike_purchase_tbl`.`purchase_id` = '"
                    + data["purchaseID"]
                    + "'"
                )
                == 1
            ):
                return self.return_data_pop(1, "Bike delivered to customer", 1)
            else:
                return self.return_data_pop(
                    0, "Error: failed to deliver bike to customer", 0.1
                )
        else:
            return self.return_data_pop(
                0, "Error: unauthorized request. no purchase id found", 0.1
            )

    def getpurchaseBookingData1(self, userID):
        self.dbConn.execute(
            "SELECT `bike_purchase_tbl`.`purchase_id`,`bike_purchase_tbl`.`bike_id`,`bike_purchase_tbl`.`bill_address`,`bike_purchase_tbl`.`bill_pincode`,`bike_purchase_tbl`.`contact_no`,`bike_purchase_tbl`.`purchase_type`,`bike_purchase_tbl`.`aadhar_no`,`bike_purchase_tbl`.`signature_img`,`bike_purchase_tbl`.`aadhar_img`,`bike_purchase_tbl`.`other_proof_img`,`bike_purchase_tbl`.`expected_delivery`,`bike_purchase_tbl`.`created_at`,`bike_purchase_tbl`.`status`,`bike_purchase_tbl`.`bill_name`,`bike_purchase_tbl`.`payment_status`,`sales_bike_tbl`.`bike_name`,if(`bike_purchase_tbl`.`purchase_type` = 0,`sales_bike_tbl`.`min_advance`,`sales_bike_tbl`.`price`) as paid_amount FROM `bike_purchase_tbl` INNER JOIN `sales_bike_tbl` ON `bike_purchase_tbl`.`bike_id` = `sales_bike_tbl`.`bike_id` WHERE `bike_purchase_tbl`.`bike_id` IN (SELECT `sales_bike_tbl`.`bike_id` FROM `sales_bike_tbl` WHERE `sales_bike_tbl`.`ser_center_id` = '"
            + userID
            + "') AND `bike_purchase_tbl`.`status` = 1;"
        )
        return self.dbConn.fetchall()

    def getpurchaseBookingData2(self, userID):
        self.dbConn.execute(
            "SELECT `bike_purchase_tbl`.`purchase_id`,`bike_purchase_tbl`.`bike_id`,`bike_purchase_tbl`.`bill_address`,`bike_purchase_tbl`.`bill_pincode`,`bike_purchase_tbl`.`contact_no`,`bike_purchase_tbl`.`purchase_type`,`bike_purchase_tbl`.`aadhar_no`,`bike_purchase_tbl`.`signature_img`,`bike_purchase_tbl`.`aadhar_img`,`bike_purchase_tbl`.`other_proof_img`,`bike_purchase_tbl`.`expected_delivery`,`bike_purchase_tbl`.`created_at`,`bike_purchase_tbl`.`status`,`bike_purchase_tbl`.`bill_name`,`bike_purchase_tbl`.`payment_status`,`sales_bike_tbl`.`bike_name`,if(`bike_purchase_tbl`.`purchase_type` = 0,`sales_bike_tbl`.`min_advance`,`sales_bike_tbl`.`price`) as paid_amount FROM `bike_purchase_tbl` INNER JOIN `sales_bike_tbl` ON `bike_purchase_tbl`.`bike_id` = `sales_bike_tbl`.`bike_id` WHERE `bike_purchase_tbl`.`bike_id` IN (SELECT `sales_bike_tbl`.`bike_id` FROM `sales_bike_tbl` WHERE `sales_bike_tbl`.`ser_center_id` = '"
            + userID
            + "') AND `bike_purchase_tbl`.`status` = 2;"
        )
        return self.dbConn.fetchall()

    def sendMail(sender, reciver, subject, content):
        msg = MIMEMultipart()
        msg['From'] = 'shefanyshanavas2023b@mca.ajce.in'
        msg['To'] = reciver
        msg['Subject'] = subject
        message = content
        msg.attach(MIMEText(message))

        mailserver = smtplib.SMTP('smtp.gmail.com', 587)
        # identify ourselves to smtp gmail client
        mailserver.ehlo()
        # secure our email with tls encryption
        mailserver.starttls()
        # re-identify ourselves as an encrypted connection
        mailserver.ehlo()
        mailserver.login('shefanyshanavas2023b@mca.ajce.in',
                         'ztzkxueyfrwfnvtp')
        mailserver.sendmail(
            'shefanyshanavas2023b@mca.ajce.in', reciver, msg.as_string())
        mailserver.quit()

    def sendResetMail(self, data, request):
        self.dbConn.execute(
            "SELECT * FROM `service_center_table` WHERE `service_center_table`.`email` = '"
            + data["email"]
            + "'"
        )
        data = self.dbConn.fetchone()

        otp = "".join(random.choices(string.ascii_lowercase, k=5))
        if data:
            if (
                self.dbConn.execute(
                    "INSERT INTO `reset_pass_tbl`(`email`, `user_id`, `code`, `created_at`, `status`) VALUES ('"
                    + str(data[5])
                    + "',"
                    + str(data[0])
                    + ",'"
                    + otp
                    + "',now(),1)"
                )
                == 1
            ):
                last_id = self.dbConn.lastrowid
                subject = "password reset mail"
                content = (
                    ' <a href="http://127.0.0.1:8000/service-center/reset-password/'
                    + otp
                    + "/"
                    + str(last_id)
                    + '" >click here to reset your password</a>'
                )
                self.sendMail(data[5], subject, content)
                return self.return_data_pop(
                    1,
                    "Success: we have send mail containing instructions to reset your password",
                    1,
                )
            else:
                return self.return_data_pop(
                    0, "Error: Failed to send you reset password mail", 0
                )
        else:
            return self.return_data_pop(
                0, "Error: Failed to send you reset password mail", 0
            )

    def updateUserForgotPass(self, data, request):
        if self.validateResetPassRequest(data["otp"], data["userid"]):
            userData = self.validateResetPassRequest(
                data["otp"], data["userid"])
            password = hashlib.md5(data["pass"].encode()).hexdigest()
            if (
                self.dbConn.execute(
                    "UPDATE `reset_pass_tbl` SET `status`=0 WHERE `reset_pass_tbl`.`reset_id` = '"
                    + data["userid"]
                    + "'"
                )
                == 1
            ):
                if (
                    self.dbConn.execute(
                        "UPDATE `service_center_table` SET `passw`='"
                        + password
                        + "' WHERE `service_center_table`.`service_center_id` = '"
                        + str(userData[2])
                        + "' AND `service_center_table`.`email` = '"
                        + data["email"]
                        + "'"
                    )
                    == 1
                ):
                    return self.return_data_pop(
                        1, "Success: your password updated successfully", 1
                    )
                else:
                    return self.return_data_pop(
                        0, "Error: something happen from our end.", 3
                    )
            else:
                return self.return_data_pop(
                    0, "Error: something happen from our end.", 2
                )
        else:
            return self.return_data_pop(0, "Error: something happen from our end.", 1)
