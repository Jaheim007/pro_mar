from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from Widget.project_march import Ui_Project
import sqlite3
import smtplib
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
import re
import requests

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

class Project(QMainWindow, Ui_Project):
    count = 0
    
    def __init__(self):    
        super().__init__()
        self.setupUi(self)
#Here I did the scraping with all of the informations       
        global html_text
        global css_text
        global javascript
        global python_re
        global php
        global flutter
        
        url_html = 'https://developer.mozilla.org/fr/docs/Web/HTML'
        url_css = 'https://developer.mozilla.org/fr/docs/Web/CSS'
        url_javascript = 'https://developer.mozilla.org/fr/docs/Web/JavaScript'
        url_python = 'https://python.doctor/'
        url_php = 'https://www.commentcamarche.net/contents/1351-php-introduction'
        url_flutter = 'https://www.didierboelens.com/fr/2018/04/flutter-introduction/#:~:text=Flutter%20offre%20un%20moyen%20de,natif%20pour%20iOS%20et%20Android.'
        
        source = requests.get(url_html).text
        source1 = requests.get(url_css).text
        source2 = requests.get(url_javascript).text
        source3 = requests.get(url_python).text
        source4 = requests.get(url_php).text
        source5= requests.get(url_flutter).text

        soup_html = BeautifulSoup(source, "lxml")
        soup_css = BeautifulSoup(source1, "lxml")
        soup_javascript = BeautifulSoup(source2, "lxml")
        soup_python = BeautifulSoup(source3, "lxml")
        soup_php = BeautifulSoup(source4, "lxml")
        soup_flutter = BeautifulSoup(source5, "lxml")
        
        
        html_text = soup_html.find('article', class_="main-page-content")
        css_text = soup_css.find('article', class_ = "main-page-content")
        javascript = soup_javascript.find('article', class_= "main-page-content")
        python_re = soup_python.find('div', id= "page")
        php = soup_php.find('div', class_= "typo_content typo_content--img")
        flutter = soup_flutter.find('div', class_= "content main-content-wrap post-content")
    
           
#These are the different btn and their different functions
        self.start_now_btn.clicked.connect(self.started)
        self.login_btn_to_direct.clicked.connect(self.loginpage)
        self.signin_btn_to_direct.clicked.connect(self.signuppage) 
        self.login_btn_to_loginpage.clicked.connect(self.login_within)
        self.signup_btn_to_signuppage.clicked.connect(self.signup_within)

#The different functions
        self.signup_btn.clicked.connect(self.save_in_database)
        self.login_btn.clicked.connect(self.verify)
        self.profile.clicked.connect(self.hide_show)
        self.disconnected.clicked.connect(self.disconnect)
        self.html_btn.clicked.connect(self.scrap_html)
        self.css_btn.clicked.connect(self.scrap_css)
        self.javascript_btn.clicked.connect(self.scrap_javascript)
        self.python_btn.clicked.connect(self.scrap_python)
        self.php_btn.clicked.connect(self.scrap_php)
        self.flutter_btn.clicked.connect(self.scrap_flutter)
        self.search_btn.clicked.connect(self.search_html)
        self.code2.clicked.connect(self.return_home)
        self.code3.clicked.connect(self.return_home2)
        self.code4.clicked.connect(self.clear_items)
        
#to hide the frame 
        self.profile_result.hide()


#The Get Started btn in the center which is supposed to send me to the sign-up page. 
    def started(self):
        self.stackedWidget.setCurrentWidget(self.signup_page)
        self.show()


#The login btn which is the and is supposed to send me directly to the login page.             
    def loginpage(self):    
        self.stackedWidget.setCurrentWidget(self.login_page)
        self.show()

#The sign btn from the home page to the sign up page.   
    def signuppage(self):
        self.stackedWidget.setCurrentWidget(self.signup_page)
        self.show()
 
#the login btn in the sign up page  
    def login_within(self):     
        self.stackedWidget.setCurrentWidget(self.login_page)
        self.show()

#the sign up page btn in the log in page 
    def signup_within(self):     
        self.stackedWidget.setCurrentWidget(self.signup_page)
        self.show()

#Creating the DataBase  
    def save_in_database(self):
       
        conn = sqlite3.connect("Database.db")
        
        user_info = {
            "username" : self.username_sign.text(),
            "nom": self.nom_line.text(),
            "prenom": self.prenom_line.text(),
            "email": self.sign_email_line.text(),
            "password": self.sign_password_line.text(),
            "confirm_password": self.confirm_password.text()
        }
        
        if self.nom_line.text() == "" or self.prenom_line.text() =="" or self.sign_email_line.text() =="" or self.sign_password_line.text() =="" or self.confirm_password.text() == "" or self.username_sign.text() == "" : 
            QMessageBox.warning(self, "Error", "Veuillez saisir les différents champs")
        
        elif self.confirm_password.text() != self.sign_password_line.text():  
            QMessageBox.warning(self, "Error", "Vos mots de passe ne correspondent pas")
        
        elif self.confirm_password.text() == self.sign_password_line.text():  
            if (re.fullmatch(regex, self.sign_email_line.text())):  
                con = conn.cursor()
                con.execute("""CREATE TABLE IF NOT EXISTS Userdata(
                                username text,
                                nom text,
                                prenom text,
                                email text,
                                password text
                            )""") 
                con.execute("INSERT INTO Userdata VALUES(:username , :nom, :prenom, :email, :password)", user_info)
   
                conn.commit()
                conn.close()
            
                title = "Code Breaker"
                msg_content = "<h2> Merci d'avoir créé un compte avec Code Breaker, votre adresse e-mail a été vérifiée.</font></h2>\n".format(title = title)
                message = MIMEText(msg_content, 'html')
                message['From'] = 'Jaheim Kouaho <jaheimkouaho@gmail.com>'
                message['Subject'] = "Code Breaker"
                msg_full = message.as_string()
                
                sever = smtplib.SMTP('smtp.gmail.com:587')
                sever.starttls()
                sever.login('jaheimkouaho@gmail.com', 'vketfheffijdklkx')
                sever.sendmail('jaheimkouaho@gmail.com', [self.sign_email_line.text()], msg_full)
                sever.quit()
                
                self.username_sign.clear()
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
                
#to verify the connection page            
    def verify(self): 
        try:
            open = sqlite3.connect('Database.db')
            cur = open.cursor()
            com = open.execute("SELECT * FROM Userdata where username = ? AND email = ? AND password = ? ",(self.username_login.text() ,self.email_line.text(), self.password_line.text())) 
            don = com.fetchone() 
              
        except sqlite3.OperationalError:
            QMessageBox.warning(self, "Error", "Cet utilisateur n'a pas été enregistré")   
            
        else:
            if don:
                QMessageBox.information(self, "Info", "Vous êtes connecté")
                self.stackedWidget.setCurrentWidget(self.home_page)
        
            else:
                QMessageBox.warning(self, "Error", "Cet utilisateur n'a pas été enregistré")
        
#To hide frame containing user information   
    def hide_show(self):
        
        if Project.count % 2 == 0: 
            self.profile_result.show()
            self.label_15.setText(self.username_login.text())
            self.label_12.setText(self.email_line.text())  
        
        else:   
            self.profile_result.hide()
        Project.count += 1

#Leave the application        
    def disconnect(self):
        QApplication.quit()

#The textbrowser of HTML        
    def scrap_html(self):
        self.search_bar.clear()     
        self.textBrowser.setText(str(html_text.text))  

#The textbroswer of CSS        
    def scrap_css(self):
        self.search_bar.clear()  
        self.textBrowser.setText(str(css_text.text))

#The textbroswer of JavaScript      
    def scrap_javascript(self):   
        self.search_bar.clear()  
        self.textBrowser.setText(str(javascript.text)) 

#The textbroswer of Python
    def scrap_python(self):
        self.search_bar.clear()  
        self.textBrowser.setText(str(python_re.text))

#The Textbrowser of PHP    
    def scrap_php(self):
        self.search_bar.clear()  
        self.textBrowser.setText(str(php.text))

#The textbrowser of Flutter
    def scrap_flutter(self):
        self.search_bar.clear()  
        self.textBrowser.setText(str(flutter.text))

#Search BAR Results html, css, php, javascript, flutter and python        
    def search_html(self):  
       
        text = self.search_bar.text().lower()
        
        if text == "html" :
            self.textBrowser.setText(str(html_text.text))
            
        elif text ==  "css":     
            self.textBrowser.setText(str(css_text.text))
          
        
        elif text == "javascript":     
            self.textBrowser.setText(str(javascript.text)) 
            
        
        elif text == "python":       
            self.textBrowser.setText(str(python_re.text))
            
        
        elif text ==  "php":     
            self.textBrowser.setText(str(php.text))
       
            
        elif text == "flutter" :     
            self.textBrowser.setText(str(flutter.text))
            
        else:  
            self.textBrowser.clear()
            QMessageBox.warning(self, "Error", "Désolé ce langage de programmation n'a pas été enregistré")

#Return to home page by code Breaker button    
    def return_home(self):              
        self.stackedWidget.setCurrentWidget(self.Main_page)
        
    def return_home2(self):     
        self.stackedWidget.setCurrentWidget(self.Main_page)

#Clear items 
    def clear_items(self):      
        self.textBrowser.clear()
        self.search_bar.clear()
        
            

            
        