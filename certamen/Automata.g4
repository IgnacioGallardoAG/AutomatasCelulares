grammar Automata;

SIMULAR: 'simular';
PASO: 'paso';
INFECTAR: 'infectar';
SUSCEPTIBLE: 'susceptible';
INFECTADO: 'infectado';
RECUPERADO: 'recuperado';
FALLECIDO: 'fallecido';
CONFIGURAR: 'configurar';
TASA: 'tasa';

inicio: (comando)+;

comando
   : comandoSimulacion
   | comandoConfiguracion
   ;

comandoSimulacion
   : SIMULAR PASO INT                    # SimularPaso
   | SIMULAR INFECTAR INT                # SimularInfeccion
   ;

comandoConfiguracion
   : CONFIGURAR TASA INFECTADO '=' FLOAT  # ConfigurarTasaInfeccion
   | CONFIGURAR TASA RECUPERADO '=' FLOAT # ConfigurarTasaRecuperacion
   | CONFIGURAR TASA FALLECIDO '=' FLOAT  # ConfigurarTasaMortalidad
   ;

INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;

WS: [ \t\r\n]+ -> skip;
