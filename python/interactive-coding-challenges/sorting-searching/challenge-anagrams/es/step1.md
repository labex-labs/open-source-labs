# Anagramas

## Problema

Dada una matriz de cadenas, escribe una función para ordenar la matriz de modo que todos los anagramas estén uno al lado del otro. Un anagrama se define como una palabra o frase formada al reordenar las letras de otra palabra o frase. Por ejemplo, "act" y "cat" son anagramas el uno del otro.

## Requisitos

Para resolver este problema, deben cumplirse los siguientes requisitos:

- La función debe agrupar todos los anagramas juntos en la matriz ordenada.
- No hay otros requisitos de clasificación más allá del agrupamiento de anagramas.
- Las entradas pueden no ser válidas, por lo que la función debe manejar entradas no válidas.
- La función debe caber en la memoria.

## Uso de ejemplo

La función debe comportarse de la siguiente manera en estos escenarios:

- Ninguno -> Excepción
- [] -> []
- Caso general
  - Entrada: ['ram', 'act', 'arm', 'bat', 'cat', 'tab']
  - Resultado: ['arm', 'ram', 'act', 'cat', 'bat', 'tab']
