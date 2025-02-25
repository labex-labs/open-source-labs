# Reglas generales de difusión (broadcasting)

NumPy compara las formas de dos matrices elemento a elemento para determinar si son compatibles para la difusión (broadcasting). Las siguientes reglas se aplican:

1. Dos dimensiones son compatibles si tienen el mismo tamaño.
2. Dos dimensiones son compatibles si una de ellas tiene un tamaño de 1.

Si no se cumplen estas condiciones, se genera un `ValueError`, lo que indica que las matrices tienen formas incompatibles.
