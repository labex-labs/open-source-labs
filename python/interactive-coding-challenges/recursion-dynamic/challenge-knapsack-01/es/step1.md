# Mochila 0/1

## Problema

Dada una mochila con una capacidad total de peso y una lista de elementos con peso w(i) y valor v(i), determinar qué elementos seleccionar para maximizar el valor total. El problema es conocido como el problema de la mochila 0/1 porque cada elemento solo se puede seleccionar una vez (decisión 0/1). El problema es NP-difícil, lo que significa que no existe un algoritmo de tiempo polinomial conocido que pueda resolverlo de manera óptima para todos los casos.

## Requisitos

Para resolver el problema de la mochila, debemos considerar los siguientes requisitos:

- Los elementos no se pueden reemplazar una vez que se colocan en la mochila.
- No podemos dividir un elemento.
- No podemos tener un elemento de entrada con peso o valor igual a 0.
- No podemos asumir que las entradas son válidas.
- Las entradas deben estar ordenadas por val/peso.
- Podemos asumir que el problema cabe en memoria.

## Ejemplo

A continuación, se muestra un ejemplo de cómo utilizar el algoritmo de la mochila:

```txt
peso_total = 8
elementos
  v | w
  0 | 0
a 2 | 2
b 4 | 2
c 6 | 4
d 9 | 5

valor máximo = 13
elementos
  v | w
b 4 | 2
d 9 | 5
```

En este ejemplo, tenemos una mochila con una capacidad total de peso de 8 y cuatro elementos con sus respectivos valores y pesos. Debemos seleccionar los elementos que maximicen el valor total mientras se mantenga el peso dentro de la capacidad de la mochila. La solución óptima es seleccionar los elementos b y d, que tienen un valor total de 13 y un peso total de 7.
