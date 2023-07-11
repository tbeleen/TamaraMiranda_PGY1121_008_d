import funciones as fn

while True:
    fn.mostrar_menu()
    opcion = fn.opcion_menu()
    if opcion ==1:
        fn.comprar_entrada()
    elif opcion ==2:
        fn.ubicaciones_disp()
    elif opcion ==3:
        fn.ver_asientos()
    elif opcion ==4:
        fn.ganancias_totales()
    else:
        fn.salir()
        break