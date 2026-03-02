"""
Rafael Zerpa, 31148991

4. Sistema de Inventario Pro (RPG)
Contexto: Un personaje de un videojuego debe gestionar una mochila con espacio limitado. A
diferencia de un inventario simple, aquí los objetos tienen peso y rareza.
● Misión: Crear el TDA Item (nombre, peso, rareza) y el TDA Inventario
(capacidad_maxima).
● Lógica: El inventario debe usar un diccionario para agrupar ítems repetidos y una lista
para el orden de obtención. El método agregar_item() debe verificar que el pes
"""

class Item:
    def __init__(self, nombre, peso, rareza):
        self.nombre = nombre
        self.peso = peso
        self.rareza = rareza

    def __str__(self):
        return f"{self.nombre} ({self.rareza}) - {self.peso}kg"

class Inventario:
    def __init__(self, capacidad_maxima):
        self.capacidad_maxima = capacidad_maxima
        self.lista_items = []
        self.conteo_items = {}
    
    def calcular_peso_actual(self):
        peso_total = 0
        for item in self.lista_items:
            peso_total = peso_total + item.peso
        return peso_total

    def agregar_item(self, item_nuevo):
        peso_actual = self.calcular_peso_actual()
        
        if (peso_actual + item_nuevo.peso) <= self.capacidad_maxima:
            self.lista_items.append(item_nuevo)
            
            nombre = item_nuevo.nombre
            if nombre in self.conteo_items:
                self.conteo_items[nombre] = self.conteo_items[nombre] + 1
            else:
                self.conteo_items[nombre] = 1
                
            print(f"Se agrego: {item_nuevo.nombre}")
            return True
        else:
            print(f"¡Inventario lleno! No puedes cargar {item_nuevo.nombre}")
            return False

    def organizar_por_rareza(self):
        def valor_rareza(item):
            if item.rareza == "Legendario": return 4
            if item.rareza == "Epico": return 3
            if item.rareza == "Raro": return 2
            return 1 

        self.lista_items.sort(key=valor_rareza, reverse=True)
        print("\n--- Inventario organizado por rareza ---")

    def mostrar_resumen(self):
        print("\n--- Contenido de la Mochila ---")
        for nombre, cantidad in self.conteo_items.items():
            print(f"- {nombre}: tienes {cantidad}")
            
        peso = self.calcular_peso_actual()
        print(f"Peso Total: {peso}/{self.capacidad_maxima} kg")

mi_mochila = Inventario(20)

espada = Item("Espada de Hierro", 5, "Comun")
pocion = Item("Pocion de Vida", 1, "Comun")
escudo = Item("Escudo Dorado", 8, "Epico")
anillo = Item("Anillo de Poder", 0.5, "Legendario")
arco = Item("Arco Pesado", 10, "Raro") 

mi_mochila.agregar_item(espada)
mi_mochila.agregar_item(pocion)
mi_mochila.agregar_item(pocion) 
mi_mochila.agregar_item(escudo)
mi_mochila.agregar_item(anillo)

mi_mochila.agregar_item(arco) 

mi_mochila.mostrar_resumen()

mi_mochila.organizar_por_rareza()

print("Orden actual de la lista (items individuales):")
for i in mi_mochila.lista_items:
    print(i)