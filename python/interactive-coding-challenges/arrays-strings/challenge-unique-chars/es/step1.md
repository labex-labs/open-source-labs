# Caracteres únicos

## Problema

Dada una cadena, la tarea es determinar si contiene todos sus caracteres únicos. En otras palabras, no debe haber caracteres repetidos en la cadena. Por ejemplo, la cadena "hello" no tiene todos sus caracteres únicos porque la letra "l" aparece dos veces. Por otro lado, la cadena "world" tiene todos sus caracteres únicos porque cada letra aparece solo una vez.

## Requisitos

Para resolver este problema, deben cumplirse los siguientes requisitos:

- Se asume que la cadena es ASCII.
  - Las cadenas Unicode pueden requerir un manejo especial dependiendo del idioma utilizado.
- Se asume que la distinción entre mayúsculas y minúsculas es sensible.
- Se pueden utilizar estructuras de datos adicionales.
- Se asume que la cadena cabe en memoria.

## Uso de ejemplo

Los siguientes son ejemplos de cómo debe comportarse la función:

- None -> False
- '' -> True
- 'foo' -> False
- 'bar' -> True
