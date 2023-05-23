from django.db import models, connection
import hashlib, datetime, os
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import razorpay
import random, string

# Create your models here.


class BasicClientHelperCls:
    def __init__(self) -> None:
        super().__init__()
        self.dbConn = connection.cursor()

    # user account registration logic

    def validateServiceID(self, serviceid):
        self.dbConn.execute(
            "SELECT `service_list_tbl`.`service_id`,`service_list_tbl`.`ser_center_id`,`service_list_tbl`.`image_name`,`service_list_tbl`.`service_name`,`service_list_tbl`.`expected_cost`,`service_list_tbl`.`descr`,`service_center_table`.`center_name`,`service_center_table`.`address`,`service_center_table`.`phone`,`cities`.`city`,`states`.`name`  FROM `service_list_tbl` INNER JOIN `service_center_table` ON `service_list_tbl`.`ser_center_id` = `service_center_table`.`service_center_id` INNER JOIN `cities` ON `service_center_table`.`city_id` = `cities`.`id` INNER JOIN `states` ON `cities`.`state_id` = `states`.`id` WHERE `service_list_tbl`.`service_id` = '"
            + serviceid
            + "';"
        )
        if not self.dbConn.fetchone():
            return False
        else:
            return True

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

    def isUserExistByPass(self, passw, userID):
        self.dbConn.execute(
            "select * from `user_tbl` WHERE `user_tbl`.`user_id` = '"
            + userID
            + "' AND `user_tbl`.`passw` = '"
            + passw
            + "'"
        )
        if not self.dbConn.fetchone():
            return False
        else:
            return True

    def getServiceExpectAmount(self, serviceID):
        self.dbConn.execute(
            "SELECT `service_list_tbl`.`expected_cost` as cost FROM `service_list_tbl` WHERE `service_list_tbl`.`service_id` = '"
            + serviceID
            + "'"
        )
        data = self.dbConn.fetchone()
        if not data:
            return False
        else:
            return str(data[0])

    def handle_uploaded_files2(self, f):
        with open(f"static/image/service_book_img/{f.name}", "wb+") as destination:
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
        return True

    def validateServiceBookExist(self, regNo):
        self.dbConn.execute(
            "SELECT * FROM `service_book_tbl` WHERE `service_book_tbl`.`number_plate` = '"
            + regNo
            + "' AND `service_book_tbl`.`status` IN (0,1,2,3)"
        )
        if not self.dbConn.fetchone():
            return True
        else:
            return False

    def handle_uploaded_files3(self, f):
        with open(f"static/image/aadhar_img/{f.name}", "wb+") as destination:
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
        return True

    def handle_uploaded_files4(self, f):
        with open(f"static/image/signature_img/{f.name}", "wb+") as destination:
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
        return True

    def handle_uploaded_files5(self, f):
        with open(f"static/image/other_proofs/{f.name}", "wb+") as destination:
            for chunk in f.chunks():
                destination.write(chunk)
            destination.close()
        return True

    def validateServiceBookID(self, serviceBookID):
        self.dbConn.execute(
            "SELECT * FROM `service_book_tbl` WHERE `service_book_tbl`.`service_book_id` ='"
            + serviceBookID
            + "'"
        )
        data = self.dbConn.fetchone()
        if not data:
            return False
        else:
            return data

    def validatePurchaseID(self, purchaseID):
        self.dbConn.execute(
            "SELECT * FROM `bike_purchase_tbl` WHERE `bike_purchase_tbl`.`purchase_id` ='"
            + purchaseID
            + "'"
        )
        data = self.dbConn.fetchone()
        if not data:
            return False
        else:
            return data


class BasicClientActionDB(BasicClientHelperCls):
    ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg"])

    def __init__(self) -> None:
        super().__init__()
        self.dbConn = connection.cursor()

    # user account registration logic
    def getRazorPayObj(self):
        return razorpay.Client(
            auth=("rzp_test_8V6ZYNb2sa2dAr", "dgBQC8XSAq1fAGqgOub725rb")
        )

    def getParticularServiceData(self, serviceid):
        if self.validateServiceID(serviceid):
            self.dbConn.execute(
                "SELECT `service_list_tbl`.`service_id`,`service_list_tbl`.`ser_center_id`,`service_list_tbl`.`image_name`,`service_list_tbl`.`service_name`,`service_list_tbl`.`expected_cost`,`service_list_tbl`.`descr`,`service_center_table`.`center_name`,`service_center_table`.`address`,`service_center_table`.`phone`,`cities`.`city`,`states`.`name`  FROM `service_list_tbl` INNER JOIN `service_center_table` ON `service_list_tbl`.`ser_center_id` = `service_center_table`.`service_center_id` INNER JOIN `cities` ON `service_center_table`.`city_id` = `cities`.`id` INNER JOIN `states` ON `cities`.`state_id` = `states`.`id` WHERE `service_list_tbl`.`service_id` = '"
                + serviceid
                + "';"
            )
            return self.dbConn.fetchone()
        else:
            return False

    def cancellBikeBooking(self, purchase_id, status, userID):
        if (
            self.dbConn.execute(
                "UPDATE `bike_purchase_tbl` SET `status`='"
                + status
                + "' WHERE `bike_purchase_tbl`.`purchase_id` = '"
                + purchase_id
                + "' AND `bike_purchase_tbl`.`user_id` ='"
                + userID
                + "'"
            )
            == 1
        ):
            return self.return_data_pop(1, "Success : Bike purchase cancelled.", 1)
        else:
            return self.return_data_pop(
                0, "Error: Failed to cancell bike purchase. please retry", 0.2
            )

    def getUserProfileData(self, userID):
        self.dbConn.execute(
            "SELECT * FROM `user_tbl` WHERE `user_tbl`.`user_id` = '" + userID + "';"
        )
        return self.dbConn.fetchone()

    def getBikeBrandData(self):
        self.dbConn.execute("SELECT * FROM `bike_brand_tbl`")
        return self.dbConn.fetchall()

    def getUserAddressData(self, userID):
        self.dbConn.execute(
            "SELECT * FROM `user_addr_tbl` WHERE `user_addr_tbl`.`user_id` = '"
            + userID
            + "';"
        )
        return self.dbConn.fetchone()

    def getServiceCenterData(self):
        self.dbConn.execute(
            "SELECT `service_list_tbl`.`service_id`,`service_list_tbl`.`ser_center_id`,`service_list_tbl`.`image_name`,`service_list_tbl`.`service_name`,`service_list_tbl`.`expected_cost`,`service_center_table`.`center_name`,`service_center_table`.`address`,`service_center_table`.`phone`,`cities`.`city`,`states`.`name`  FROM `service_list_tbl` INNER JOIN `service_center_table` ON `service_list_tbl`.`ser_center_id` = `service_center_table`.`service_center_id` INNER JOIN `cities` ON `service_center_table`.`city_id` = `cities`.`id` INNER JOIN `states` ON `cities`.`state_id` = `states`.`id` WHERE `service_list_tbl`.`status` = 1"
        )
        return self.dbConn.fetchall()

    def getRecomServiceCenterData(self):
        self.dbConn.execute(
            "SELECT `service_list_tbl`.`service_id`,`service_list_tbl`.`ser_center_id`,`service_list_tbl`.`image_name`,`service_list_tbl`.`service_name`,`service_list_tbl`.`expected_cost`,`service_center_table`.`center_name`,`service_center_table`.`address`,`service_center_table`.`phone`,`cities`.`city`,`states`.`name`  FROM `service_list_tbl` INNER JOIN `service_center_table` ON `service_list_tbl`.`ser_center_id` = `service_center_table`.`service_center_id` INNER JOIN `cities` ON `service_center_table`.`city_id` = `cities`.`id` INNER JOIN `states` ON `cities`.`state_id` = `states`.`id` WHERE `service_list_tbl`.`status` = 1 ORDER BY RAND() LIMIT 4;"
        )
        return self.dbConn.fetchall()

    def getStateData(self):
        self.dbConn.execute("SELECT `states`.`id`,`states`.`name` FROM `states`")
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

    def getBikeStock(self, salesBikeID):
        self.dbConn.execute(
            "SELECT `sales_bike_tbl`.`stock` as stock FROM `sales_bike_tbl` WHERE `sales_bike_tbl`.`bike_id` = '"
            + salesBikeID
            + "'"
        )
        data = self.dbConn.fetchone()
        if data:
            return int(data[0])
        else:
            return 0

    def getSalesBikeData1(self, userID, salesBikeID):
        self.dbConn.execute(
            "SELECT `sales_bike_tbl`.`bike_id`,`sales_bike_tbl`.`bike_name`,`sales_bike_tbl`.`min_advance`,`sales_bike_tbl`.`stock`,`sales_bike_tbl`.`descr`,`sales_bike_tbl`.`price`,`bike_brand_tbl`.`brand_name`,`service_center_table`.`center_name`,`service_center_table`.`address`,`service_center_table`.`phone`,`service_center_table`.`email`,`cities`.`city`,`states`.`name`,`bike_brand_tbl`.`brand_name` FROM `sales_bike_tbl` INNER JOIN `service_center_table` ON `sales_bike_tbl`.`ser_center_id` = `service_center_table`.`service_center_id` INNER JOIN `bike_brand_tbl` ON `sales_bike_tbl`.`brand_id` = `bike_brand_tbl`.`brand_id` INNER JOIN `cities` ON `service_center_table`.`city_id` = `cities`.`id` INNER JOIN `states` ON `cities`.`state_id` = `states`.`id` WHERE `sales_bike_tbl`.`bike_id` = '"
            + salesBikeID
            + "';"
        )
        data = self.dbConn.fetchone()
        if not data:
            return False
        else:
            new_data = list(data)
            self.dbConn.execute(
                "SELECT `sales_bike_img_tbl`.`image_name` FROM `sales_bike_img_tbl` WHERE `sales_bike_img_tbl`.`sales_bike_id`  = '"
                + str(data[0])
                + "'"
            )
            new_data.append(self.dbConn.fetchall())
            return new_data

    def getBikeSalesDataByCity(self, cityID):
        self.dbConn.execute(
            "SELECT `sales_bike_tbl`.`bike_id`,`sales_bike_tbl`.`bike_name`,`sales_bike_tbl`.`price`,`bike_brand_tbl`.`brand_name` FROM `sales_bike_tbl` INNER JOIN `service_center_table` ON `sales_bike_tbl`.`ser_center_id` = `service_center_table`.`service_center_id` INNER JOIN `bike_brand_tbl` ON `sales_bike_tbl`.`brand_id` = `bike_brand_tbl`.`brand_id` WHERE `sales_bike_tbl`.`ser_center_id` IN (SELECT `service_center_table`.`service_center_id` FROM `service_center_table` WHERE `service_center_table`.`city_id` = '"
            + cityID
            + "');"
        )
        data = self.dbConn.fetchall()
        if not data:
            return self.return_data_pop(0, "Error: No results found", 0.1)
        else:
            new_data = []
            for key in data:
                self.dbConn.execute(
                    "SELECT `sales_bike_img_tbl`.`image_name` FROM `sales_bike_img_tbl` WHERE `sales_bike_img_tbl`.`sales_bike_id` = '"
                    + str(key[0])
                    + "'"
                )
                temp = list(key)
                temp.append(self.dbConn.fetchall())
                new_data.append(temp)
            return json.dumps({"status": 1, "data": new_data})

    def getSearchSalesBikeData(self, keyword):
        self.dbConn.execute(
            "SELECT `sales_bike_tbl`.`bike_id`,`sales_bike_tbl`.`bike_name`,`sales_bike_tbl`.`price`,`bike_brand_tbl`.`brand_name` FROM `sales_bike_tbl` INNER JOIN `service_center_table` ON `sales_bike_tbl`.`ser_center_id` = `service_center_table`.`service_center_id` INNER JOIN `bike_brand_tbl` ON `sales_bike_tbl`.`brand_id` = `bike_brand_tbl`.`brand_id` WHERE `sales_bike_tbl`.`bike_name` LIKE '%"
            + keyword
            + "%' OR `bike_brand_tbl`.`brand_name` LIKE '%"
            + keyword
            + "%';"
        )
        data = self.dbConn.fetchall()
        if not data:
            return self.return_data_pop(0, "Error: No results found", 0.1)
        else:
            new_data = []
            for key in data:
                self.dbConn.execute(
                    "SELECT `sales_bike_img_tbl`.`image_name` FROM `sales_bike_img_tbl` WHERE `sales_bike_img_tbl`.`sales_bike_id` = '"
                    + str(key[0])
                    + "'"
                )
                temp = list(key)
                temp.append(self.dbConn.fetchall())
                new_data.append(temp)
            return json.dumps({"status": 1, "data": new_data})

    def getServiceDataByCity(self, cityID):
        self.dbConn.execute(
            "SELECT `service_list_tbl`.`service_id`,`service_list_tbl`.`ser_center_id`,`service_list_tbl`.`image_name`,`service_list_tbl`.`service_name`,`service_list_tbl`.`expected_cost`,`service_center_table`.`center_name`,`service_center_table`.`address`,`service_center_table`.`phone`,`cities`.`city`,`states`.`name`  FROM `service_list_tbl` INNER JOIN `service_center_table` ON `service_list_tbl`.`ser_center_id` = `service_center_table`.`service_center_id` INNER JOIN `cities` ON `service_center_table`.`city_id` = `cities`.`id` INNER JOIN `states` ON `cities`.`state_id` = `states`.`id` WHERE `service_list_tbl`.`status` = 1 AND `service_list_tbl`.`ser_center_id` IN (SELECT `service_center_table`.`service_center_id` FROM `service_center_table` WHERE `service_center_table`.`city_id` = '"
            + cityID
            + "');"
        )
        result = self.dbConn.fetchall()
        if not result:
            return self.return_data_pop(0, "Error: No results found", 0.1)
        else:
            return json.dumps({"status": 1, "data": result})

    def getSearchServiceData(self, keyword):
        self.dbConn.execute(
            "SELECT `service_list_tbl`.`service_id`,`service_list_tbl`.`ser_center_id`,`service_list_tbl`.`image_name`,`service_list_tbl`.`service_name`,`service_list_tbl`.`expected_cost`,`service_center_table`.`center_name`,`service_center_table`.`address`,`service_center_table`.`phone`,`cities`.`city`,`states`.`name`  FROM `service_list_tbl` INNER JOIN `service_center_table` ON `service_list_tbl`.`ser_center_id` = `service_center_table`.`service_center_id` INNER JOIN `cities` ON `service_center_table`.`city_id` = `cities`.`id` INNER JOIN `states` ON `cities`.`state_id` = `states`.`id` WHERE `service_list_tbl`.`status` = 1 AND `service_list_tbl`.`service_name` LIKE '%"
            + keyword
            + "%' OR `service_center_table`.`center_name` LIKE '%"
            + keyword
            + "%';"
        )
        result = self.dbConn.fetchall()
        if not result:
            return self.return_data_pop(0, "Error: No results found", 0.1)
        else:
            return json.dumps({"status": 1, "data": result})

    def validateSalesBike(self, salesBikeID):
        self.dbConn.execute(
            "SELECT * FROM `sales_bike_tbl` WHERE `sales_bike_tbl`.`bike_id` = '"
            + salesBikeID
            + "'"
        )
        if not self.dbConn.fetchone():
            return False
        else:
            return True

    def validateServiceBook(self, serviceID):
        self.dbConn.execute(
            "SELECT * FROM `service_book_tbl` WHERE `service_book_tbl`.`service_book_id` = '"
            + serviceID
            + "'"
        )
        if not self.dbConn.fetchone():
            return False
        else:
            return True

    def validatePurchaseBook(self, serviceID):
        self.dbConn.execute(
            "SELECT * FROM `bike_purchase_tbl` WHERE `bike_purchase_tbl`.`purchase_id` = '"
            + serviceID
            + "'"
        )
        if not self.dbConn.fetchone():
            return False
        else:
            return True

    def getUserServiceData1(self, userID, serviceid):
        self.dbConn.execute(
            "SELECT `service_book_tbl`.`service_book_id`,`service_book_tbl`.`estimate_delivery`,`service_book_tbl`.`complaints`,`service_book_tbl`.`worker_note`,`service_book_tbl`.`lat`,`service_book_tbl`.`lng`,`service_book_tbl`.`bike_model`,`service_book_tbl`.`number_plate`,`service_book_tbl`.`alternate_phone`,`service_book_tbl`.`bill_amount`,`service_book_tbl`.`pickup_mode`,`bike_brand_tbl`.`brand_name`,`service_list_tbl`.`image_name`,`service_list_tbl`.`service_name`,`service_list_tbl`.`service_id`,`service_center_table`.`center_name`,`service_center_table`.`address`,`service_center_table`.`phone`,`service_center_table`.`email`,`cities`.`city`,`states`.`name`,`service_book_tbl`.`bill_status`,`service_book_tbl`.`status`,`service_book_tbl`.`created_at`,`service_book_tbl`.`estimate_delivery` FROM `service_book_tbl` INNER JOIN `service_list_tbl` ON `service_book_tbl`.`service_id` = `service_list_tbl`.`service_id` INNER JOIN `service_center_table` ON `service_list_tbl`.`ser_center_id` = `service_center_table`.`service_center_id` INNER JOIN `user_tbl` ON `service_book_tbl`.`user_id` = `user_tbl`.`user_id` INNER JOIN `bike_brand_tbl` ON `service_book_tbl`.`bike_brand_id` = `bike_brand_tbl`.`brand_id` INNER JOIN `cities` on `service_center_table`.`city_id` = `cities`.`id` INNER JOIN `states` ON `cities`.`state_id` = `states`.`id` WHERE `service_book_tbl`.`user_id` = '"
            + userID
            + "' AND `service_book_tbl`.`service_book_id` = '"
            + serviceid
            + "';"
        )
        data = self.dbConn.fetchone()
        if not data:
            return False
        else:
            new_data = list(data)
            self.dbConn.execute(
                "SELECT * FROM `service_book_img_tbl` WHERE `service_book_img_tbl`.`service_book_id` = '"
                + str(data[0])
                + "'"
            )
            new_data.append(self.dbConn.fetchall())
            return new_data
        # print(data)

    def getUserServiceData(self, userID):
        self.dbConn.execute(
            "SELECT `service_book_tbl`.`service_book_id`,`service_book_tbl`.`estimate_delivery`,`service_book_tbl`.`complaints`,`service_book_tbl`.`worker_note`,`service_book_tbl`.`lat`,`service_book_tbl`.`lng`,`service_book_tbl`.`bike_model`,`service_book_tbl`.`number_plate`,`service_book_tbl`.`alternate_phone`,`service_book_tbl`.`bill_amount`,`service_book_tbl`.`pickup_mode`,`bike_brand_tbl`.`brand_name`,`service_list_tbl`.`image_name`,`service_list_tbl`.`service_name`,`service_list_tbl`.`service_id`,`service_center_table`.`center_name`,`service_center_table`.`address`,`service_center_table`.`phone`,`service_center_table`.`email`,`cities`.`city`,`states`.`name`,`service_book_tbl`.`bill_status`,`service_book_tbl`.`status`,`service_book_tbl`.`created_at`,`service_book_tbl`.`estimate_delivery` FROM `service_book_tbl` INNER JOIN `service_list_tbl` ON `service_book_tbl`.`service_id` = `service_list_tbl`.`service_id` INNER JOIN `service_center_table` ON `service_list_tbl`.`ser_center_id` = `service_center_table`.`service_center_id` INNER JOIN `user_tbl` ON `service_book_tbl`.`user_id` = `user_tbl`.`user_id` INNER JOIN `bike_brand_tbl` ON `service_book_tbl`.`bike_brand_id` = `bike_brand_tbl`.`brand_id` INNER JOIN `cities` on `service_center_table`.`city_id` = `cities`.`id` INNER JOIN `states` ON `cities`.`state_id` = `states`.`id` WHERE `service_book_tbl`.`user_id` = '"
            + userID
            + "';"
        )
        data = self.dbConn.fetchall()
        if not data:
            return False
        else:
            new_data = []
            for key in data:
                self.dbConn.execute(
                    "SELECT * FROM `service_book_img_tbl` WHERE `service_book_img_tbl`.`service_book_id` = '"
                    + str(key[0])
                    + "'"
                )
                temp = list(key)
                temp.append(self.dbConn.fetchall())
                new_data.append(temp)
            return new_data
        # print(data)

    def getUserPurchaseData(self, userID):
        self.dbConn.execute(
            "SELECT `bike_purchase_tbl`.`purchase_id`,`bike_purchase_tbl`.`bike_id`,`sales_bike_tbl`.`bike_name`,`bike_purchase_tbl`.`bill_address`,`bike_purchase_tbl`.`bill_pincode`,`bike_purchase_tbl`.`contact_no`,`bike_purchase_tbl`.`purchase_type`,`bike_purchase_tbl`.`expected_delivery`,`bike_purchase_tbl`.`aadhar_no`,`bike_purchase_tbl`.`signature_img`,`bike_purchase_tbl`.`aadhar_img`,`bike_purchase_tbl`.`other_proof_img`,IF(`bike_purchase_tbl`.`purchase_type` = 0,`sales_bike_tbl`.`min_advance`,`sales_bike_tbl`.`price`) as paid_amount,`sales_bike_tbl`.`ser_center_id`,`service_center_table`.`center_name`,`service_center_table`.`address`,`service_center_table`.`phone`,`bike_purchase_tbl`.`status`,`bike_purchase_tbl`.`payment_status` FROM `bike_purchase_tbl` INNER JOIN `sales_bike_tbl` ON `bike_purchase_tbl`.`bike_id` = `sales_bike_tbl`.`bike_id` INNER JOIN `service_center_table` ON `sales_bike_tbl`.`ser_center_id` = `service_center_table`.`service_center_id` WHERE `bike_purchase_tbl`.`user_id`  = '"
            + userID
            + "';"
        )
        data = self.dbConn.fetchall()
        if not data:
            return False
        else:
            new_data = []
            for key in data:
                self.dbConn.execute(
                    "SELECT * FROM `sales_bike_img_tbl` WHERE `sales_bike_img_tbl`.`sales_bike_id` = '"
                    + str(key[1])
                    + "'"
                )
                temp = list(key)
                temp.append(self.dbConn.fetchall())
                new_data.append(temp)
            return new_data
        # print(data)

    def getSalesBikeData(self):
        self.dbConn.execute(
            "SELECT `sales_bike_tbl`.`bike_id`,`sales_bike_tbl`.`bike_name`,`sales_bike_tbl`.`price`,`bike_brand_tbl`.`brand_name` FROM `sales_bike_tbl` INNER JOIN `bike_brand_tbl` ON `sales_bike_tbl`.`brand_id` = `bike_brand_tbl`.`brand_id` WHERE `sales_bike_tbl`.`status` = 1;"
        )
        data = self.dbConn.fetchall()
        new_data = []
        for key in data:
            temp = list(key)
            self.dbConn.execute(
                "SELECT `sales_bike_img_tbl`.`image_name` FROM `sales_bike_img_tbl` WHERE `sales_bike_img_tbl`.`sales_bike_id` = '"
                + str(key[0])
                + "'"
            )
            temp.append(self.dbConn.fetchall())
            new_data.append(temp)
        return new_data

    def getRecomSalesBikeData(self):
        self.dbConn.execute(
            "SELECT `sales_bike_tbl`.`bike_id`,`sales_bike_tbl`.`bike_name`,`sales_bike_tbl`.`price`,`bike_brand_tbl`.`brand_name` FROM `sales_bike_tbl` INNER JOIN `bike_brand_tbl` ON `sales_bike_tbl`.`brand_id` = `bike_brand_tbl`.`brand_id` WHERE `sales_bike_tbl`.`status` = 1 ORDER BY RAND() LIMIT 4;"
        )
        data = self.dbConn.fetchall()
        new_data = []
        for key in data:
            temp = list(key)
            self.dbConn.execute(
                "SELECT `sales_bike_img_tbl`.`image_name` FROM `sales_bike_img_tbl` WHERE `sales_bike_img_tbl`.`sales_bike_id` = '"
                + str(key[0])
                + "'"
            )
            temp.append(self.dbConn.fetchall())
            new_data.append(temp)
        return new_data

    def cancellServiceBooking(self, serviceBookID, status, userID):
        if (
            self.dbConn.execute(
                "UPDATE `service_book_tbl` SET `status`='"
                + status
                + "' WHERE `service_book_tbl`.`service_book_id` = '"
                + serviceBookID
                + "' AND `service_book_tbl`.`user_id` ='"
                + userID
                + "'"
            )
            == 1
        ):
            return self.return_data_pop(1, "Success : Service booking cancelled.", 1)
        else:
            return self.return_data_pop(
                0, "Error: Failed to cancell service booking. please retry", 0.2
            )

    def generateServiceBook(self, data, imageFiles, userID):
        if self.getServiceExpectAmount(data["serviceid"]):
            serviceID = data["serviceid"]
            complaints = data["complaints"]
            workerNote = ""
            if int(data["drop_mode"]) == 0:
                lattitude = ""
                longittude = ""
            else:
                lattitude = data["lat"]
                longittude = data["long"]
            bikeBrandID = data["bike_brand"]
            bikeModelName = data["bike_model"]
            bikeRegNo = data["register_no"]
            alterPhone = data["alter_phone"]
            billeAmount = self.getServiceExpectAmount(serviceID)
            pickupMode = data["drop_mode"]
            current_timestamp = datetime.datetime.now()
            estimateDelivery = current_timestamp + datetime.timedelta(days=5)

            if self.validateServiceBookExist(bikeRegNo):
                if (
                    self.dbConn.execute(
                        "INSERT INTO `service_book_tbl`(`service_id`, `user_id`, `complaints`, `worker_note`, `lat`, `lng`, `bike_brand_id`, `bike_model`, `number_plate`, `alternate_phone`, `bill_amount`, `pickup_mode`, `created_at`, `estimate_delivery`, `bill_status`, `status`) VALUES ('"
                        + serviceID
                        + "','"
                        + userID
                        + "','"
                        + complaints
                        + "','"
                        + workerNote
                        + "','"
                        + lattitude
                        + "','"
                        + longittude
                        + "','"
                        + bikeBrandID
                        + "','"
                        + bikeModelName
                        + "','"
                        + bikeRegNo
                        + "','"
                        + alterPhone
                        + "','"
                        + billeAmount
                        + "','"
                        + pickupMode
                        + "',now(),'"
                        + str(estimateDelivery)
                        + "',0,0)"
                    )
                    == 1
                ):
                    last_insertid = str(self.dbConn.lastrowid)
                    image = imageFiles.getlist("bike_images")
                    for key in image:
                        path = "static/image/service_book_img/" + key.name
                        if bool(key) == True:
                            if self.allowed_file(key.name):
                                if not os.path.exists(path):
                                    self.handle_uploaded_files2(key)
                                self.dbConn.execute(
                                    "INSERT INTO `service_book_img_tbl`( `service_book_id`, `image`, `created_at`) VALUES ('"
                                    + last_insertid
                                    + "','"
                                    + key.name
                                    + "',now())"
                                )
                    return self.return_data_pop(
                        1,
                        "Service booking recieved suuccessfully. expected delivery on "
                        + str(estimateDelivery),
                        1,
                    )
                else:
                    return self.return_data_pop(
                        0,
                        "Error: something happen from our end. we couldnt save your service booking",
                        0.4,
                    )
            else:
                return self.return_data_pop(
                    0,
                    "Error: Booking not completed. already service booking pending on this vehichle number.",
                    0.4,
                )
        else:
            return self.return_data_pop(
                0, "Error: unauthorized request. invalid service id recived", 0.4
            )

        # if status  0  : customer booked a new service.
        # satsu  1 : service center accepted service and bike not reached service center
        # status 2 : bike recived at service center and service started
        # status 3 : service completed and ready to deliver
        # status 4 : delivered and completed.
        # status 5 : cancelled by user
        # status 6 : cancelled by service center

    def updateProfile(self, data, userID):
        if (
            self.dbConn.execute(
                "UPDATE `user_tbl` SET `fullname`='"
                + data["fullname"]
                + "',`phone`='"
                + data["phone"]
                + "',`address`='"
                + data["address"]
                + "' WHERE `user_tbl`.`user_id` ='"
                + userID
                + "'"
            )
            == 1
        ):
            return self.return_data_pop(1, "profile updated successfully", 1)
        else:
            return self.return_data_pop(0, "Error: profile updation failed", 0.2)

    def updatePasswrod(self, data, userID):
        curr_pass = hashlib.md5(data["curr_pass"].encode()).hexdigest()
        passw = hashlib.md5(data["passw"].encode()).hexdigest()
        confpassw = hashlib.md5(data["confpassw"].encode()).hexdigest()
        if self.isUserExistByPass(curr_pass, userID):
            if (
                self.dbConn.execute(
                    "UPDATE `user_tbl` SET `passw`='"
                    + passw
                    + "' WHERE `user_tbl`.`user_id` ='"
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

    def createUserfnc(self, data):
        fullname = data["fullname"]
        email = data["email"]
        phone = data["phone"]
        state = data["state"]
        city = data["city"]
        address = data["address"]
        password = hashlib.md5(data["password"].encode()).hexdigest()

        self.dbConn.execute(
            "SELECT * FROM `user_tbl` WHERE `email` = '"
            + email
            + "' OR `phone` = '"
            + phone
            + "'"
        )
        if not self.dbConn.fetchone():
            if (
                self.dbConn.execute(
                    "INSERT INTO `user_tbl`(`fullname`, `email`, `phone`,`city_id`, `address`, `passw`, `date`, `type`, `status`) VALUES ('"
                    + fullname
                    + "','"
                    + email
                    + "','"
                    + phone
                    + "','"
                    + city
                    + "','"
                    + address
                    + "','"
                    + password
                    + "',now(),0,2)"
                )
                == 1
            ):
                last_insertid = str(self.dbConn.lastrowid)
                otp = "".join(random.choices(string.ascii_lowercase, k=5))

                if (
                    self.dbConn.execute(
                        "INSERT INTO `reset_pass_tbl`(`email`, `user_id`, `code`, `created_at`, `status`) VALUES ('"
                        + email
                        + "',"
                        + last_insertid
                        + ",'"
                        + otp
                        + "',now(),1)"
                    )
                    == 1
                ):
                    last_insertid = str(self.dbConn.lastrowid)
                    content = (
                        ' <a href="http://127.0.0.1:8000/account-activate/'
                        + otp
                        + "/"
                        + str(last_insertid)
                        + '/0" >click here to reset your password</a>'
                    )
                    self.sendMail(email, "Activate your MotoLogic Account", content)
                    return self.return_data_pop(
                        1,
                        "Account created successfully, please verify email to login",
                        1,
                    )
                else:
                    return self.return_data_pop(
                        0, "Error:account created, failed to send activation email.", 0
                    )

            else:
                return self.return_data_pop(
                    0, "Error: Account registration failed", 0.2
                )
        else:
            return self.return_data_pop(
                0, "Error: User already exist, Please login.", 0.1
            )

    def getPaymentSessionData(self, request):
        if not request.session["payment"]:
            return False
        else:
            return request.session["payment"]

    def validateUserLogin(self, data, request):
        password = hashlib.md5(data["password"].encode()).hexdigest()
        email = data["email"]
        self.dbConn.execute(
            "SELECT * FROM `user_tbl` WHERE `email` = '"
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
            if int(result[9]) == 0:
                return self.return_data_pop(
                    0, "Error: Account is deactivated. please contact admin", 0.2
                )
            elif int(result[9]) == 2:
                return self.return_data_pop(
                    0,
                    "Error: Please verify your email id, we have send a verification mail to you inbox",
                    0.2,
                )
            elif int(result[9]) == 1:
                request.session["is_logged"] = True
                request.session["data"] = {
                    "user_id": result[0],
                    "name": result[1],
                    "email": result[2],
                    "phone": result[3],
                    "cityid": result[4],
                    "address": result[5],
                    "type": result[8],
                }
                return self.return_data_pop(
                    1, "Loggin completed. you will be redirected to home", 1
                )
            else:
                return self.return_data_pop(
                    0, "Error: Something happend, please retry", 0.2
                )

    def return_data_pop(self, status, msg, error_code):
        return_data = {"status": status, "msg": msg, "error_code": error_code}
        return json.dumps(return_data)

    def __del__(self):
        # closing the cursor by destroyer
        self.dbConn.close()

    def allowed_file(self, filename):
        return (
            "." in filename
            and filename.rsplit(".", 1)[1].lower() in self.ALLOWED_EXTENSIONS
        )

    def bikePurchaseInvoke(self, data, imageFiles, userID, request):
        # salesBikeID = data['salesBikeID']
        stock = self.getBikeStock(data["salesBikeID"]) - 1
        if self.getBikeStock(data["salesBikeID"]) > 0:
            bike_data = self.getSalesBikeData1(userID, data["salesBikeID"])

            if int(data["book_type"]) == 0:
                amount = bike_data[2]
            else:
                amount = bike_data[5]

            current_timestamp = datetime.datetime.now()
            estimateDelivery = current_timestamp + datetime.timedelta(days=15)
            image = imageFiles.getlist("files")
            i = 1
            temp = []
            for key in image:
                path1 = "static/image/aadhar_img/" + key.name
                path2 = "static/image/aadhar_img/" + key.name
                path3 = "static/image/aadhar_img/" + key.name
                temp.append(key.name)
                if bool(key) == True:
                    if self.allowed_file(key.name):
                        if i == 1:
                            if not os.path.exists(path1):
                                self.handle_uploaded_files3(key)
                        elif i == 2:
                            if not os.path.exists(path2):
                                self.handle_uploaded_files4(key)
                        elif i == 3:
                            if not os.path.exists(path3):
                                self.handle_uploaded_files5(key)
                i = i + 1
            if (
                self.dbConn.execute(
                    "INSERT INTO `bike_purchase_tbl`( `bike_id`, `user_id`, `bill_address`, `bill_pincode`, `contact_no`, `purchase_type`, `aadhar_no`, `signature_img`, `aadhar_img`, `other_proof_img`, `expected_delivery`, `created_at`, `status`, `bill_name`,`payment_status`) VALUES ('"
                    + data["salesBikeID"]
                    + "','"
                    + userID
                    + "','"
                    + data["bill_address"]
                    + "','"
                    + data["bill_pincode"]
                    + "','"
                    + data["bill_phone"]
                    + "','"
                    + data["book_type"]
                    + "','"
                    + data["aadharNo"]
                    + "','"
                    + str(temp[1])
                    + "','"
                    + str(temp[0])
                    + "','"
                    + str(temp[2])
                    + "','"
                    + str(estimateDelivery)
                    + "',now(),0,'"
                    + data["bill_name"]
                    + "',0)"
                )
                == 1
            ):
                last_insertid = str(self.dbConn.lastrowid)
                client = self.getRazorPayObj()
                orderData = {
                    "amount": float(amount) * 100,
                    "currency": "INR",
                    "receipt": last_insertid,
                }
                request.session["payment"] = {
                    "data": client.order.create(data=orderData),
                    "last_insertid": last_insertid,
                    "billing_data": data,
                }
                self.dbConn.execute(
                    "UPDATE `sales_bike_tbl` SET `stock`='"
                    + str(stock)
                    + "' WHERE `sales_bike_tbl`.`bike_id` = '"
                    + data["salesBikeID"]
                    + "'"
                )
                return self.return_data_pop(
                    1, "Success:you will be redirected to payment page", last_insertid
                )
            else:
                return self.return_data_pop(
                    0, "Error: Failed to submit your purchase request.", 0.2
                )
        else:
            return self.return_data_pop(0, "Error: Product out of stock.", 0.2)
        # status = 0 = booking recived
        # status = 1 = booking confirmed not delived
        # status = 2 = delivered
        # status = 3 = cancelled by user
        # status = 4 = cancelled by service center

    def verifyPayment(self, data, user_id, request):
        booking_id = data["booking_id"]
        client = self.getRazorPayObj()
        params_dict = {
            "razorpay_order_id": data["razorpay_order_id"],
            "razorpay_payment_id": data["razorpay_payment_id"],
            "razorpay_signature": data["razorpay_signature"],
        }
        status = client.utility.verify_payment_signature(params_dict)
        if status == "True" or status == True:
            self.dbConn.execute(
                "UPDATE `bike_purchase_tbl` SET `payment_status`= 1 WHERE `bike_purchase_tbl`.`purchase_id` = '"
                + booking_id
                + "'"
            )
            return self.return_data_pop(
                1,
                "Success:you will be redirected to payment page. order id :"
                + data["razorpay_order_id"],
                data["razorpay_order_id"],
            )
        else:
            return self.return_data_pop(
                0,
                "Error: Pyament verification failed. please note the order id for futher reference :"
                + data["razorpay_order_id"],
                data["razorpay_order_id"],
            )

    def submitFeedback(self, data, userID):
        self.dbConn.execute(
            "SELECT * FROM `service_feedback_tbl` WHERE `service_feedback_tbl`.`user_id` = '"
            + userID
            + "' AND `service_feedback_tbl`.`service_book_id` = '"
            + data["service_id"]
            + "'"
        )

        if not self.dbConn.fetchone():
            if (
                self.dbConn.execute(
                    "INSERT INTO `service_feedback_tbl`(`user_id`,`service_book_id`, `rating`, `comment`, `created_at`) VALUES ('"
                    + userID
                    + "','"
                    + data["service_id"]
                    + "','"
                    + data["rating"]
                    + "','"
                    + data["comment"]
                    + "',now())"
                )
                == 1
            ):
                return self.return_data_pop(1, "Success: Your feedback  submitted", 1)
            else:
                return self.return_data_pop(
                    0, "Error: failed to submit your feedback", 0
                )
        else:
            if (
                self.dbConn.execute(
                    "UPDATE `service_feedback_tbl` SET `rating`='"
                    + data["rating"]
                    + "',`comment`='"
                    + data["comment"]
                    + "' WHERE `service_feedback_tbl`.`user_id` = '"
                    + userID
                    + "' AND `service_feedback_tbl`.`service_book_id` = '"
                    + data["service_id"]
                    + "'"
                )
                == 1
            ):
                return self.return_data_pop(
                    1, "Success:we already have your feedback and updated it ", 1
                )
            else:
                return self.return_data_pop(
                    0, "Error: failed to submit your feedback", 0
                )

    def submitContactForm(self, data, request):
        if (
            self.dbConn.execute(
                "INSERT INTO `contact_tbl`(`name`, `email`, `subject`, `comments`, `created_at`) VALUES ('"
                + data["name"]
                + "','"
                + data["email"]
                + "','"
                + data["subject"]
                + "','"
                + data["message"]
                + "',now())"
            )
            == 1
        ):
            return self.return_data_pop(1, "Success: Your query submitted", 1)
        else:
            return self.return_data_pop(
                0, "Error: something happend from our end. please try later", 0
            )

    def createServicePaymentRequest(self, serviceid, userID, request):
        self.dbConn.execute(
            "SELECT `service_book_tbl`.`service_book_id`,`service_book_tbl`.`bill_amount`,`user_tbl`.`fullname`,`user_tbl`.`email`,`user_tbl`.`phone`,`user_tbl`.`address`,`cities`.`city`,`states`.`name` FROM `service_book_tbl` INNER JOIN `user_tbl` on `service_book_tbl`.`user_id` = `user_tbl`.`user_id` INNER JOIN `cities` ON `user_tbl`.`city_id` = `cities`.`id` INNER JOIN `states` on `cities`.`state_id` = `states`.`id` WHERE `service_book_tbl`.`service_book_id` = '"
            + serviceid
            + "' AND `service_book_tbl`.`user_id` = '"
            + userID
            + "'"
        )
        data = self.dbConn.fetchone()
        if data:
            client = self.getRazorPayObj()
            orderData = {
                "amount": float(data[1]) * 100,
                "currency": "INR",
                "receipt": serviceid,
            }
            payment_data = client.order.create(data=orderData)
            request.session["service_payment"] = {
                "payment_data": payment_data,
                "billing_data": orderData,
                "serviceid": serviceid,
            }
            return {"payment_data": payment_data, "billing_data": data}
        else:
            return False

    def verifyPayment1(self, data, userID, request):
        booking_id = data["booking_id"]
        client = self.getRazorPayObj()
        params_dict = {
            "razorpay_order_id": data["razorpay_order_id"],
            "razorpay_payment_id": data["razorpay_payment_id"],
            "razorpay_signature": data["razorpay_signature"],
        }
        status = client.utility.verify_payment_signature(params_dict)
        if status == "True" or status == True:
            self.dbConn.execute(
                "UPDATE `service_book_tbl` SET `bill_status`='[value-16]' WHERE `service_book_tbl`.`service_book_id` = '"
                + booking_id
                + "' AND `service_book_tbl`.`user_id` = '"
                + userID
                + "'"
            )
            return self.return_data_pop(
                1,
                "Success:Oyur payment recived successfully. order id :"
                + data["razorpay_order_id"],
                data["razorpay_order_id"],
            )
        else:
            return self.return_data_pop(
                0,
                "Error: Pyament verification failed. please note the order id for futher reference :"
                + data["razorpay_order_id"],
                data["razorpay_order_id"],
            )

    def getPurchaseDetailsData(self, purchaseID):
        self.dbConn.execute(
            "SELECT `bike_purchase_tbl`.`purchase_id`,`bike_purchase_tbl`.`bike_id`,`bike_purchase_tbl`.`bill_address`,`bike_purchase_tbl`.`bill_pincode`,`bike_purchase_tbl`.`contact_no`,`bike_purchase_tbl`.`purchase_type`,`bike_purchase_tbl`.`aadhar_no`,`bike_purchase_tbl`.`signature_img`,`bike_purchase_tbl`.`aadhar_img`,`bike_purchase_tbl`.`other_proof_img`,`bike_purchase_tbl`.`expected_delivery`,`bike_purchase_tbl`.`created_at`,`bike_purchase_tbl`.`status`,`bike_purchase_tbl`.`bill_name`,`bike_purchase_tbl`.`payment_status`,`sales_bike_tbl`.`bike_name`,if(`bike_purchase_tbl`.`purchase_type` = 0,`sales_bike_tbl`.`min_advance`,`sales_bike_tbl`.`price`) as paid_amount,`sales_bike_tbl`.`min_advance`,`sales_bike_tbl`.`price`,`bike_brand_tbl`.`brand_name`,`service_center_table`.`center_name`,`service_center_table`.`address`,`service_center_table`.`phone`,`service_center_table`.`email` ,`cities`.`city`,`states`.`name` FROM `bike_purchase_tbl` INNER JOIN `sales_bike_tbl` ON `bike_purchase_tbl`.`bike_id` = `sales_bike_tbl`.`bike_id` INNER JOIN `bike_brand_tbl` ON `sales_bike_tbl`.`brand_id` = `bike_brand_tbl`.`brand_id` INNER JOIN `service_center_table` ON `sales_bike_tbl`.`ser_center_id` = `service_center_table`.`service_center_id` INNER JOIN `cities` ON`service_center_table`.`city_id` = `cities`.`id` INNER JOIN `states` ON `cities`.`state_id` = `states`.`id` WHERE `bike_purchase_tbl`.`purchase_id` = '"
            + purchaseID
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
            "SELECT * FROM `user_tbl` WHERE `user_tbl`.`email` = '"
            + data["email"]
            + "'"
        )
        data = self.dbConn.fetchone()
        otp = "".join(random.choices(string.ascii_lowercase, k=5))
        if data:
            if (
                self.dbConn.execute(
                    "INSERT INTO `reset_pass_tbl`(`email`, `user_id`, `code`, `created_at`, `status`) VALUES ('"
                    + data[2]
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
                    '<a href="http://127.0.0.1:8000/reset-password/'
                    + otp
                    + "/"
                    + str(last_id)
                    + '" >click here to reset your password</a>'
                )
                self.sendMail(data[2], subject, content)
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
            userData = self.validateResetPassRequest(data["otp"], data["userid"])
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
                        "UPDATE `user_tbl` SET `passw`='"
                        + password
                        + "' WHERE `user_tbl`.`user_id` = '"
                        + str(userData[2])
                        + "' AND `user_tbl`.`email` = '"
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

    def activateAccountByEmail(self, otp, userid, user_type):
        if user_type == 0:
            if self.validateResetPassRequest(otp, userid):
                userData = self.validateResetPassRequest(otp, userid)
                if (
                    self.dbConn.execute(
                        "UPDATE `reset_pass_tbl` SET `status`= 0 WHERE `reset_pass_tbl`.`reset_id` = '"
                        + userid
                        + "'"
                    )
                    == 1
                ):
                    if (
                        self.dbConn.execute(
                            "UPDATE `user_tbl` SET `status`= 1 WHERE `user_tbl`.`user_id` = '"
                            + str(userData[2])
                            + "'"
                        )
                        == 1
                    ):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
