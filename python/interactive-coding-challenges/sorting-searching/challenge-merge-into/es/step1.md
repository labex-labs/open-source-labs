# Fusionar en

## Problema

Dadas dos matrices ordenadas A y B, fusionar B en A en orden ascendente. Las matrices pueden contener elementos duplicados y las entradas pueden no ser válidas. Las entradas también incluirán el tamaño real de A y B, y podemos suponer que esto cabe en memoria.

Para resolver este problema, debemos considerar si A tiene suficiente espacio para B y si las entradas tienen elementos duplicados en la matriz. Si A no tiene suficiente espacio para B, es posible que necesitemos asignar memoria adicional. Si las entradas tienen elementos duplicados en la matriz, debemos asegurarnos de que estos duplicados se manejen correctamente durante la fusión.

## Requisitos

Para resolver este problema, debemos cumplir con los siguientes requisitos:

- Asegurarse de que A tenga suficiente espacio para B
- Manejar correctamente los elementos duplicados de la matriz
- Comprobar que las entradas son válidas
- Incluir el tamaño real de A y B en las entradas
- Suponer que las entradas caben en memoria

## Uso de ejemplo

Para ilustrar cómo se puede resolver este problema, considere los siguientes ejemplos:

- Si A o B es None, se debe generar una excepción.
- Si el índice del último elemento en A o B es menor que 0, se debe generar una excepción.
- Si A o B está vacía, el resultado debe ser A o B, respectivamente.
- En el caso general, podemos fusionar B en A de la siguiente manera:

```
A = [1, 3, 5, 7, 9, None, None, None]
B = [4, 5, 6]
A = [1, 3, 4, 5, 5, 6, 7, 9]
```
