# Generated from Automata.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,43,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,1,1,1,3,1,16,8,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,24,8,2,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,41,8,3,
        1,3,0,0,4,0,2,4,6,0,0,43,0,9,1,0,0,0,2,15,1,0,0,0,4,23,1,0,0,0,6,
        40,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,11,1,0,0,0,11,9,1,0,0,0,11,
        12,1,0,0,0,12,1,1,0,0,0,13,16,3,4,2,0,14,16,3,6,3,0,15,13,1,0,0,
        0,15,14,1,0,0,0,16,3,1,0,0,0,17,18,5,2,0,0,18,19,5,3,0,0,19,24,5,
        11,0,0,20,21,5,2,0,0,21,22,5,4,0,0,22,24,5,11,0,0,23,17,1,0,0,0,
        23,20,1,0,0,0,24,5,1,0,0,0,25,26,5,9,0,0,26,27,5,10,0,0,27,28,5,
        6,0,0,28,29,5,1,0,0,29,41,5,12,0,0,30,31,5,9,0,0,31,32,5,10,0,0,
        32,33,5,7,0,0,33,34,5,1,0,0,34,41,5,12,0,0,35,36,5,9,0,0,36,37,5,
        10,0,0,37,38,5,8,0,0,38,39,5,1,0,0,39,41,5,12,0,0,40,25,1,0,0,0,
        40,30,1,0,0,0,40,35,1,0,0,0,41,7,1,0,0,0,4,11,15,23,40
    ]

class AutomataParser ( Parser ):

    grammarFileName = "Automata.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'simular'", "'paso'", "'infectar'", 
                     "'susceptible'", "'infectado'", "'recuperado'", "'fallecido'", 
                     "'configurar'", "'tasa'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "SIMULAR", "PASO", "INFECTAR", 
                      "SUSCEPTIBLE", "INFECTADO", "RECUPERADO", "FALLECIDO", 
                      "CONFIGURAR", "TASA", "INT", "FLOAT", "WS" ]

    RULE_inicio = 0
    RULE_comando = 1
    RULE_comandoSimulacion = 2
    RULE_comandoConfiguracion = 3

    ruleNames =  [ "inicio", "comando", "comandoSimulacion", "comandoConfiguracion" ]

    EOF = Token.EOF
    T__0=1
    SIMULAR=2
    PASO=3
    INFECTAR=4
    SUSCEPTIBLE=5
    INFECTADO=6
    RECUPERADO=7
    FALLECIDO=8
    CONFIGURAR=9
    TASA=10
    INT=11
    FLOAT=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class InicioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AutomataParser.ComandoContext)
            else:
                return self.getTypedRuleContext(AutomataParser.ComandoContext,i)


        def getRuleIndex(self):
            return AutomataParser.RULE_inicio

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInicio" ):
                listener.enterInicio(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInicio" ):
                listener.exitInicio(self)




    def inicio(self):

        localctx = AutomataParser.InicioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_inicio)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.comando()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==AutomataParser.SIMULAR or _la==AutomataParser.CONFIGURAR):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comandoSimulacion(self):
            return self.getTypedRuleContext(AutomataParser.ComandoSimulacionContext,0)


        def comandoConfiguracion(self):
            return self.getTypedRuleContext(AutomataParser.ComandoConfiguracionContext,0)


        def getRuleIndex(self):
            return AutomataParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)




    def comando(self):

        localctx = AutomataParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comando)
        try:
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [AutomataParser.SIMULAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.comandoSimulacion()
                pass
            elif token in [AutomataParser.CONFIGURAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.comandoConfiguracion()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoSimulacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AutomataParser.RULE_comandoSimulacion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SimularInfeccionContext(ComandoSimulacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AutomataParser.ComandoSimulacionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIMULAR(self):
            return self.getToken(AutomataParser.SIMULAR, 0)
        def INFECTAR(self):
            return self.getToken(AutomataParser.INFECTAR, 0)
        def INT(self):
            return self.getToken(AutomataParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimularInfeccion" ):
                listener.enterSimularInfeccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimularInfeccion" ):
                listener.exitSimularInfeccion(self)


    class SimularPasoContext(ComandoSimulacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AutomataParser.ComandoSimulacionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SIMULAR(self):
            return self.getToken(AutomataParser.SIMULAR, 0)
        def PASO(self):
            return self.getToken(AutomataParser.PASO, 0)
        def INT(self):
            return self.getToken(AutomataParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimularPaso" ):
                listener.enterSimularPaso(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimularPaso" ):
                listener.exitSimularPaso(self)



    def comandoSimulacion(self):

        localctx = AutomataParser.ComandoSimulacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_comandoSimulacion)
        try:
            self.state = 23
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = AutomataParser.SimularPasoContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(AutomataParser.SIMULAR)
                self.state = 18
                self.match(AutomataParser.PASO)
                self.state = 19
                self.match(AutomataParser.INT)
                pass

            elif la_ == 2:
                localctx = AutomataParser.SimularInfeccionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.match(AutomataParser.SIMULAR)
                self.state = 21
                self.match(AutomataParser.INFECTAR)
                self.state = 22
                self.match(AutomataParser.INT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoConfiguracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AutomataParser.RULE_comandoConfiguracion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ConfigurarTasaMortalidadContext(ComandoConfiguracionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AutomataParser.ComandoConfiguracionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CONFIGURAR(self):
            return self.getToken(AutomataParser.CONFIGURAR, 0)
        def TASA(self):
            return self.getToken(AutomataParser.TASA, 0)
        def FALLECIDO(self):
            return self.getToken(AutomataParser.FALLECIDO, 0)
        def FLOAT(self):
            return self.getToken(AutomataParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfigurarTasaMortalidad" ):
                listener.enterConfigurarTasaMortalidad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfigurarTasaMortalidad" ):
                listener.exitConfigurarTasaMortalidad(self)


    class ConfigurarTasaRecuperacionContext(ComandoConfiguracionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AutomataParser.ComandoConfiguracionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CONFIGURAR(self):
            return self.getToken(AutomataParser.CONFIGURAR, 0)
        def TASA(self):
            return self.getToken(AutomataParser.TASA, 0)
        def RECUPERADO(self):
            return self.getToken(AutomataParser.RECUPERADO, 0)
        def FLOAT(self):
            return self.getToken(AutomataParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfigurarTasaRecuperacion" ):
                listener.enterConfigurarTasaRecuperacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfigurarTasaRecuperacion" ):
                listener.exitConfigurarTasaRecuperacion(self)


    class ConfigurarTasaInfeccionContext(ComandoConfiguracionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AutomataParser.ComandoConfiguracionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def CONFIGURAR(self):
            return self.getToken(AutomataParser.CONFIGURAR, 0)
        def TASA(self):
            return self.getToken(AutomataParser.TASA, 0)
        def INFECTADO(self):
            return self.getToken(AutomataParser.INFECTADO, 0)
        def FLOAT(self):
            return self.getToken(AutomataParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConfigurarTasaInfeccion" ):
                listener.enterConfigurarTasaInfeccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConfigurarTasaInfeccion" ):
                listener.exitConfigurarTasaInfeccion(self)



    def comandoConfiguracion(self):

        localctx = AutomataParser.ComandoConfiguracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_comandoConfiguracion)
        try:
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = AutomataParser.ConfigurarTasaInfeccionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(AutomataParser.CONFIGURAR)
                self.state = 26
                self.match(AutomataParser.TASA)
                self.state = 27
                self.match(AutomataParser.INFECTADO)
                self.state = 28
                self.match(AutomataParser.T__0)
                self.state = 29
                self.match(AutomataParser.FLOAT)
                pass

            elif la_ == 2:
                localctx = AutomataParser.ConfigurarTasaRecuperacionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.match(AutomataParser.CONFIGURAR)
                self.state = 31
                self.match(AutomataParser.TASA)
                self.state = 32
                self.match(AutomataParser.RECUPERADO)
                self.state = 33
                self.match(AutomataParser.T__0)
                self.state = 34
                self.match(AutomataParser.FLOAT)
                pass

            elif la_ == 3:
                localctx = AutomataParser.ConfigurarTasaMortalidadContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.match(AutomataParser.CONFIGURAR)
                self.state = 36
                self.match(AutomataParser.TASA)
                self.state = 37
                self.match(AutomataParser.FALLECIDO)
                self.state = 38
                self.match(AutomataParser.T__0)
                self.state = 39
                self.match(AutomataParser.FLOAT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





