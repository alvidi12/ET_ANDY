# Analizar los datos de sus trabajadores para generar algunos reportes

from statistics import geometric_mean
import random

#Sueldos aleatorio (entre $300.000 y $2.500.000)
trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
#Menu
print("\nMenu de la aplicacion.\nEscoga sus funciones\n\n1. Asignar sueldos aleatorios\n2. Clasificar sueldos\n3. Ver estadísticas\n4. Reporte de sueldos\n5. Salir del programa\n")
seleccion = int(input("Seleccione una opcion: "))

# Asignar sueldos aleatorios
JuanPérez =random.uniform(30000,2500000)
MaríaGarcía = random.uniform(30000,2500000)
CarlosLópez =random.uniform(30000,2500000)
AnaMartínez =random.uniform(30000,2500000)
PedroRodríguez =random.uniform(30000,2500000)
LauraHernández =random.uniform(30000,2500000)
MiguelSánchez = random.uniform(30000,2500000)
IsabelGómez = random.uniform(30000,2500000)
FranciscoDíaz = random.uniform(30000,2500000)
ElenaFernández =random.uniform(30000,2500000)
def sueldos_aleatorio():
   for i in range(1):
       print(f"Juan Pérez: {JuanPérez:.0f}\nMaría García: {MaríaGarcía:.0f}\nCarlos López: {CarlosLópez:.0f}\nAna Martínez: {AnaMartínez:.0f}\nPedro Rodríguez: {PedroRodríguez:.0f}\nLaura Hernández: {LauraHernández:.0f}\nMiguel Sánchez: {MiguelSánchez:.0f}\nIsabel Gómez: {IsabelGómez:.0f}\nFrancisco Díaz: {FranciscoDíaz:.0f}\nElena Fernández: {ElenaFernández:.0f}")
op1 = sueldos_aleatorio()

"""
Sueldos menores a $800.000 TOTAL: 2
Nombre empleado Sueldo
Juan Pérez $500000
María García $700000
Sueldos entre $800.000 y $2.000.000
TOTAL: 2
Nombre empleado Sueldo
Pedro Soto $1100000
Isabel Gómez $800000
Sueldos superiores a $2.000.000
TOTAL: 1
Nombre empleado Sueldo
Miguel Sánchez $2100000
TOTAL SUELDOS: $ 5200000
"""
# Clasificar sueldos
def clasificar_sueldos():
    for count in JuanPérez, MaríaGarcía, CarlosLópez, AnaMartínez, PedroRodríguez, LauraHernández, MiguelSánchez, IsabelGómez, FranciscoDíaz, ElenaFernández:
        print(f"Sueldos menores a $800.000 TOTAL: {count}")
        print('Nombre empleado Sueldo')
        print('Juan Pérez $500000')
        print('María García $700000')
        print(f'Sueldos entre $800.000 y $2.000.000 TOTAL: {count}')
        print('Nombre empleado Sueldo')
        print('Pedro Soto $1100000')
        print('Isabel Gómez $800000')
        print(f'Sueldos superiores a $2.000.000 TOTAL: {count}')
        print('Nombre empleado Sueldo')
        print('Miguel Sánchez $2100000')
        print("TOTAL SUELDOS: $ 5200000")
op2 = clasificar_sueldos()

"""
3. Ver estadísticas
Crear una función que permita mostrar por pantalla los siguientes datos con respecto a los sueldos:
 Sueldo más alto
 Sueldo más bajo
 Promedio de sueldos
 Media geométrica 
"""
def ver_estadisticas():
    print("")
op3 = ver_estadisticas()

""""
4. Reporte de sueldos
La aplicación deberá poseer una función para mostrar el detalle de los sueldos de los trabajadores, según la siguiente regla de
negocio:
 Descuento salud 7%
 Descuento AFP 12%
 Sueldo líquido calculado en base al sueldo base menos el descuento en salud y menos el descuento afp.
Y mostrarse como en la siguiente tabla de ejemplo:

Nombre empleado Sueldo Base Descuento Salud Descuento AFP Sueldo Líquido
Juan Pérez $1000000 $70000 $120000 $810000
Pedro Soto $800000 $56000 $96000 $648000

Estos datos se deberán exportar a un archivo de texto separado por comas (.csv) para su posterior lectura en otra aplicación.
"""
#Reporte de sueldo
def reporte_sueldo():
#Mostrar y leer el archivo csv
    for fila in leer_archivo_csv('ejemplo.csv'):
        print(fila)
op4 = reporte_sueldo()

#Crear archivo CSV
def crear_archivo_csv(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(datos)
    print(f"Se ha creado el archivo: {nombre_archivo}")


# MENÚ
while True:
    if seleccion == "1":
        print(op1)
    elif seleccion == "2":
        print(op2)
    elif seleccion =="3":
        print(op3)
    elif seleccion == "4":
        print(op4)
    elif seleccion == "5":
        print("Finalizando programa…\nDesarrollado por Andy Villarroel\nRUT 19.540.448-8")
        break








"""

5. Salir del programa
La aplicación deberá finalizar para salir el programa mostrando un mensaje con sus datos

Finalizando programa…
Desarrollado por Carlos Vergara
RUT 12.345.678-9
"""