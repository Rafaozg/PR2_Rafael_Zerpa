"""
Rafael Zerpa, 31148991

3. El Mazo de Cartas (Juego de 21)
Contexto: Se requiere programar la lógica base para un juego de cartas sencillo. El azar y la
gestión de colecciones son fundamentales aquí.
● Misión: Diseñar el TDA Carta (palo, valor_numerico) y el TDA Mazo.
● Lógica: El Mazo debe inicializarse con las 52 cartas. Debe incluir un método
repartir_carta() que retire una carta aleatoria del mazo y la entregue. Implementar una
función que sume los puntos de una mano de cartas, considerando que las figuras valen
10.
"""
import random

class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor

    def __str__(self):
        return f"{self.valor} de {self.palo}"

class Mazo:
    def __init__(self):
        self.cartas = []
        palos = ["Corazones", "Diamantes", "Tréboles", "Picas"]
        valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

        for palo in palos:
            for valor in valores:
                nueva_carta = Carta(palo, valor)
                self.cartas.append(nueva_carta)

    def repartir_carta(self):
        if len(self.cartas) > 0:
            indice_aleatorio = random.randint(0, len(self.cartas) - 1)
            carta_repartida = self.cartas.pop(indice_aleatorio)
            return carta_repartida
        else:
            return None

def calcular_puntos(mano):
    total = 0
    for carta in mano:
        valor = carta.valor
        
        if valor in ['J', 'Q', 'K']:
            total += 10
        elif valor == 'A':
            total += 11
        else:
            total += int(valor)
            
    return total

if __name__ == "__main__":
    print("--- Iniciando Juego de Cartas ---")
    
    mi_mazo = Mazo()
    print(f"Mazo creado con {len(mi_mazo.cartas)} cartas.")

    mano_jugador = []
    
    print("\nRepartiendo cartas...")
    carta1 = mi_mazo.repartir_carta()
    carta2 = mi_mazo.repartir_carta()
    
    mano_jugador.append(carta1)
    mano_jugador.append(carta2)

    print("Tu mano:")
    for c in mano_jugador:
        print(f" - {c}")

    puntos = calcular_puntos(mano_jugador)
    print(f"\nPuntaje total: {puntos}")
    
    print(f"(Quedan {len(mi_mazo.cartas)} cartas en el mazo)")