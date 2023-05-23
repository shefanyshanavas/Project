from django.db import models, connection
import hashlib
import datetime
import os
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from textblob import TextBlob
import emoji
import random
import string


# Create your models here.
class AdminHelperCls:
    def __init__(self) -> None:
        self.dbConn = connection.cursor()

    def __del__(self):
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

    def validateServiceCenterID(self, centerID):
        self.dbConn.execute(
            "SELECT * FROM `service_center_table` WHERE `service_center_table`.`service_center_id` = '"
            + centerID
            + "'"
        )
        data = self.dbConn.fetchone()
        if not data:
            return False
        else:
            return data

    def validateUsersID(self, centerID):
        self.dbConn.execute(
            "SELECT * FROM `user_tbl` WHERE `user_tbl`.`user_id` = '" + centerID + "'"
        )
        data = self.dbConn.fetchone()
        if not data:
            return False
        else:
            return data

    def validateSuperAdminID(self, adminID):
        self.dbConn.execute(
            "SELECT * FROM `admin_tbl` WHERE `admin_tbl`.`admin_id` = '" + adminID + "'"
        )
        data = self.dbConn.fetchone()
        if not data:
            return False
        else:
            return data

    def isUserExistByPass(self, passw, userID):
        self.dbConn.execute(
            "select * from `admin_tbl` WHERE `admin_tbl`.`admin_id` = '"
            + userID
            + "' AND `admin_tbl`.`passw` = '"
            + passw
            + "'"
        )
        if not self.dbConn.fetchone():
            return False
        else:
            return True


class BasicAdminActionDB(AdminHelperCls):
    def __init__(self) -> None:
        super().__init__()
        self.dbConn = connection.cursor()

    def __del__(self):
        # closing the cursor by destroyer
        self.dbConn.close()

    def return_data_pop(self, status, msg, error_code):
        return_data = {"status": status, "msg": msg, "error_code": error_code}
        return json.dumps(return_data)

    def createUserfnc(self, data):
        password = hashlib.md5(data["password"].encode()).hexdigest()
        self.dbConn.execute(
            "SELECT * FROM `admin_tbl` WHERE `admin_tbl`.`email` = '"
            + data["email"]
            + "'"
        )
        if not self.dbConn.fetchall():
            if (
                self.dbConn.execute(
                    "INSERT INTO `admin_tbl`( `user_name`, `email`, `passw`, `created_at`, `status`) VALUES ('"
                    + data["userName"]
                    + "','"
                    + data["email"]
                    + "','"
                    + password
                    + "',Now(),2)"
                )
                == 1
            ):
                return self.return_data_pop(
                    1,
                    "Account creation completed. please wait untill admin verification complete.",
                    1,
                )
            else:
                return self.return_data_pop(
                    0, "Error: Account registration failed", 0.2
                )
        else:
            return self.return_data_pop(
                0, "Error: User already exist, Please login.", 0.1
            )

    def validateUserLogin(self, data, request):
        password = hashlib.md5(data["password"].encode()).hexdigest()
        email = data["email"]
        self.dbConn.execute(
            "SELECT * FROM `admin_tbl` WHERE `email` = '"
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
            if int(result[5]) == 0:
                return self.return_data_pop(
                    0, "Error: Account is deactivated. please contact admin", 0.2
                )
            elif int(result[5]) == 1:
                request.session["is_logged"] = True
                request.session["data"] = {
                    "user_id": result[0],
                    "name": result[1],
                    "email": result[2],
                    "type": 2,
                }
                return self.return_data_pop(
                    1, "Loggin completed. you will be redirected to home", 1
                )

            else:
                return self.return_data_pop(0, "Error: Something Happended.", 0)

    def getServiceCenterData(self):
        self.dbConn.execute(
            "SELECT * FROM `service_center_table` INNER JOIN `cities` ON `service_center_table`.`city_id` = `cities`.`id` INNER JOIN `states` ON `cities`.`state_id` = `states`.`id`; "
        )
        return self.dbConn.fetchall()

    def enableDisableCenters(self, data):
        if self.validateServiceCenterID(data["centerID"]):
            status = 0 if self.validateServiceCenterID(data["centerID"])[
                11] == 1 else 1
            if (
                self.dbConn.execute(
                    "UPDATE `service_center_table` SET `status`='"
                    + str(status)
                    + "' WHERE `service_center_table`.`service_center_id` = '"
                    + data["centerID"]
                    + "'"
                )
                == 1
            ):
                return self.return_data_pop(1, "Success: Operation completed", 1)
            else:
                return self.return_data_pop(0, "Error: Operation failed", 0.2)
        else:
            return self.return_data_pop(
                0, "Error: unauthorized request. invalid center id", 0.1
            )

    def getUserData(self):
        self.dbConn.execute(
            "SELECT * FROM `user_tbl` INNER JOIN `cities` ON `user_tbl`.`city_id` = `cities`.`id` INNER JOIN `states` on `cities`.`state_id` = `states`.`id`; "
        )
        return self.dbConn.fetchall()

    def enableDisableUsers(self, data):
        if self.validateUsersID(data["userID"]):
            status = 0 if self.validateUsersID(data["userID"])[9] == 1 else 1
            if (
                self.dbConn.execute(
                    "UPDATE `user_tbl` SET `status`='"
                    + str(status)
                    + "' WHERE `user_tbl`.`user_id` = '"
                    + data["userID"]
                    + "'"
                )
                == 1
            ):
                return self.return_data_pop(1, "Success: Operation completed", 1)
            else:
                return self.return_data_pop(0, "Error: Operation failed", 0.2)
        else:
            return self.return_data_pop(
                0, "Error: unauthorized request. invalid center id", 0.1
            )

    def getParticularBikeData(self, bikeid):
        self.dbConn.execute(
            "SELECT * FROM `sales_bike_tbl` WHERE `sales_bike_tbl`.`ser_center_id` = '"
            + bikeid
            + "'"
        )
        data = self.dbConn.fetchall()
        new_data = []
        if data:
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

    def getPraticularServiceData(self, servieid):
        self.dbConn.execute(
            "SELECT * FROM `service_list_tbl` WHERE `service_list_tbl`.`ser_center_id` = '"
            + servieid
            + "'"
        )
        return self.dbConn.fetchall()

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
            "SELECT `service_feedback_tbl`.`feedback_id`,`service_feedback_tbl`.`service_book_id`, `service_feedback_tbl`.`rating`,`service_feedback_tbl`.`comment`,`user_tbl`.`fullname`,`user_tbl`.`email`,`service_feedback_tbl`.`created_at`,`service_center_table`.`center_name`,`service_center_table`.`address`,`service_center_table`.`address`,`service_center_table`.`phone` FROM `service_feedback_tbl` INNER JOIN `user_tbl` ON `service_feedback_tbl`.`user_id` = `user_tbl`.`user_id` INNER JOIN `service_book_tbl` ON `service_feedback_tbl`.`service_book_id` = `service_book_tbl`.`service_book_id` INNER JOIN `service_list_tbl` ON `service_book_tbl`.`service_id` = `service_list_tbl`.`service_id` INNER JOIN `service_center_table` ON `service_list_tbl`.`ser_center_id` = `service_center_table`.`service_center_id`;"
        )
        data1 = self.dbConn.fetchall()
        new_data = []
        if not data1:
            return False
        else:
            for key in data1:
                print
                # return data
                data = list(key)
                data.append(getAnalysis(getPolarity(key[3])))
                data.append(getPolarity(key[3]))
                data.append(getSubjectivity(key[3]))
                new_data.append(data)
        return new_data

    def getBikeBrandData(self):
        self.dbConn.execute("SELECT * FROM `bike_brand_tbl`")
        return self.dbConn.fetchall()

    def updateUserPass(self, data, userID):
        curr_pass = hashlib.md5(data["curr_pass"].encode()).hexdigest()
        passw = hashlib.md5(data["passw"].encode()).hexdigest()
        confpassw = hashlib.md5(data["confpassw"].encode()).hexdigest()
        if self.isUserExistByPass(curr_pass, userID):
            if (
                self.dbConn.execute(
                    "UPDATE `admin_tbl` SET `passw`='"
                    + passw
                    + "' WHERE `admin_tbl`.`admin_id` ='"
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
            "SELECT * FROM `admin_tbl` WHERE `admin_tbl`.`email` = '"
            + data["email"]
            + "'"
        )
        data = self.dbConn.fetchone()

        otp = "".join(random.choices(string.ascii_lowercase, k=5))
        if data:
            if (
                self.dbConn.execute(
                    "INSERT INTO `reset_pass_tbl`(`email`, `user_id`, `code`, `created_at`, `status`) VALUES ('"
                    + str(data[2])
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
                    ' <a href="http://127.0.0.1:8000/admin/reset-password/'
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
            userData = self.validateResetPassRequest(
                data["otp"], data["userid"])
            password = hashlib.md5(data["pass"].encode()).hexdigest()
            if (
                self.dbConn.execute(
                    "UPDATE `reset_pass_tbl` SET `status`= 0 WHERE `reset_pass_tbl`.`reset_id` = '"
                    + data["userid"]
                    + "'"
                )
                == 1
            ):
                if (
                    self.dbConn.execute(
                        "UPDATE `admin_tbl` SET `passw`='"
                        + password
                        + "' WHERE `admin_tbl`.`admin_id` = '"
                        + str(userData[2])
                        + "' AND `admin_tbl`.`email` = '"
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

    def getNotifications(self, request):
        self.dbConn.execute(
            "SELECT * FROM `service_center_table` WHERE `service_center_table`.`status` = 2 "
        )
        data = self.dbConn.fetchall()
        if data:
            return_data = {"status": 1, "data": data}
            return json.dumps(return_data, default=str)
        else:
            return self.return_data_pop(0, "Error: No results found", 1)

    def activateSerivceCenter(self, data):
        if self.validateServiceCenterID(data["centerID"]):
            if (
                self.dbConn.execute(
                    "UPDATE `service_center_table` SET `status`= 1 WHERE `service_center_table`.`service_center_id` = '"
                    + data["centerID"]
                    + "'"
                )
                == 1
            ):
                return self.return_data_pop(1, "Success: Verification completed", 1)
            else:
                return self.return_data_pop(0, "Error: verification failed", 0.2)
        else:
            return self.return_data_pop(
                0, "Error: unauthorized request. invalid center id", 0.1
            )

    def rejectDeleteSerivceCenter(self, data):
        if self.validateServiceCenterID(data["centerID"]):
            if (
                self.dbConn.execute(
                    "DELETE FROM `service_center_table` WHERE `service_center_table`.`service_center_id` = '"
                    + data["centerID"]
                    + "'"
                )
                == 1
            ):
                return self.return_data_pop(
                    1, "Success: Verification rejected and data deleted", 1
                )
            else:
                return self.return_data_pop(
                    0, "Error: verification rejection failed", 0.2
                )
        else:
            return self.return_data_pop(
                0, "Error: unauthorized request. invalid center id", 0.1
            )

    def getSuperUserData(self):
        self.dbConn.execute("SELECT * FROM `admin_tbl`")
        return self.dbConn.fetchall()

    def verifyNewAdminUsers(self, data):
        if self.validateSuperAdminID(data["userID"]):
            if (
                self.dbConn.execute(
                    "UPDATE `admin_tbl` SET `status`= 1 WHERE `admin_tbl`.`admin_id` = '"
                    + data["userID"]
                    + "'"
                )
                == 1
            ):
                return self.return_data_pop(
                    1, "Success: New super user verification completed", 1
                )
            else:
                return self.return_data_pop(
                    0, "Error: failed to verify new super users", 0.2
                )
        else:
            return self.return_data_pop(
                0, "Error: unauthorized request. invalid admin id", 0.1
            )

    def enableDisableAdmins(self, data):
        if self.validateSuperAdminID(data["userID"]):
            status = 0 if self.validateSuperAdminID(data["userID"])[
                5] == 1 else 1
            if (
                self.dbConn.execute(
                    "UPDATE `admin_tbl` SET `status`='"
                    + str(status)
                    + "' WHERE `admin_tbl`.`admin_id` = '"
                    + data["userID"]
                    + "'"
                )
                == 1
            ):
                return self.return_data_pop(1, "Success: Operation completed", 1)
            else:
                return self.return_data_pop(0, "Error: Operation failed", 0.2)
        else:
            return self.return_data_pop(
                0, "Error: unauthorized request. invalid admin id", 0.1
            )
