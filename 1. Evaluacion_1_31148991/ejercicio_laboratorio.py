"""
Jesus Diaz: 0412-5015670

Declarativo (Programacion Orientado)

Listas [] -----> Ordenado Mutable
Tuplas () -----> Ordenadas Inmutables
Diccionario {k:v} -----> No ordenado Mutables, Busqueda 0(1)

def nombre(parametro1,parametro2):
    pass
    return#_ para que me devuelva algoroducto
#print(f" ",end=" ")

Actividad: modelar un inventario de un personaj
Caracterisicas: -espada
                -pocion
                -escudo
                
"""

inventario= {
    "espada": {
        'precio':40,
        'tipo':'arma'
    },

    "pocion": {
        'precio':10,
        'tipo':'consumible'
    },
    "escudo": {
        'precio':20,
        'tipo':'defensa'
    },
}

def filtro_inventario(precio):
    productos_filtrados=[]
    for productos,contenido in inventario.items():
        for clave,valor in contenido.items():
            if clave=='precio' and valor <= precio:
                productos_filtrados.append(productos)
                
    
    return productos_filtrados
    
precio=int(input("Cantidad de dinero del jugador: "))
precio_filtrados = filtro_inventario(precio)#Rafael Zerpa


if precio_filtrados:
    print(precio_filtrados)
else:
    print("Dinero insuficiente")