'''
Created on Sep 10, 2016

@author: python

- Nos piden que la agenda pueda darme un conjunto de contactos que nacieron despues de cierta fecha (ej 1993).
- La agenda puede buscar contactos por iniciales y devolver los resultados posibles.
'''
# -*- coding: utf-8 -*-

import Contacto
from AgendaContactosModulo import AgendaContactos

class MiClase:
    if __name__ == "__main__":
        agenda = AgendaContactos()
        
        while(True):
            print("1-Agregar Contacto")
            print("2-Editar Contacto")
            print("3-Borrar Contacto")
            print("4-Mostrar Contactos")
            print("5-Mostrar Contacto despues de:")
            print("6-Buscar por iniciales")
            print("7-Enviar mail")
            print("8-Enviar mail despues de 1993")
            print("9-Edad de los contactos despues de 10 years")
            print("10-Cargar contactos de archivo txt")
            opcion =int(input("Ingrese una opcion: "))
            if(opcion == 1):
                agenda.agregarContacto()
            if(opcion == 2):
                agenda.editarContacto()
            if(opcion == 3):
                agenda.borrarContacto()
            if(opcion == 4):
                agenda.mostrarContactos()
            if(opcion == 5):
                agenda.mostrarContactosDespuesDe()
            if(opcion == 6):
                agenda.buscarPorIniciales()  
            if(opcion == 7):
                agenda.enviarMail()
            if(opcion == 8):
                agenda.enviarMailsDespuesDe()
            if(opcion == 9):
                agenda.edadDespuesDe10()
            if(opcion == 10):
                agenda.cargarDeArchivoTxt()
# QuA  si lo ponemos  "MiClase" debajo del main e intentamos correr
#¿Cómo podemos resolverlo?