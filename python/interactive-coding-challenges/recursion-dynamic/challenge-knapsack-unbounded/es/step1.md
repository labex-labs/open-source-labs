# Mochila Ilimitada

## Problema

Dada una mochila con una capacidad total de peso y una lista de elementos con peso w(i) y valor v(i), determinar el valor total máximo que se puede cargar. Los elementos se pueden seleccionar múltiples veces.

## Requisitos

Para resolver el problema de la mochila ilimitada, deben cumplirse los siguientes requisitos:

- Los elementos se pueden reemplazar una vez que se colocan en la mochila.
- Un elemento no se puede dividir.
- Los elementos de entrada no pueden tener un peso o valor de 0.
- Solo se debe devolver el valor total, no los elementos que componen el valor total máximo.
- Las entradas pueden no ser válidas, por lo que se requiere validación.
- Las entradas están ordenadas por val/peso.
- Las restricciones de memoria no son un problema.

## Uso de ejemplo

El problema de la mochila ilimitada se puede utilizar en varios escenarios, como la asignación de recursos y la optimización de carteras financieras. Aquí hay algunos ejemplos de cómo se puede utilizar:

- Si el peso total o los elementos son None, se debe generar una excepción.
- Si el peso total o los elementos son 0, el resultado debe ser 0.
- Para un caso general, suponga que el peso total es 8 y los elementos son:

  | v   | w   |
  | --- | --- |
  | 0   | 0   |
  | 1   | 1   |
  | 3   | 2   |
  | 7   | 4   |

  El valor máximo que se puede cargar es 14.
