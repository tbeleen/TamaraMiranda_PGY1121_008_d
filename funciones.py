import os
import time 
import msvcrt
import numpy

evento = numpy.zeros((10,10), int)

lista_filas =    []
lista_columnas = []
lista_ruts =     []
lista_cant_entradas = []

acum_cant_entrada_pla = 0
acum_cant_entrada_gold = 0
acum_cant_entrada_sil = 0
acumulador_pla = 0
acumulador_gold = 0
acumulador_sil = 0
acum_total = 0
acum_total_entradas = 0

def mostrar_menu():
    os.system('cls')
    print("""MENÚ
    1. Comprar entradas
    2. Mostrar ubicaciones disponibles
    3. Ver listado de asistente
    4. Mostrar ganancias totales
    5. Salir""")

def opcion_menu():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion in(1,2,3,4,5):
                return opcion
            else:
                print("Debe ingresar una opción entre 1 y 5!")
        except:
            print("ERROR! debe ingresar un número entero")

def cantidad_entrada():
    while True:
        try:
            cantidad = int(input("Ingrese cantidad de entradas(max 3): "))
            if cantidad >=1 and cantidad<=3:
                return cantidad
            else:
                print("Debe seleccionar como maximo 3 entradas!")
        except:
            print("ERROR! debe ingresar un número entero!")

def escenario():
    print("          __________________________")
    print("         |                          |")
    print("         |       ESCENARIO          |")
    print("         |                          |")
    print("          --------------------------")
    for x in range(10):
        print(f"Fila {x+1}:   ", end=" ")
        for y in range(10):
            print(evento[x][y], end=" ")
        print()
    print("columna :  1 2 3 4 5 6 7 8 9 10")

def validar_fila():
    while True:
        try:
            fila = int(input("Ingrese fila: "))
            if fila >= 1 and fila <= 10:
                return fila
            else:
                print("Debe ingresar un valor del 1 al 10")
        except:
            print("ERROR!debe ingresar un número entero")

def validar_columna():
    while True:
        try:
            columna = int(input("Ingrese columna: "))
            if columna >= 1 and columna <= 10:
                return columna
            else:
                print("Debe ingresar un valor del 1 al 10")
        except:
            print("ERROR!debe ingresar un número entero")

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni n°veridicador): " ) )
            if rut>=1000000 and rut <= 99999999:
                return rut
            else:
                print("Rut no debe tener puntos ni dígito verificador!")
        except:
            print("ERROR! debe ingresar un número entero")

def precios():
    print("""PRECIOS
    Platinum  $120.000 (Asientos fila 1 y 2)
    Gold      $80.000  (Asientos fila 3,4 y 5)
    Silver    $50.000  (Asientos fila 6,7,8,9 y 10)""")

def comprar_entrada():
    os.system('cls')
    cant_entrada = cantidad_entrada()
    escenario()
    precios()
    fila = validar_fila()
    columna = validar_columna()
    if lista_cant_entradas ==1 or lista_cant_entradas ==2 or lista_cant_entradas ==3  and fila in(1,2):
       acum_cant_entrada_pla = acum_cant_entrada_pla + lista_cant_entradas
    elif lista_cant_entradas == 1 or lista_cant_entradas ==2 or lista_cant_entradas ==3 and fila in(2,4,5):
        acum_cant_entrada_gold = acum_cant_entrada_gold + lista_cant_entradas
    elif lista_cant_entradas == 1 or lista_cant_entradas ==2 or lista_cant_entradas ==3 and fila in(6,7,8,9,10):
        acum_cant_entrada_sil = acum_cant_entrada_sil + lista_cant_entradas

    if fila in(1,2):
        acumulador_pla = acumulador_pla + 120000*acum_cant_entrada_pla
    elif fila in(3,4,5):
        acumulador_gold = acumulador_gold + 80000*acum_cant_entrada_gold
    else:
        acumulador_sil = acumulador_sil + 50000*acum_cant_entrada_sil

    rut = validar_rut()
    if rut in lista_ruts:
        print("RUT YA EXISTE!")

    if evento[fila-1][columna-1]==0:
        evento[fila-1][columna-1]=1
        lista_ruts.append(rut)
        lista_filas.append(fila)
        lista_columnas.append(columna)
        lista_cant_entradas.append(cant_entrada)

    else:
        print("Asiento ocupado! seleccione otro!")
    print("LA COMPRA DE ENTRADAS FUE REALIZADA CORRECTAMENTE!")
    time.sleep(3)  

def ubicaciones_disp():
    escenario()
    print("Presione una tecla para continuar...")
    msvcrt.getch()

def ver_asientos():
    print("Lista de rut",lista_ruts)
    lista_ruts.sort
    print("PRESIONE UNA TECLA PARA CONTINUAR...")
    msvcrt.getch()

def ganancias_totales():
    acum_total = acumulador_pla + acumulador_gold + acumulador_sil
    acum_total_entradas = acum_cant_entrada_pla + acum_cant_entrada_gold + acum_cant_entrada_sil

    print(f"""
    TIPO ENTRADA           CANTIDAD                       TOTAL
    -----------------------------------------------------------------
    Platinum $120.000  {acum_cant_entrada_pla}       {acum_cant_entrada_pla}
    -----------------------------------------------------------------
    Gold    $80.000    {acum_cant_entrada_gold}      {acum_cant_entrada_gold}
    -----------------------------------------------------------------
    Silver  $50.000    {acum_cant_entrada_sil}       {acum_cant_entrada_sil}
    -----------------------------------------------------------------
    Total             {acum_total_entradas}          {acum_total}     """)


    
def salir():
    print("Gracias por visitaros!")
    time.sleep(3)
    





    
        
    