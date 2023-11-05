#import de los módulos "os" y "time" para limpiar la pantalla y hacer un sleep
import os
import time

#Clase Divisiones
class Divisiones:
    CodDivision = str
    NombreDivision = str
    UrlDivision = str
#Constructor clase Divisiones
    def __init__(self, CodDivision, NombreDivision, UrlDivision):
        self.CodDivision = CodDivision
        self.NombreDivision = NombreDivision
        self.UrlDivision = UrlDivision
#Método para mostrar la información de la clase Divisiones
    def InfoDivision(self):
        return "\
    *** Info Division/es ***\n\
    Código Division: {0} \n\
    Nombre: {1} \n\
    Url: {2} \n\
    ******************************".format(self.CodDivision, self.NombreDivision, self.UrlDivision)

#Clase Entrenadores
class Entrenadores:
    CodEntrenador = str
    Nombre = str
    Correo = str
#Constructor clase Entrenadores
    def __init__(self, CodEntrenador, Nombre, Correo):
        self.CodEntrenador = CodEntrenador
        self.Nombre = Nombre
        self.Correo = Correo
#Método para mostrar la información de la clase Entrenadores
    def InfoEntrenador(self):
        return "\
    *** Info Entrenador/es ***\n\
    Código Entrenador: {0} \n\
    Nombre: {1} \n\
    Correo: {2} \n\
    ******************************".format(self.CodEntrenador, self.Nombre, self.Correo)

#Clase Clubes
class Clubes:
    CodClub = str
    NombreClub = str
    CodDivision = Divisiones
    Comuna = str
    FechaFundación = int
    CodEntrenador = Entrenadores
#Constructor clase Clubes
    def __init__(self, CodClub, NombreClub, CodDivision, Comuna, FechaFundación, CodEntrenador):
        self.CodClub = CodClub
        self.NombreClub = NombreClub
        self.CodDivision = CodDivision
        self.Comuna = Comuna
        self.FechaFundación = FechaFundación
        self.CodEntrenador = CodEntrenador
#Método para mostrar la información de la clase Clubes
    def InfoClub(self):
        return "\
    *** Info Club/es ***\n\
    Código Club: {0} \n\
    Nombre: {1} \n\
    Código División: {2} \n\
    Comuna: {3} \n\
    Año Fundación: {4} \n\
    Código Entrenador: {5} \n\
    ******************************".format(self.CodClub, self.NombreClub, self.CodDivision, self.Comuna, self.FechaFundación, self.CodEntrenador)
#Listas
listaDivisiones = []
listaEntrenadores = []
listaClubes = []
#Menú
def menu():
    print("1. Registrar Divisiones")
    print("2. Registrar Entrenadores")
    print("3. Registrar Clubes")
    print("4. Listar Divisiones")
    print("5. Listar Entrenadores")
    print("6. Listar Clubes")
    print("7. Salir")
#Función para ingresar datos de la clase Divisiones
def ingresarDivision():
    print("Ingrese los datos de la división")
    CodDivision = input("Ingrese el código de la división: ")
    NombreDivision = input("Ingrese el nombre de la división: ")
    UrlDivision = input("Ingrese la url de la división: ")
    division = Divisiones(CodDivision, NombreDivision, UrlDivision)
    listaDivisiones.append(division)
    print("¡División ingresada correctamente!")
    time.sleep(1)
    os.system("cls")
#Función para ingresar datos de la clase Entrenadores
def ingresarEntrenador():
    print("Ingrese los datos del entrenador")
    CodEntrenador = input("Ingrese el código del entrenador: ")
    Nombre = input("Ingrese el nombre del entrenador: ")
    Correo = input("Ingrese el correo del entrenador: ")
    entrenador = Entrenadores(CodEntrenador, Nombre, Correo)
    listaEntrenadores.append(entrenador)
    print("¡Entrenador ingresado correctamente!")
    time.sleep(1)
    os.system("cls")
#Función para ingresar datos de la clase Clubes
def ingresarClub():
    print("Ingrese los datos del club")
    CodClub = input("Ingrese el código del club: ")
    NombreClub = input("Ingrese el nombre del club: ")
    for division in listaDivisiones:
        print(division.InfoDivision())
    CodDivision = input("Ingrese el código de la división: ")
    Comuna = input("Ingrese la comuna del club: ")
    FechaFundación = input("Ingrese el año de fundación del club: ")
    for entrenador in listaEntrenadores:
        print(entrenador.InfoEntrenador())
    CodEntrenador = input("Ingrese el código del entrenador: ")
    club = Clubes(CodClub, NombreClub, CodDivision, Comuna, FechaFundación, CodEntrenador)
    listaClubes.append(club)
    print("¡Club ingresado correctamente!")
    time.sleep(1)
    os.system("cls")
#Función para mostrar datos de la clase Divisiones
def mostrarDivision():
    os.system("cls")
    for division in listaDivisiones:
        print(division.InfoDivision())
#Función para mostrar datos de la clase Entrenadores
def mostrarEntrenador():
    os.system("cls")
    for entrenador in listaEntrenadores:
        print(entrenador.InfoEntrenador())
#Función para mostrar datos de la clase Clubes, además de mostrar los datos de las clases Divisiones y Entrenadores
def mostrarClub():
    os.system("cls")
    for club in listaClubes:
        print(club.InfoClub())
        for division in listaDivisiones:
            if club.CodDivision == division.CodDivision:
                print(division.InfoDivision())
        for entrenador in listaEntrenadores:
            if club.CodEntrenador == entrenador.CodEntrenador:
                print(entrenador.InfoEntrenador())

#Variable para el menú
option=0
#While para mostrar el menú y las opciones
while True:
    menu()
    option = input("Ingrese una opción: ")
    if option == "1":
        ingresarDivision()
    elif option == "2":
        ingresarEntrenador()
    elif option == "3":
        ingresarClub()
    elif option == "4":
        mostrarDivision()
    elif option == "5":
        mostrarEntrenador()
    elif option == "6":
        mostrarClub()
    elif option == "7":
        break
    else:
        print("Opción no válida")
#Mensaje de despedida
print("Fin del programa")
