# Generated from Automata.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .AutomataParser import AutomataParser
else:
    from AutomataParser import AutomataParser

# This class defines a complete listener for a parse tree produced by AutomataParser.
class AutomataListener(ParseTreeListener):

    # Enter a parse tree produced by AutomataParser#inicio.
    def enterInicio(self, ctx:AutomataParser.InicioContext):
        pass

    # Exit a parse tree produced by AutomataParser#inicio.
    def exitInicio(self, ctx:AutomataParser.InicioContext):
        pass


    # Enter a parse tree produced by AutomataParser#comando.
    def enterComando(self, ctx:AutomataParser.ComandoContext):
        pass

    # Exit a parse tree produced by AutomataParser#comando.
    def exitComando(self, ctx:AutomataParser.ComandoContext):
        pass


    # Enter a parse tree produced by AutomataParser#SimularPaso.
    def enterSimularPaso(self, ctx:AutomataParser.SimularPasoContext):
        pass

    # Exit a parse tree produced by AutomataParser#SimularPaso.
    def exitSimularPaso(self, ctx:AutomataParser.SimularPasoContext):
        pass


    # Enter a parse tree produced by AutomataParser#SimularInfeccion.
    def enterSimularInfeccion(self, ctx:AutomataParser.SimularInfeccionContext):
        pass

    # Exit a parse tree produced by AutomataParser#SimularInfeccion.
    def exitSimularInfeccion(self, ctx:AutomataParser.SimularInfeccionContext):
        pass


    # Enter a parse tree produced by AutomataParser#ConfigurarTasaInfeccion.
    def enterConfigurarTasaInfeccion(self, ctx:AutomataParser.ConfigurarTasaInfeccionContext):
        pass

    # Exit a parse tree produced by AutomataParser#ConfigurarTasaInfeccion.
    def exitConfigurarTasaInfeccion(self, ctx:AutomataParser.ConfigurarTasaInfeccionContext):
        pass


    # Enter a parse tree produced by AutomataParser#ConfigurarTasaRecuperacion.
    def enterConfigurarTasaRecuperacion(self, ctx:AutomataParser.ConfigurarTasaRecuperacionContext):
        pass

    # Exit a parse tree produced by AutomataParser#ConfigurarTasaRecuperacion.
    def exitConfigurarTasaRecuperacion(self, ctx:AutomataParser.ConfigurarTasaRecuperacionContext):
        pass


    # Enter a parse tree produced by AutomataParser#ConfigurarTasaMortalidad.
    def enterConfigurarTasaMortalidad(self, ctx:AutomataParser.ConfigurarTasaMortalidadContext):
        pass

    # Exit a parse tree produced by AutomataParser#ConfigurarTasaMortalidad.
    def exitConfigurarTasaMortalidad(self, ctx:AutomataParser.ConfigurarTasaMortalidadContext):
        pass



del AutomataParser