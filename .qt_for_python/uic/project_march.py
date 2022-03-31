# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_march.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resource_rc

class Ui_Project(object):
    def setupUi(self, Project):
        if not Project.objectName():
            Project.setObjectName(u"Project")
        Project.resize(1207, 740)
        self.centralwidget = QWidget(Project)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-1, -1, 1211, 741))
        self.Main_page = QWidget()
        self.Main_page.setObjectName(u"Main_page")
        self.background_image_page1 = QLabel(self.Main_page)
        self.background_image_page1.setObjectName(u"background_image_page1")
        self.background_image_page1.setGeometry(QRect(-10, -10, 1221, 751))
        self.background_image_page1.setPixmap(QPixmap(u":/Images/Static/background.webp"))
        self.background_image_page1.setScaledContents(True)
        self.label = QLabel(self.Main_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 40, 211, 51))
        self.label.setPixmap(QPixmap(u":/Images/Static/LogoMakr-80ZEB9.png"))
        self.login_btn_to_direct = QPushButton(self.Main_page)
        self.login_btn_to_direct.setObjectName(u"login_btn_to_direct")
        self.login_btn_to_direct.setGeometry(QRect(870, 40, 131, 51))
        self.login_btn_to_direct.setStyleSheet(u"font: 18pt \".AppleSystemUIFont\";\n"
"background-color: #FFF;\n"
"color: #1589FF;")
        self.login_btn_to_direct.setFlat(True)
        self.signin_btn_to_direct = QPushButton(self.Main_page)
        self.signin_btn_to_direct.setObjectName(u"signin_btn_to_direct")
        self.signin_btn_to_direct.setGeometry(QRect(1030, 40, 141, 51))
        self.signin_btn_to_direct.setStyleSheet(u"font: 18pt \".AppleSystemUIFont\";\n"
"color: #1589FF;\n"
"background-color: #FFF;")
        self.signin_btn_to_direct.setAutoDefault(False)
        self.signin_btn_to_direct.setFlat(True)
        self.label_2 = QLabel(self.Main_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 180, 511, 91))
        self.label_2.setStyleSheet(u"font: 40pt \".AppleSystemUIFont\";\n"
"color: #A0CFEC;")
        self.label_3 = QLabel(self.Main_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 240, 601, 141))
        self.label_3.setStyleSheet(u"font: 28pt \".AppleSystemUIFont\";\n"
"color: #1589FF;")
        self.start_now_btn = QPushButton(self.Main_page)
        self.start_now_btn.setObjectName(u"start_now_btn")
        self.start_now_btn.setGeometry(QRect(70, 380, 251, 61))
        self.start_now_btn.setStyleSheet(u"font: 18pt \".AppleSystemUIFont\";\n"
"color:#FFF;\n"
"background-color:  #1589FF;")
        self.start_now_btn.setFlat(False)
        self.stackedWidget.addWidget(self.Main_page)
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.background_image_page1_2 = QLabel(self.login_page)
        self.background_image_page1_2.setObjectName(u"background_image_page1_2")
        self.background_image_page1_2.setGeometry(QRect(0, 0, 1211, 741))
        self.background_image_page1_2.setPixmap(QPixmap(u":/Images/Static/background.webp"))
        self.background_image_page1_2.setScaledContents(True)
        self.label_5 = QLabel(self.login_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 40, 211, 51))
        self.label_5.setPixmap(QPixmap(u":/Images/Static/LogoMakr-80ZEB9.png"))
        self.frame = QFrame(self.login_page)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(380, 160, 451, 441))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 30, 341, 61))
        self.label_4.setStyleSheet(u"font: 20pt \".AppleSystemUIFont\";\n"
"")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 100, 231, 21))
        self.label_6.setStyleSheet(u"font: 15pt \".AppleSystemUIFont\";\n"
"")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 200, 81, 21))
        self.label_7.setStyleSheet(u"font: 15pt \".AppleSystemUIFont\";\n"
"")
        self.email_line = QLineEdit(self.frame)
        self.email_line.setObjectName(u"email_line")
        self.email_line.setGeometry(QRect(40, 130, 341, 41))
        self.email_line.setStyleSheet(u"background-color: #F8F6F0;")
        self.password_line = QLineEdit(self.frame)
        self.password_line.setObjectName(u"password_line")
        self.password_line.setGeometry(QRect(40, 230, 341, 41))
        self.password_line.setStyleSheet(u"background-color: #F8F6F0;")
        self.login_btn = QPushButton(self.frame)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(120, 340, 181, 51))
        self.login_btn.setStyleSheet(u"font: 18pt \".AppleSystemUIFont\";\n"
"color:#FFF;\n"
"background-color:  #1589FF;")
        self.login_btn.setFlat(False)
        self.label_8 = QLabel(self.login_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(710, 40, 271, 61))
        self.label_8.setStyleSheet(u"font: 20pt \".AppleSystemUIFont\";\n"
"")
        self.signup_btn_to_signuppage = QPushButton(self.login_page)
        self.signup_btn_to_signuppage.setObjectName(u"signup_btn_to_signuppage")
        self.signup_btn_to_signuppage.setGeometry(QRect(990, 50, 151, 41))
        self.signup_btn_to_signuppage.setStyleSheet(u"font: 18pt \".AppleSystemUIFont\";\n"
"color:#FFF;\n"
"background-color:  #1589FF;")
        self.signup_btn_to_signuppage.setFlat(False)
        self.stackedWidget.addWidget(self.login_page)
        self.signup_page = QWidget()
        self.signup_page.setObjectName(u"signup_page")
        self.login_btn_to_loginpage = QPushButton(self.signup_page)
        self.login_btn_to_loginpage.setObjectName(u"login_btn_to_loginpage")
        self.login_btn_to_loginpage.setGeometry(QRect(1020, 40, 141, 41))
        self.login_btn_to_loginpage.setStyleSheet(u"font: 16pt \".AppleSystemUIFont\";\n"
"color:#FFF;\n"
"background-color:  #1589FF;")
        self.login_btn_to_loginpage.setFlat(False)
        self.label_9 = QLabel(self.signup_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(780, 30, 251, 61))
        self.label_9.setStyleSheet(u"font: 18pt \".AppleSystemUIFont\";\n"
"")
        self.background_image_page1_3 = QLabel(self.signup_page)
        self.background_image_page1_3.setObjectName(u"background_image_page1_3")
        self.background_image_page1_3.setGeometry(QRect(0, 0, 1211, 751))
        self.background_image_page1_3.setPixmap(QPixmap(u":/Images/Static/background.webp"))
        self.background_image_page1_3.setScaledContents(True)
        self.frame_2 = QFrame(self.signup_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(390, 90, 451, 621))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 30, 341, 61))
        self.label_10.setStyleSheet(u"font: 20pt \".AppleSystemUIFont\";\n"
"")
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(40, 100, 231, 21))
        self.label_11.setStyleSheet(u"font: 15pt \".AppleSystemUIFont\";\n"
"")
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(40, 190, 81, 21))
        self.label_12.setStyleSheet(u"font: 15pt \".AppleSystemUIFont\";\n"
"")
        self.nom_line = QLineEdit(self.frame_2)
        self.nom_line.setObjectName(u"nom_line")
        self.nom_line.setGeometry(QRect(40, 130, 341, 41))
        self.nom_line.setStyleSheet(u"background-color: #F8F6F0;")
        self.prenom_line = QLineEdit(self.frame_2)
        self.prenom_line.setObjectName(u"prenom_line")
        self.prenom_line.setGeometry(QRect(40, 220, 341, 41))
        self.prenom_line.setStyleSheet(u"background-color: #F8F6F0;")
        self.sign_email_line = QLineEdit(self.frame_2)
        self.sign_email_line.setObjectName(u"sign_email_line")
        self.sign_email_line.setGeometry(QRect(40, 310, 341, 41))
        self.sign_email_line.setStyleSheet(u"background-color: #F8F6F0;")
        self.sign_password_line = QLineEdit(self.frame_2)
        self.sign_password_line.setObjectName(u"sign_password_line")
        self.sign_password_line.setGeometry(QRect(40, 400, 341, 41))
        self.sign_password_line.setStyleSheet(u"background-color: #F8F6F0;")
        self.sign_password_line.setEchoMode(QLineEdit.Password)
        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(40, 280, 231, 21))
        self.label_14.setStyleSheet(u"font: 15pt \".AppleSystemUIFont\";\n"
"")
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(40, 460, 231, 21))
        self.label_15.setStyleSheet(u"font: 15pt \".AppleSystemUIFont\";\n"
"")
        self.confirm_password = QLineEdit(self.frame_2)
        self.confirm_password.setObjectName(u"confirm_password")
        self.confirm_password.setGeometry(QRect(40, 490, 341, 41))
        self.confirm_password.setStyleSheet(u"background-color: #F8F6F0;")
        self.confirm_password.setEchoMode(QLineEdit.Password)
        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(40, 370, 231, 21))
        self.label_16.setStyleSheet(u"font: 15pt \".AppleSystemUIFont\";\n"
"")
        self.signup_btn = QPushButton(self.frame_2)
        self.signup_btn.setObjectName(u"signup_btn")
        self.signup_btn.setGeometry(QRect(120, 550, 181, 51))
        self.signup_btn.setStyleSheet(u"font: 18pt \".AppleSystemUIFont\";\n"
"color:#FFF;\n"
"background-color:  #1589FF;")
        self.signup_btn.setFlat(False)
        self.label_13 = QLabel(self.signup_page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(40, 40, 211, 51))
        self.label_13.setPixmap(QPixmap(u":/Images/Static/LogoMakr-80ZEB9.png"))
        self.stackedWidget.addWidget(self.signup_page)
        self.background_image_page1_3.raise_()
        self.login_btn_to_loginpage.raise_()
        self.label_9.raise_()
        self.frame_2.raise_()
        self.label_13.raise_()
        Project.setCentralWidget(self.centralwidget)

        self.retranslateUi(Project)

        self.stackedWidget.setCurrentIndex(0)
        self.login_btn_to_direct.setDefault(False)
        self.signin_btn_to_direct.setDefault(False)
        self.start_now_btn.setDefault(True)
        self.login_btn.setDefault(True)
        self.signup_btn_to_signuppage.setDefault(True)
        self.login_btn_to_loginpage.setDefault(True)
        self.signup_btn.setDefault(True)


        QMetaObject.connectSlotsByName(Project)
    # setupUi

    def retranslateUi(self, Project):
        Project.setWindowTitle(QCoreApplication.translate("Project", u"MainWindow", None))
        self.background_image_page1.setText("")
        self.label.setText("")
        self.login_btn_to_direct.setText(QCoreApplication.translate("Project", u"Connexion", None))
        self.signin_btn_to_direct.setText(QCoreApplication.translate("Project", u"S'inscrire", None))
        self.label_2.setText(QCoreApplication.translate("Project", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Bienvenue sur Code Breaker</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Project", u"<html><head/><body><p>Rejoignez les millions d'apprenants \u00e0 coder </p><p>avec Code Breaker gratuitement</p></body></html>", None))
        self.start_now_btn.setText(QCoreApplication.translate("Project", u"Commencez maintenant", None))
        self.background_image_page1_2.setText("")
        self.label_5.setText("")
        self.label_4.setText(QCoreApplication.translate("Project", u"<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline;\">Connectez-vous \u00e0 Code Breaker</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Project", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Email</span></p><p><span style=\" text-decoration: underline;\"><br/></span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Project", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Password</span></p><p><span style=\" text-decoration: underline;\"><br/></span></p></body></html>", None))
        self.login_btn.setText(QCoreApplication.translate("Project", u"Connexion", None))
        self.label_8.setText(QCoreApplication.translate("Project", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Vous n'avez pas de compte ?</span></p></body></html>", None))
        self.signup_btn_to_signuppage.setText(QCoreApplication.translate("Project", u"S'inscrire", None))
        self.login_btn_to_loginpage.setText(QCoreApplication.translate("Project", u"Connexion", None))
        self.label_9.setText(QCoreApplication.translate("Project", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Vous avez d\u00e9j\u00e0 un compte?</span></p></body></html>", None))
        self.background_image_page1_3.setText("")
        self.label_10.setText(QCoreApplication.translate("Project", u"<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline;\">Inscrivez-vous \u00e0 Code Breaker</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Project", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Nom</span></p><p><span style=\" text-decoration: underline;\"><br/></span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Project", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Prenom</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("Project", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Email</span></p><p><span style=\" text-decoration: underline;\"><br/></span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("Project", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Confirmez le mot de passe</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("Project", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Mot de passe</span></p></body></html>", None))
        self.signup_btn.setText(QCoreApplication.translate("Project", u"S'inscrire", None))
        self.label_13.setText("")
    # retranslateUi

