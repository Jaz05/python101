'''
Created on 13/10/2016

@author: javier_zardain
'''
import smtplib
import email.mime.multipart
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def traerEmail():
    em = email()
    em.configurarMail(input("Ingrese su cuenta gmail: "), input("Ingrese su password: "))
    return em

def enviarMails(lista):
        email =  traerEmail()
        resultados = {}
        for contacto in lista:
            resultados[contacto.email] = "SENT" if email.enviarMail(contacto.email) else "NOT SENT"
        print (resultados)

class email:
    
    def configurarMail(self,remitente, ps):
        self.fromaddr = remitente
        self.password = ps
    
    def enviarMail(self,destinatario):
        try:
            toaddr = destinatario
            msg = MIMEMultipart()
            msg['From'] = self.fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "Mensaje de prueba"
            body = "Mensaje de prueba"
            msg.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.fromaddr, self.password)
            text = msg.as_string()
            server.sendmail(self.fromaddr, toaddr, text)
            server.quit()
            return True
        except Exception as ex:
            print(ex)
            return False