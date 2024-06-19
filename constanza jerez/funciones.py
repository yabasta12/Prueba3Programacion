import csv

PAQUETES=["pequeño", "mediano", "grande"]
SECTORES=["centro","norte","sur"]

def registrar_pedido(paquete):
    nombre=input("ingrese su nombre y apellido:")
    while True:
        if " " in nombre:
            break
        else:
            print("ingrese su nombre y apellido por favor\n")
            return

    direccion= input("ingrese su dirección:")
    if direccion =="":
        print("por favor, ingrese su dirección")
        return
    sector=("ingrese el sector de su vivienda (Centro/Norte/Sur)").lower
    while sector not in SECTORES:
        print("sector no válido, por favor vuelva a ingresarlo")
        sector=("ingrese el sector de su vivienda (Centro/Norte/Sur)").lower
    detallePedi=input("ingrese el detalle de su pedido (pequeño/mediano/grande)").lower()
    while detallePedi not in PAQUETES:
        print("detalle no válido, por favor vuelva a ingresarlo ")
        detallePedi=input("ingrese el detalle de su pedido (pequeño/mediano/grande)").lower()

    paquete.append({
        "nombre":nombre,
        "direccion":direccion,
        "sector":sector,
        "detallePedi": detallePedi
    })
    

def listar_pedido(paquete):
    print("LISTA DE PEDIDOS")
    print("****************")
    for package in paquete:
        print(package)

def imprimir_pedido (paquete):
    ruta=input("ingrese la ruta que desea ver (centro/norte/sur), si desea ver todas las rutas presione ENTER").lower()
    if ruta=="":
        ruta_paquetes= paquete
        nombreArchivo= "ruta_completa.txt"
    elif ruta in SECTORES:
        ruta_paquetes=[]
        for Sector in SECTORES:
            if Sector["sector"] == ruta:
                ruta_paquetes.append (Sector)
        nombreArchivo =f"ruta_{ruta}.txt"

    else:
        print("ruta no válida")
        return
    
    # with open (nombreArchivo,"w") as archivo:
    #     for package in paquete: 
    #         archivo({
    #             "nombre": 
    #         })