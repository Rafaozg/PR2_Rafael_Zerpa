"""
Rafael Zerpa, V-31.148.991
"""

import random

class Aldeano:
    def __init__(self):
        nombres = ["Arthur", "Beatrice", "Cédric", "Diana", "Elias", "Fiona"]
        apellidos = ["Stark", "Targaryen", "Lannister", "Snow", "Tully"]
        
        self.nombre = random.choice(nombres)
        self.apellido = random.choice(apellidos)
        self.edad = random.randint(18, 50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Almacen:
    def __init__(self):
        self.__inventario = {
            "Trigo": 0, "Pan": 0, "Madera": 0, "Piedra": 0,
            "Hierro": 0, "Oro": 0, "Monedas": 0
        }

    def ver_inventario(self):
        return self.__inventario.copy()

    def agregar_recursos(self, recursos):
        for item, cantidad in recursos.items():
            if item in self.__inventario:
                self.__inventario[item] += cantidad

    def consumir_recursos(self, recursos_necesarios):
        for item, cantidad in recursos_necesarios.items():
            if self.__inventario.get(item, 0) < cantidad:
                return False 
        
        for item, cantidad in recursos_necesarios.items():
            self.__inventario[item] -= cantidad
        return True

class Edificio:
    def __init__(self, nombre, costo_base):
        self.nombre = nombre
        self.nivel = 1
        self.costo_base = costo_base 

    def mejorar(self, almacen):
        costo_mejora = {}
        for item, cantidad in self.costo_base.items():
            costo_mejora[item] = cantidad * self.nivel

        if almacen.consumir_recursos(costo_mejora):
            self.nivel += 1
            print(f"[{self.nombre}] Nivel {self.nivel} alcanzado.")
            return True
        else:
            print(f"[{self.nombre}] Recursos insuficientes para mejorar.")
            return False

class Casa(Edificio):
    def __init__(self, nombre):
        costo_construccion = {"Madera": 5, "Piedra": 5}
        super().__init__(nombre, costo_construccion)

    def obtener_capacidad(self):
        return 3 + (2 * self.nivel)

class EdificioTrabajo(Edificio):
    def __init__(self, nombre, costo_mejora, costo_produccion, item_produce, cant_produce, turnos_req):
        super().__init__(nombre, costo_mejora)
        self.costo_produccion = costo_produccion 
        self.item_produce = item_produce         
        self.cant_produce = cant_produce         
        self.turnos_req = turnos_req             
        
        self.lista_activos = []
        self.lista_espera = []
        self.turno_actual = 0
        self.en_produccion = False 

    def _integrar_espera(self):
        if len(self.lista_espera) > 0:
            self.lista_activos.extend(self.lista_espera)
            self.lista_espera.clear()

    def remover_trabajador(self, aldeano):
        if aldeano in self.lista_espera:
            self.lista_espera.remove(aldeano)
            return True
        elif aldeano in self.lista_activos:
            self.lista_activos.remove(aldeano)
            print(f"[{self.nombre}] ALERTA: Trabajador retirado. Ciclo reiniciado.")
            self.turno_actual = 0
            self.en_produccion = False
            return True
        return False

    def trabajar(self, almacen):
        if len(self.lista_activos) == 0:
            self._integrar_espera()
            return True

        if self.turno_actual == 0 and not self.en_produccion:
            costo_total = {}
            for item, cantidad in self.costo_produccion.items():
                costo_total[item] = cantidad * len(self.lista_activos)

            if almacen.consumir_recursos(costo_total):
                self.en_produccion = True
            else:
                print(f"[{self.nombre}] DETENIDO: Faltan materiales.")
                return False 

        if self.en_produccion:
            self.turno_actual += 1
            
            if self.turno_actual == self.turnos_req:
                produccion_total = (self.cant_produce * len(self.lista_activos)) * self.nivel
                almacen.agregar_recursos({self.item_produce: produccion_total})
                print(f"[{self.nombre}] produjo {produccion_total} {self.item_produce}.")
                
                self.turno_actual = 0
                self.en_produccion = False
                self._integrar_espera()
        return True

class Asentamiento:
    def __init__(self):
        self.almacen = Almacen()
        self.casas = []
        self.edificios_trabajo = []
        self.poblacion_total = []

    def construir_casa(self, nombre):
        multiplicador = len(self.casas) + 1
        costo_construccion = {"Madera": 5 * multiplicador, "Piedra": 5 * multiplicador}
        
        print(f"Construyendo '{nombre}' (Costo: {costo_construccion})...")
        if self.almacen.consumir_recursos(costo_construccion):
            nueva_casa = Casa(nombre)
            self.casas.append(nueva_casa)
            print(f"Casa '{nombre}' construida con éxito.")
            return True
        else:
            print("Construcción fallida: Recursos insuficientes.")
            return False

    def reclutar_aldeano(self):
        capacidad_maxima = 0
        for casa in self.casas:
            capacidad_maxima += casa.obtener_capacidad()
            
        if len(self.poblacion_total) < capacidad_maxima:
            nuevo_aldeano = Aldeano()
            self.poblacion_total.append(nuevo_aldeano)
            print(f"Reclutado: {nuevo_aldeano}")
            return nuevo_aldeano
        else:
            print("Límite de población. Construye más casas.")
            return None

    def asignar_aldeano(self, aldeano, edificio):
        edificio.lista_espera.append(aldeano)
        print(f"{aldeano.nombre} asignado a {edificio.nombre} (En espera).")

    def remover_aldeano(self, aldeano, edificio):
        edificio.remover_trabajador(aldeano)

    def avanzar_turno(self):
        print("\n--- NUEVO TURNO ---")
        for edificio in self.edificios_trabajo:
            edificio.trabajar(self.almacen)
            
        print("\nINVENTARIO:")
        inventario = self.almacen.ver_inventario()
        for item, cantidad in inventario.items():
            print(f" - {item}: {cantidad}")
        print("-------------------\n")

if __name__ == "__main__":
    print("=== SIMULADOR DE ASENTAMIENTO ===\n")
    mi_ciudad = Asentamiento()
    
    mi_ciudad.almacen.agregar_recursos({"Madera": 50, "Piedra": 50})
    
    mi_ciudad.construir_casa("Cabaña Norte")
    mi_ciudad.construir_casa("Cabaña Sur")
    
    aldeano1 = mi_ciudad.reclutar_aldeano()
    aldeano2 = mi_ciudad.reclutar_aldeano()
    aldeano3 = mi_ciudad.reclutar_aldeano()
    aldeano4 = mi_ciudad.reclutar_aldeano()
    
    granja = EdificioTrabajo("Granja", {"Madera": 10}, {}, "Trigo", 1, 1)
    panaderia = EdificioTrabajo("Panadería", {"Piedra": 10}, {"Trigo": 2}, "Pan", 1, 1)
    aserradero = EdificioTrabajo("Aserradero", {"Piedra": 15}, {"Pan": 2}, "Madera", 3, 2)
    cantera = EdificioTrabajo("Cantera", {"Madera": 15}, {"Pan": 2}, "Piedra", 3, 2)
    mina_hierro = EdificioTrabajo("Mina de Hierro", {"Madera": 25}, {"Piedra": 2, "Pan": 3}, "Hierro", 1, 3)
    mina_oro = EdificioTrabajo("Mina de Oro", {"Madera": 30, "Piedra": 30}, {"Hierro": 1, "Pan": 5}, "Oro", 1, 3)
    casa_moneda = EdificioTrabajo("Casa de Moneda", {"Piedra": 40}, {"Oro": 1}, "Monedas", 10, 1)

    mi_ciudad.edificios_trabajo.extend([
        granja, panaderia, aserradero, cantera, 
        mina_hierro, mina_oro, casa_moneda
    ])
    
    print("\n[Asignación de Tareas]")
    mi_ciudad.asignar_aldeano(aldeano1, granja)
    mi_ciudad.asignar_aldeano(aldeano2, granja)
    mi_ciudad.asignar_aldeano(aldeano3, panaderia)
    mi_ciudad.asignar_aldeano(aldeano4, aserradero)
    
    mi_ciudad.avanzar_turno()
    mi_ciudad.avanzar_turno()
    mi_ciudad.avanzar_turno()