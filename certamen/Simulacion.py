from antlr4 import *

from AutomataLexer import AutomataLexer
from AutomataParser import AutomataParser


# Clase para representar una celda en el autómata
class Celda:
    def __init__(self, estado="Susceptible"):
        self.estado = estado 
        self.prob_infeccion = None  # Tasa de infección predeterminada
        self.prob_recuperacion = None  # Tasa de recuperación predeterminada
        self.prob_mortalidad = None  # Tasa de mortalidad predeterminada

    def actualizar_estado(self):
        # Lógica simplificada de actualización de estado
        pass  # Implementaremos después la lógica completa

# Clase para el autómata celular
class AutomataCelular:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.grilla = [[Celda() for _ in range(columnas)] for _ in range(filas)]

    def configurar_tasa(self, tipo, valor):
        # Configura la tasa en todas las celdas del autómata
        for fila in self.grilla:
            for celda in fila:
                if tipo == "infectado":
                    celda.prob_infeccion = valor
                elif tipo == "recuperado":
                    celda.prob_recuperacion = valor
                elif tipo == "fallecido":
                    celda.prob_mortalidad = valor

    def mostrar_grilla(self):
        for fila in self.grilla:
            print(" ".join([celda.estado[0] for celda in fila]))
        print()

# Función para procesar los comandos y configurar el autómata
def procesar_comandos(automata):
    input_stream = FileStream("entrada.txt")
    lexer = AutomataLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = AutomataParser(token_stream)
    tree = parser.inicio()

    for comando in tree.getChildren():
        if comando.getChild(0).getText() == "configurar":
            tipo_tasa = comando.getChild(2).getText()
            valor = float(comando.getChild(4).getText())
            automata.configurar_tasa(tipo_tasa, valor)

# Función principal para inicializar el autómata y procesar los comandos
def main():
    automata = AutomataCelular(5, 5)  # Crear una grilla de 5x5 para el ejemplo
    procesar_comandos(automata)
    print("Tasas configuradas en el autómata:")
    automata.mostrar_grilla()

if __name__ == "__main__":
    main()
