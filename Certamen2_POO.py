#import os para limpiar pantalla
import os

    #Definición de clases


#Clase Divisiones
class Divisiones:
    CodDivision = str
    NombreDivision = str
    UrlDivision = str

    def __init__(self, CodDivision, NombreDivision, UrlDivision):
        self.CodDivision = CodDivision
        self.NombreDivision = NombreDivision
        self.UrlDivision = UrlDivision

    def InfoDivision(self):
        return "\
    *** Info Division ***\n\
    Código Division: {0} \n\
    Nombre: {1} \n\
    Url: {2} \n\
    ******************************".format(self.CodDivision, self.NombreDivision, self.UrlDivision)


#Clase Entrenadores
class Entrenadores:
    CodEntrenador = str
    Nombre = str
    Correo = str

    def __init__(self, CodEntrenador, Nombre, Correo):
        self.CodEntrenador = CodEntrenador
        self.Nombre = Nombre
        self.Correo = Correo

    def InfoEntrenador(self):
        return "\
    *** Info Entrenador ***\n\
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

    def __init__(self, CodClub, NombreClub, CodDivision, Comuna, FechaFundación, CodEntrenador):
        self.CodClub = CodClub
        self.NombreClub = NombreClub
        self.CodDivision = CodDivision
        self.Comuna = Comuna
        self.FechaFundación = FechaFundación
        self.CodEntrenador = CodEntrenador

    def InfoClub(self):
        return "\
    *** Info Club ***\n\
    Código Club: {0} \n\
    Nombre: {1} \n\
    Código División: {2} \n\
    Comuna: {3} \n\
    Año Fundación: {4} \n\
    Código Entrenador: {5} \n\
    ******************************".format(self.CodClub, self.NombreClub, self.CodDivision, self.Comuna, self.FechaFundación, self.CodEntrenador)



#Listas
ListaDivisiones = []
ListaEntrenador = []
ListaClubes = []



    #MENÚ
while True:
#Menú de opciones
    Opción = 0
    print("\t ****** Menú ****** \n \
        1. Agregar Division \n \
        2. Agregar Entrenador \n \
        3. Agregar Club \n \
        4. Listar Divisiones \n \
        5. Listar Entrenadores \n \
        6. Listar Clubes \n \
        7. Salir")



#Validación de opción
    while(not(Opción >= 1 and Opción <= 7)):
        Opción = int(input("Ingrese una opción: "))
        if Opción >= 1 and Opción <= 7:
            break
        else:
            print("Ingrese una opción válida")



    #Opciones
#Agregar Division
    if Opción == 1:
        CodDivision = input("Ingrese el código de la división: ")
        NombreDivision = input("Ingrese el nombre de la división: ")
        UrlDivision = input("Ingrese la url de la división: ")
        Division = Divisiones(CodDivision, NombreDivision, UrlDivision)
        ListaDivisiones.append(Division)
        os.system("cls")



#Agregar Entrenador
    elif Opción == 2:
        CodEntrenador = input("Ingrese el código del entrenador: ")
        Nombre = input("Ingrese el nombre del entrenador: ")
        Correo = input("Ingrese el correo del entrenador: ")
        Entrenador = Entrenadores(CodEntrenador, Nombre, Correo)
        ListaEntrenador.append(Entrenador)
        os.system("cls")



#Agregar Club
    elif Opción == 3:
        CodClub = input("Ingrese el código del club: ")
        NombreClub = input("Ingrese el nombre del club: ")
        for Division in ListaDivisiones:
            print(Division.InfoDivision())
        CodDivision = input("Ingrese el código de la división: ")
        Comuna = input("Ingrese la comuna del club: ")
        FechaFundación = int(input("Ingrese el año de fundación del club: "))
        for Entrenador in ListaEntrenador:
            print(Entrenador.InfoEntrenador())
        CodEntrenador = input("Ingrese el código del entrenador: ")
        Club = Clubes(CodClub, NombreClub, CodDivision, Comuna, FechaFundación, CodEntrenador)
        ListaClubes.append(Club)
        os.system("cls")



#Listar Divisiones
    elif Opción == 4:
        for Division in ListaDivisiones:
            print(Division.InfoDivision())
        print("")



#Listar Entrenadores
    elif Opción == 5:
        for Entrenador in ListaEntrenador:
            print(Entrenador.InfoEntrenador())
        print("")



#Listar Clubes
    elif Opción == 6:
        for Club in ListaClubes:
            print(Club.InfoClub())
        print("")



#Salir
    elif Opción == 7:
        print("¡Adios!")
        break


