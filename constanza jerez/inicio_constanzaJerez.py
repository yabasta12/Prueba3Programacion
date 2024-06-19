import funciones as fn

paquete= []

while True:
    print("bienvenido a PaquExpress")
    print("************************")
    print("1. Registrar pedido")
    print("2. Listar pedidos")
    print("3. Imprimir ruta")
    print("4. salir")
    print("************************")
    opcion =int(input("ingrese su opción..."))

    if opcion ==1:
        fn.registrar_pedido(paquete)
    elif opcion ==2:
        fn.listar_pedido(paquete)
    elif opcion ==3 :
        fn.imprimir_pedido(paquete)
    elif opcion ==4:
        print("muchas gracias por confiar en nosotros")
        break
    else:
        print("opcion no valida")
        