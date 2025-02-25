# Sumar Dígitos

## Problema

Dado un entero, debemos sumar repetidamente sus dígitos hasta que el resultado sea un solo dígito. Por ejemplo, si se nos da el entero 138, sumamos 1 + 3 + 8 = 12. Dado que 12 no es un solo dígito, repetimos el proceso y sumamos 1 + 2 = 3. Por lo tanto, el resultado final es 3.

## Requisitos

Para resolver este problema, debemos considerar los siguientes requisitos:

- El entero de entrada no es negativo.
- Las entradas no siempre pueden ser válidas, por lo que debemos manejar cualquier error que pueda ocurrir.
- La solución debe caber en memoria.

## Uso de Ejemplo

A continuación se presentan algunos ejemplos de cómo se puede utilizar esta función:

- Si pasamos None como entrada, la función debe generar un TypeError.
- Si pasamos un entero negativo como entrada, la función debe generar un ValueError.
- Si pasamos 9 como entrada, la función debe devolver 9 ya que ya es un solo dígito.
- Si pasamos 138 como entrada, la función debe devolver 3.
- Si pasamos 65536 como entrada, la función debe devolver 7.
