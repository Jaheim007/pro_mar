from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from Widget.project_march import Ui_Project
import sqlite3
import smtplib
from email.mime.text import MIMEText
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

class Project(QMainWindow, Ui_Project):
    def __init__(self):    
        super().__init__()
        self.setupUi(self)

#These are the different btnand their different functions
        self.start_now_btn.clicked.connect(self.started)
        self.login_btn_to_direct.clicked.connect(self.loginpage)
        self.signin_btn_to_direct.clicked.connect(self.signuppage) 
        self.login_btn_to_loginpage.clicked.connect(self.login_within)
        self.signup_btn_to_signuppage.clicked.connect(self.signup_within)
        self.signup_btn.clicked.connect(self.save_in_database)

#The Get Started btn in the center which is supposed to send me to the sign-up page. 
    def started(self):
        self.stackedWidget.setCurrentWidget(self.signup_page)
        self.show()

#The login btn which is the and is supposed to send me directly to the login page.             
    def loginpage(self):    
        self.stackedWidget.setCurrentWidget(self.login_page)
        self.show()
    
    def signuppage(self):
        self.stackedWidget.setCurrentWidget(self.signup_page)
        self.show()
    
    def login_within(self):     
        self.stackedWidget.setCurrentWidget(self.login_page)
        self.show()

    def signup_within(self):     
        self.stackedWidget.setCurrentWidget(self.signup_page)
        self.show()
    
    def save_in_database(self):
        conn = sqlite3.connect("Database.db")
        
        user_info = {
            "nom": self.nom_line.text(),
            "prenom": self.prenom_line.text(),
            "email": self.sign_email_line.text(),
            "password": self.sign_password_line.text(),
            "confirm_password": self.confirm_password.text()
        }
        
        if self.nom_line.text() == "" or self.prenom_line.text() =="" or self.sign_email_line.text() =="" or self.sign_password_line.text() =="" or self.confirm_password.text() == "" : 
            QMessageBox.warning(self, "Error", "Veuillez saisir les différents champs")
        
        elif self.confirm_password.text() != self.sign_password_line.text():  
            QMessageBox.warning(self, "Error", "Vos mots de passe ne correspondent pas")
            self.nom_line.clear()
            self.prenom_line.clear()
            self.sign_email_line.clear()
            self.sign_password_line.clear()
            self.confirm_password.clear()
            
        elif self.confirm_password.text() == self.sign_password_line.text():  
            if (re.fullmatch(regex, self.sign_email_line.text())):  
                con = conn.cursor()
                con.execute("""CREATE TABLE IF NOT EXISTS Userdata(
                                nom text,
                                prenom text,
                                email text,
                                password text
                            )""") 
                con.execute("INSERT INTO Userdata VALUES(:nom, :prenom, :email, :password, :confirm_password)", user_info)
   
                
                conn.commit()
                conn.close()
            
                title = "Code Breaker"
                msg_content = "<h2> Merci d'avoir créé un compte avec Code Breaker, votre adresse e-mail a été vérifiée.</font></h2>\n".format(title = title)
                message = MIMEText(msg_content, 'html')
                message['From'] = 'Jaheim Kouaho <jaheimkouaho@gmail.com>'
                # message["To"] = 'Jaheim <jaheimkouaho@gmail.com>'
                message['Subject'] = "Code Breaker"
                msg_full = message.as_string()
                
                sever = smtplib.SMTP('smtp.gmail.com:587')
                sever.starttls()
                sever.login('jaheimkouaho@gmail.com', 'vketfheffijdklkx')
                sever.sendmail('jaheimkouaho@gmail.com', [self.sign_email_line.text()], msg_full)
                sever.quit()
                
                self.nom_line.clear()
                self.prenom_line.clear()
                self.sign_email_line.clear()
                self.sign_password_line.clear()
                self.confirm_password.clear()
                
                QMessageBox.information(self, "Info", "Merci de vous être inscrit à Code Breaker, un message a été envoyé à votre adresse e-mail")
                
                self.stackedWidget.setCurrentWidget(self.login_page)
                self.show()
            
            else: 
                QMessageBox.warning(self, "Error", "Merci de saisir votre adresse email au format : votreexemple@exemple.com")
                self.nom_line.clear()
                self.prenom_line.clear()
                self.sign_email_line.clear()
                self.sign_password_line.clear()
                self.confirm_password.clear()
            
            
        