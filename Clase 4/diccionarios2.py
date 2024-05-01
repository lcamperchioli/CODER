from pprint import pprint
base_de_datos = {
    "articulos": {
        "sal": 10.5,
        "pan": 20.0,
        "leche": 25.5,
        "vino": 100,
    },
    "proveedor":{
        1: "Sociedad La Estancia",
        2: "Sociedad El buen vino",
    },
}

precio_articulo = base_de_datos["articulos"]["sal"]
pprint(precio_articulo)

# Aumento el precio de la sal 
precio = input("Ingresa el porcentaje de aumento en la sal")
base_de_datos["articulos"]["sal"] *= (1 + (precio/100))
pprint(base_de_datos)

nuevos_productos = {"sal fina": 10.5, "pan lactal": 20.0, "leche en polvo": 25.5, "vino blanco": 100}
base_de_datos["articulos"].update(nuevos_productos)
pprint(base_de_datos)

ultimo_proveedor = len(base_de_datos["proveedores"])
print(ultimo_proveedor)

nuevo_proveedor = input("Ingrese el nuevo proveedor")
base_de_datos["proveedores"][ultimo_proveedor + 1] = nuevo_proveedor

pprint(base_de_datos["proveedores"])


