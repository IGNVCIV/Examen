#[Examen - Javiera Aguilar]
import random
import csv

def SalarioAleatorio():
    Salarios = {Trabajadores:random.randint(300000,2500000) for Trabajadores in Trabajadores} #Lee mejor la prueba xd /Comentario Resuelto
    print("* Se han asignado los sueldos * \n[!] Recuerde que los sueldos fueron asignados de manera aleatoria entre un rango de $300.000 y $2.500.000.-")
    for trabajador,Salarios in Salarios.items():
        print(f"{trabajador} =   ${Salarios}")
    return Salarios

def ClasificarSalarios(Salarios):
    Clasificación = {"Sueldos menores a $800.000":[], 
                     "Sueldos entre $800.000 y $2.000.000":[],
                     "Sueldos superiores a $2.000.000":[]}
    for trabajador, Salarios in Salarios.items():
        if Salarios < 800000:
            Clasificación["Sueldos menores a $800.000"].append((trabajador, Salarios))
        elif Salarios < 2000000:
            Clasificación["Sueldos entre $800.000 y $2.000.000"].append((trabajador, Salarios))
        else:
            Clasificación ["Sueldos superiores a $2.000.000"].append((trabajador, Salarios))
    print("[Clasificación de Sueldos - EMPRESA MANTARRAYACORP]")
    for categoria, trabajadores in Clasificación.items():
        print(f"{categoria} - Total:{len(trabajadores)}")
        for trabajadores, Salarios in trabajadores:
            print(f"{trabajadores} = {Salarios}")
            print()
            print(f"Total Salarios: {sum(Salarios.values())}")
def ReporteSalarios(Salarios):
    with open('Sueldos.csv','a',newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv, delimiter=";")
        escritor_csv.writerow(['Nombre Trabajador ','Salario Bruto($) ','Descuento Salud ','Descuento AFP ','Salario Líquido($) '])

Trabajadores = ["Juan Pérez",
                "María García",
                "Carlos López",
                "Ana Martínez",
                "Pedro Rodríguez",
                "Laura Hernández",
                "Miguel Sánchez",
                "Isabel Gómez",
                "Francisco Díaz",
                "Elena Fernández"]
Salarios = {} 

while True:
    try:
        print("""[EMPRESA MANTARRAYACORP - SUELDOS DE LA EMPRESA]
              \r 1. Asignar sueldos
              \r 2. Clasificar Sueldos
              \r 3. Ver Estadistica
              \r 4. Reporte de Sueldos
              \r 5. Salir del Programa
              """)
        opción = input ("\n -> Ingrese la opción que desee: ")
        assert opción in ("1","2","3","4","5"), "Opción Invalida"
        if opción == "1":
            print("[Ha seleccionado Asignación de Sueldos]\n")
            SalarioAleatorio()
        elif opción == "2":
            print("[Ha seleccionado Clasificar Sueldos]\n")
            ClasificarSalarios()
        elif opción == "3":
            print("[Ha seleccionado Ver Estadistica]\n")
        elif opción == "4":
            print("[Ha seleccionado Reporte de Sueldos]\n")
            ReporteSalarios(Salarios)
        elif opción == "5":
            print("\n Saliendo del Programa...")
    except AssertionError as e:
        print(f"\n [!] ERROR: {e} \n Por favor, Vuelva a intentarlo.\n")
    except KeyboardInterrupt:
        print("\n [Programa interrumpido por un atajo de teclado.]")
