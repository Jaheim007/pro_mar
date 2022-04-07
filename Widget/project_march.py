# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/project_march.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Project(object):
    def setupUi(self, Project):
        Project.setObjectName("Project")
        Project.resize(1430, 859)
        self.centralwidget = QtWidgets.QWidget(Project)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(-1, -1, 1431, 861))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Main_page = QtWidgets.QWidget()
        self.Main_page.setObjectName("Main_page")
        self.background_image_page1 = QtWidgets.QLabel(self.Main_page)
        self.background_image_page1.setGeometry(QtCore.QRect(-10, -10, 1451, 871))
        self.background_image_page1.setText("")
        self.background_image_page1.setPixmap(QtGui.QPixmap(":/Images/Static/background.webp"))
        self.background_image_page1.setScaledContents(True)
        self.background_image_page1.setObjectName("background_image_page1")
        self.label = QtWidgets.QLabel(self.Main_page)
        self.label.setGeometry(QtCore.QRect(40, 40, 211, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/Images/Static/LogoMakr-80ZEB9.png"))
        self.label.setObjectName("label")
        self.login_btn_to_direct = QtWidgets.QPushButton(self.Main_page)
        self.login_btn_to_direct.setGeometry(QtCore.QRect(1070, 40, 131, 51))
        self.login_btn_to_direct.setStyleSheet("font: 15pt \".AppleSystemUIFont\";\n"
"background-color: #FFF;\n"
"color: #1589FF;")
        self.login_btn_to_direct.setDefault(False)
        self.login_btn_to_direct.setFlat(True)
        self.login_btn_to_direct.setObjectName("login_btn_to_direct")
        self.signin_btn_to_direct = QtWidgets.QPushButton(self.Main_page)
        self.signin_btn_to_direct.setGeometry(QtCore.QRect(1240, 40, 141, 51))
        self.signin_btn_to_direct.setStyleSheet("font: 15pt \".AppleSystemUIFont\";\n"
"color: #1589FF;\n"
"background-color: #FFF;")
        self.signin_btn_to_direct.setAutoDefault(False)
        self.signin_btn_to_direct.setDefault(False)
        self.signin_btn_to_direct.setFlat(True)
        self.signin_btn_to_direct.setObjectName("signin_btn_to_direct")
        self.label_2 = QtWidgets.QLabel(self.Main_page)
        self.label_2.setGeometry(QtCore.QRect(70, 230, 541, 91))
        self.label_2.setStyleSheet("font: 20pt \".AppleSystemUIFont\";\n"
"color: #A0CFEC;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.Main_page)
        self.label_3.setGeometry(QtCore.QRect(70, 280, 661, 141))
        self.label_3.setStyleSheet("font: 16pt \".AppleSystemUIFont\";\n"
"color: #1589FF;")
        self.label_3.setObjectName("label_3")
        self.start_now_btn = QtWidgets.QPushButton(self.Main_page)
        self.start_now_btn.setGeometry(QtCore.QRect(70, 460, 291, 61))
        self.start_now_btn.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"color:#FFF;\n"
"background-color:  #1589FF;")
        self.start_now_btn.setDefault(True)
        self.start_now_btn.setFlat(False)
        self.start_now_btn.setObjectName("start_now_btn")
        self.stackedWidget.addWidget(self.Main_page)
        self.login_page = QtWidgets.QWidget()
        self.login_page.setObjectName("login_page")
        self.background_image_page1_2 = QtWidgets.QLabel(self.login_page)
        self.background_image_page1_2.setGeometry(QtCore.QRect(0, 0, 1441, 861))
        self.background_image_page1_2.setStyleSheet("")
        self.background_image_page1_2.setText("")
        self.background_image_page1_2.setPixmap(QtGui.QPixmap(":/Images/Static/background.webp"))
        self.background_image_page1_2.setScaledContents(False)
        self.background_image_page1_2.setObjectName("background_image_page1_2")
        self.label_5 = QtWidgets.QLabel(self.login_page)
        self.label_5.setGeometry(QtCore.QRect(40, 40, 211, 51))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/Images/Static/LogoMakr-80ZEB9.png"))
        self.label_5.setObjectName("label_5")
        self.frame = QtWidgets.QFrame(self.login_page)
        self.frame.setGeometry(QtCore.QRect(420, 180, 531, 581))
        self.frame.setStyleSheet("QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 25px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 451, 61))
        self.label_4.setStyleSheet("font: 16pt \".AppleSystemUIFont\";\n"
"")
        self.label_4.setObjectName("label_4")
        self.username_login = QtWidgets.QLineEdit(self.frame)
        self.username_login.setGeometry(QtCore.QRect(50, 140, 401, 41))
        self.username_login.setStyleSheet("background-color: #F8F6F0;")
        self.username_login.setObjectName("username_login")
        self.password_line = QtWidgets.QLineEdit(self.frame)
        self.password_line.setGeometry(QtCore.QRect(50, 320, 401, 41))
        self.password_line.setStyleSheet("background-color: #F8F6F0;")
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line.setObjectName("password_line")
        self.login_btn = QtWidgets.QPushButton(self.frame)
        self.login_btn.setGeometry(QtCore.QRect(160, 430, 181, 51))
        self.login_btn.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"color:#FFF;\n"
"background-color:  #1589FF;")
        self.login_btn.setDefault(True)
        self.login_btn.setFlat(False)
        self.login_btn.setObjectName("login_btn")
        self.email_line = QtWidgets.QLineEdit(self.frame)
        self.email_line.setGeometry(QtCore.QRect(50, 230, 401, 41))
        self.email_line.setStyleSheet("background-color: #F8F6F0;")
        self.email_line.setObjectName("email_line")
        self.label_8 = QtWidgets.QLabel(self.login_page)
        self.label_8.setGeometry(QtCore.QRect(870, 40, 351, 61))
        self.label_8.setStyleSheet("font: 16pt \".AppleSystemUIFont\";\n"
"")
        self.label_8.setObjectName("label_8")
        self.signup_btn_to_signuppage = QtWidgets.QPushButton(self.login_page)
        self.signup_btn_to_signuppage.setGeometry(QtCore.QRect(1240, 50, 151, 41))
        self.signup_btn_to_signuppage.setStyleSheet("QPushButton{\n"
"font: 14pt \".AppleSystemUIFont\";\n"
"color:#FFF;\n"
"background-color:  #1589FF;\n"
"}")
        self.signup_btn_to_signuppage.setDefault(True)
        self.signup_btn_to_signuppage.setFlat(False)
        self.signup_btn_to_signuppage.setObjectName("signup_btn_to_signuppage")
        self.stackedWidget.addWidget(self.login_page)
        self.signup_page = QtWidgets.QWidget()
        self.signup_page.setObjectName("signup_page")
        self.login_btn_to_loginpage = QtWidgets.QPushButton(self.signup_page)
        self.login_btn_to_loginpage.setGeometry(QtCore.QRect(1260, 40, 141, 41))
        self.login_btn_to_loginpage.setStyleSheet("font: 12pt \".AppleSystemUIFont\";\n"
"color:#FFF;\n"
"background-color:  #1589FF;")
        self.login_btn_to_loginpage.setDefault(True)
        self.login_btn_to_loginpage.setFlat(False)
        self.login_btn_to_loginpage.setObjectName("login_btn_to_loginpage")
        self.label_9 = QtWidgets.QLabel(self.signup_page)
        self.label_9.setGeometry(QtCore.QRect(920, 30, 331, 61))
        self.label_9.setStyleSheet("font: 16pt \".AppleSystemUIFont\";\n"
"")
        self.label_9.setObjectName("label_9")
        self.background_image_page1_3 = QtWidgets.QLabel(self.signup_page)
        self.background_image_page1_3.setGeometry(QtCore.QRect(0, 0, 1431, 861))
        self.background_image_page1_3.setText("")
        self.background_image_page1_3.setPixmap(QtGui.QPixmap(":/Images/Static/background.webp"))
        self.background_image_page1_3.setScaledContents(True)
        self.background_image_page1_3.setObjectName("background_image_page1_3")
        self.frame_2 = QtWidgets.QFrame(self.signup_page)
        self.frame_2.setGeometry(QtCore.QRect(470, 110, 511, 681))
        self.frame_2.setStyleSheet("QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 25px\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(20, 30, 461, 61))
        self.label_10.setStyleSheet("font: 16pt \".AppleSystemUIFont\";\n"
"")
        self.label_10.setObjectName("label_10")
        self.nom_line = QtWidgets.QLineEdit(self.frame_2)
        self.nom_line.setGeometry(QtCore.QRect(50, 200, 401, 41))
        self.nom_line.setStyleSheet("background-color: #F8F6F0;")
        self.nom_line.setObjectName("nom_line")
        self.prenom_line = QtWidgets.QLineEdit(self.frame_2)
        self.prenom_line.setGeometry(QtCore.QRect(50, 280, 401, 41))
        self.prenom_line.setStyleSheet("background-color: #F8F6F0;")
        self.prenom_line.setObjectName("prenom_line")
        self.sign_email_line = QtWidgets.QLineEdit(self.frame_2)
        self.sign_email_line.setGeometry(QtCore.QRect(50, 360, 401, 41))
        self.sign_email_line.setStyleSheet("background-color: #F8F6F0;")
        self.sign_email_line.setObjectName("sign_email_line")
        self.sign_password_line = QtWidgets.QLineEdit(self.frame_2)
        self.sign_password_line.setGeometry(QtCore.QRect(50, 440, 401, 41))
        self.sign_password_line.setStyleSheet("background-color: #F8F6F0;")
        self.sign_password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sign_password_line.setObjectName("sign_password_line")
        self.confirm_password = QtWidgets.QLineEdit(self.frame_2)
        self.confirm_password.setGeometry(QtCore.QRect(50, 520, 401, 41))
        self.confirm_password.setStyleSheet("background-color: #F8F6F0;")
        self.confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password.setObjectName("confirm_password")
        self.signup_btn = QtWidgets.QPushButton(self.frame_2)
        self.signup_btn.setGeometry(QtCore.QRect(160, 590, 181, 51))
        self.signup_btn.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"color:#FFF;\n"
"background-color:  #1589FF;")
        self.signup_btn.setDefault(True)
        self.signup_btn.setFlat(False)
        self.signup_btn.setObjectName("signup_btn")
        self.username_sign = QtWidgets.QLineEdit(self.frame_2)
        self.username_sign.setGeometry(QtCore.QRect(50, 120, 401, 41))
        self.username_sign.setStyleSheet("background-color: #F8F6F0;")
        self.username_sign.setObjectName("username_sign")
        self.label_13 = QtWidgets.QLabel(self.signup_page)
        self.label_13.setGeometry(QtCore.QRect(40, 40, 211, 51))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/Images/Static/LogoMakr-80ZEB9.png"))
        self.label_13.setObjectName("label_13")
        self.background_image_page1_3.raise_()
        self.login_btn_to_loginpage.raise_()
        self.label_9.raise_()
        self.frame_2.raise_()
        self.label_13.raise_()
        self.stackedWidget.addWidget(self.signup_page)
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.frame_3 = QtWidgets.QFrame(self.home_page)
        self.frame_3.setGeometry(QtCore.QRect(-1, -1, 1431, 91))
        self.frame_3.setStyleSheet("background-color: #123456;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(20, 20, 211, 51))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap(":/Images/Static/LogoMakr-0NnMg3.png"))
        self.label_14.setObjectName("label_14")
        self.nom_line_2 = QtWidgets.QLineEdit(self.frame_3)
        self.nom_line_2.setGeometry(QtCore.QRect(970, 30, 341, 41))
        self.nom_line_2.setStyleSheet("background-color: #F8F6F0;")
        self.nom_line_2.setObjectName("nom_line_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(900, 20, 61, 61))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/Static/search_24px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(200, 200))
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.profile = QtWidgets.QPushButton(self.frame_3)
        self.profile.setGeometry(QtCore.QRect(1330, 20, 71, 61))
        self.profile.setStyleSheet("font: 12pt \".AppleSystemUIFont\";\n"
"color:#FFF;\n"
"background-color: #123456;")
        self.profile.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Images/Static/account_50px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.profile.setIcon(icon1)
        self.profile.setIconSize(QtCore.QSize(100, 100))
        self.profile.setDefault(False)
        self.profile.setFlat(True)
        self.profile.setObjectName("profile")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(560, 80, 1431, 91))
        self.frame_4.setStyleSheet("background-color: #123456;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setGeometry(QtCore.QRect(10, 20, 211, 51))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap(":/Images/Static/LogoMakr-0NnMg3.png"))
        self.label_16.setObjectName("label_16")
        self.nom_line_4 = QtWidgets.QLineEdit(self.frame_4)
        self.nom_line_4.setGeometry(QtCore.QRect(970, 30, 341, 41))
        self.nom_line_4.setStyleSheet("background-color: #F8F6F0;")
        self.nom_line_4.setObjectName("nom_line_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setGeometry(QtCore.QRect(900, 20, 61, 61))
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.profile_3 = QtWidgets.QPushButton(self.frame_4)
        self.profile_3.setGeometry(QtCore.QRect(1330, 20, 71, 61))
        self.profile_3.setStyleSheet("font: 12pt \".AppleSystemUIFont\";\n"
"color:#FFF;\n"
"background-color: #123456;")
        self.profile_3.setText("")
        self.profile_3.setIcon(icon1)
        self.profile_3.setIconSize(QtCore.QSize(100, 100))
        self.profile_3.setDefault(False)
        self.profile_3.setFlat(True)
        self.profile_3.setObjectName("profile_3")
        self.line = QtWidgets.QFrame(self.home_page)
        self.line.setGeometry(QtCore.QRect(0, 75, 1431, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frame_5 = QtWidgets.QFrame(self.home_page)
        self.frame_5.setGeometry(QtCore.QRect(0, 90, 391, 771))
        self.frame_5.setStyleSheet("background-color: #123456;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        self.label_11.setGeometry(QtCore.QRect(-10, 40, 401, 51))
        self.label_11.setStyleSheet("font: 16pt \".AppleSystemUIFont\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_11.setObjectName("label_11")
        self.signup_btn_2 = QtWidgets.QPushButton(self.frame_5)
        self.signup_btn_2.setGeometry(QtCore.QRect(-50, 120, 341, 51))
        self.signup_btn_2.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"color:#FFF;\n"
"background-color: #123456;")
        self.signup_btn_2.setDefault(False)
        self.signup_btn_2.setFlat(True)
        self.signup_btn_2.setObjectName("signup_btn_2")
        self.signup_btn_3 = QtWidgets.QPushButton(self.frame_5)
        self.signup_btn_3.setGeometry(QtCore.QRect(-50, 200, 321, 51))
        self.signup_btn_3.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"color:#FFF;\n"
"background-color: #123456;")
        self.signup_btn_3.setDefault(False)
        self.signup_btn_3.setFlat(True)
        self.signup_btn_3.setObjectName("signup_btn_3")
        self.signup_btn_4 = QtWidgets.QPushButton(self.frame_5)
        self.signup_btn_4.setGeometry(QtCore.QRect(-40, 270, 361, 51))
        self.signup_btn_4.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"color:#FFF;\n"
"background-color: #123456;")
        self.signup_btn_4.setDefault(False)
        self.signup_btn_4.setFlat(True)
        self.signup_btn_4.setObjectName("signup_btn_4")
        self.signup_btn_5 = QtWidgets.QPushButton(self.frame_5)
        self.signup_btn_5.setGeometry(QtCore.QRect(-100, 340, 451, 51))
        self.signup_btn_5.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"color:#FFF;\n"
"background-color: #123456;")
        self.signup_btn_5.setDefault(False)
        self.signup_btn_5.setFlat(True)
        self.signup_btn_5.setObjectName("signup_btn_5")
        self.signup_btn_6 = QtWidgets.QPushButton(self.frame_5)
        self.signup_btn_6.setGeometry(QtCore.QRect(-160, 410, 571, 61))
        self.signup_btn_6.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"color:#FFF;\n"
"background-color: #123456;")
        self.signup_btn_6.setDefault(False)
        self.signup_btn_6.setFlat(True)
        self.signup_btn_6.setObjectName("signup_btn_6")
        self.signup_btn_7 = QtWidgets.QPushButton(self.frame_5)
        self.signup_btn_7.setGeometry(QtCore.QRect(-60, 490, 351, 71))
        self.signup_btn_7.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"color:#FFF;\n"
"background-color: #123456;")
        self.signup_btn_7.setDefault(False)
        self.signup_btn_7.setFlat(True)
        self.signup_btn_7.setObjectName("signup_btn_7")
        self.line_3 = QtWidgets.QFrame(self.frame_5)
        self.line_3.setGeometry(QtCore.QRect(0, 170, 391, 31))
        self.line_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame_5)
        self.line_4.setGeometry(QtCore.QRect(0, 250, 391, 31))
        self.line_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.frame_5)
        self.line_5.setGeometry(QtCore.QRect(0, 320, 391, 31))
        self.line_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.frame_5)
        self.line_6.setGeometry(QtCore.QRect(0, 390, 391, 31))
        self.line_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.frame_5)
        self.line_7.setGeometry(QtCore.QRect(0, 470, 391, 31))
        self.line_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.frame_5)
        self.line_8.setGeometry(QtCore.QRect(0, 550, 391, 31))
        self.line_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.frame_5)
        self.line_9.setGeometry(QtCore.QRect(0, 90, 391, 31))
        self.line_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_2 = QtWidgets.QFrame(self.home_page)
        self.line_2.setGeometry(QtCore.QRect(380, 90, 20, 771))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.background_image_page1_4 = QtWidgets.QLabel(self.home_page)
        self.background_image_page1_4.setGeometry(QtCore.QRect(0, 0, 1431, 861))
        self.background_image_page1_4.setText("")
        self.background_image_page1_4.setPixmap(QtGui.QPixmap(":/Images/Static/background.webp"))
        self.background_image_page1_4.setScaledContents(True)
        self.background_image_page1_4.setObjectName("background_image_page1_4")
        self.label_6 = QtWidgets.QLabel(self.home_page)
        self.label_6.setGeometry(QtCore.QRect(420, 110, 971, 721))
        self.label_6.setObjectName("label_6")
        self.background_image_page1_4.raise_()
        self.frame_3.raise_()
        self.frame_5.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.label_6.raise_()
        self.stackedWidget.addWidget(self.home_page)
        Project.setCentralWidget(self.centralwidget)

        self.retranslateUi(Project)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Project)

    def retranslateUi(self, Project):
        _translate = QtCore.QCoreApplication.translate
        Project.setWindowTitle(_translate("Project", "MainWindow"))
        self.login_btn_to_direct.setText(_translate("Project", "Connexion"))
        self.signin_btn_to_direct.setText(_translate("Project", "S\'inscrire"))
        self.label_2.setText(_translate("Project", "<html><head/><body><p><span style=\" text-decoration: underline;\">Bienvenue sur Code Breaker</span></p></body></html>"))
        self.label_3.setText(_translate("Project", "<html><head/><body><p>Rejoignez les millions d\'apprenants à coder </p><p>avec Code Breaker gratuitement</p></body></html>"))
        self.start_now_btn.setText(_translate("Project", "Commencez maintenant"))
        self.label_4.setText(_translate("Project", "<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline;\">Connectez-vous à Code Breaker</span></p></body></html>"))
        self.username_login.setPlaceholderText(_translate("Project", "Nom d\'utilisateur"))
        self.password_line.setPlaceholderText(_translate("Project", "Mot de passe"))
        self.login_btn.setText(_translate("Project", "Connexion"))
        self.email_line.setPlaceholderText(_translate("Project", "Email"))
        self.label_8.setText(_translate("Project", "<html><head/><body><p><span style=\" text-decoration: underline;\">Vous n\'avez pas de compte ?</span></p></body></html>"))
        self.signup_btn_to_signuppage.setText(_translate("Project", "S\'inscrire"))
        self.login_btn_to_loginpage.setText(_translate("Project", "Connexion"))
        self.label_9.setText(_translate("Project", "<html><head/><body><p><span style=\" text-decoration: underline;\">Vous avez déjà un compte?</span></p></body></html>"))
        self.label_10.setText(_translate("Project", "<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline;\">Inscrivez-vous à Code Breaker</span></p></body></html>"))
        self.nom_line.setPlaceholderText(_translate("Project", "Nom"))
        self.prenom_line.setPlaceholderText(_translate("Project", "Prenom"))
        self.sign_email_line.setPlaceholderText(_translate("Project", "Email"))
        self.sign_password_line.setPlaceholderText(_translate("Project", "Mot de passe"))
        self.confirm_password.setPlaceholderText(_translate("Project", "Confirmez le mot de passe"))
        self.signup_btn.setText(_translate("Project", "S\'inscrire"))
        self.username_sign.setPlaceholderText(_translate("Project", "Nom d\'utilisateur"))
        self.nom_line_2.setPlaceholderText(_translate("Project", "Rechercher un language de progammation"))
        self.nom_line_4.setPlaceholderText(_translate("Project", "Rechercher un language de progammation"))
        self.label_11.setText(_translate("Project", "<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline;\">Language de progammation</span></p><p align=\"center\"><span style=\" text-decoration: underline;\"><br/></span></p></body></html>"))
        self.signup_btn_2.setText(_translate("Project", "⚬ HTML"))
        self.signup_btn_3.setText(_translate("Project", "⚬ CSS"))
        self.signup_btn_4.setText(_translate("Project", "⚬ JavaScript"))
        self.signup_btn_5.setText(_translate("Project", "⚬ Python"))
        self.signup_btn_6.setText(_translate("Project", "⚬ Flutter"))
        self.signup_btn_7.setText(_translate("Project", "⚬ PHP"))
        self.label_6.setText(_translate("Project", "TextLabel"))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Project = QtWidgets.QMainWindow()
    ui = Ui_Project()
    ui.setupUi(Project)
    Project.show()
    sys.exit(app.exec_())
