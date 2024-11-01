# Proyecto de Simulación de Autómata Celular
* Este proyecto implementa un autómata celular asimétrico para simular modelos de contagio compartimental, configurando tasas de infección, recuperación y mortalidad en una grilla de celdas.
* Cada celda representa un grupo poblacional que puede cambiar de estado según las tasas configuradas.

## Requisitos
1. Se utilizó Python 3.12.1, recomiendo usar una versión superior a la 3.8, aunque idealmente usar la misma.
   * Para verificarlo en consola usar el comando "python --version"
2. Este proyecto usa ANTLR para el análisis léxico y sintáctico. dentro del proyecto deje el archivo de ANTLR que usé sino descargalo desde la página oficial de ANTLR.
3. Debes tener el paquete de ANTLR para python:
    * comando --> "pip install antlr4-python3-runtime"

## Estructura del proyecto

* Automata.g4: Es el archivo de gramática ANTLR que define los comandos para configurar el autómata.
* Simulacion.py: Script principal para ejecutar la simulación. Configura el autómata según los comandos y muestra el estado inicial de la grilla.
* entrada.txt: Archivo de entrada que contiene los comandos para configurar para configurar las tasas de infección, recuperación y mortalidad.
* Limpiar.bat: Es un script de limpieza para eliminar archivos generados por ANTLR.

## Generar los archivos ANTLR

