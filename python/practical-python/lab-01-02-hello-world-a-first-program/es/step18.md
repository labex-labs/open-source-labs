# Ejercicio 1.5: La Pelota Rebotante

Una pelota de goma se deja caer desde una altura de 100 metros y cada vez que golpea el suelo, rebota hasta 3/5 de la altura desde la que cayó. Escribe un programa `bounce.py` que imprima una tabla mostrando la altura de las primeras 10 rebotes.

Aquí está una solución:

```python
# bounce.py

height = 100
bounce = 1
while bounce <= 10:
    height = height * (3 / 5)
    print(bounce, round(height, 4))
    bounce += 1
```

Tu programa debe crear una tabla que se vea más o menos así:

```code
1 60.0
2 36.0
3 21.599999999999998
4 12.959999999999999
5 7.775999999999999
6 4.6655999999999995
7 2.7993599999999996
8 1.6796159999999998
9 1.0077695999999998
10 0.6046617599999998
```

_Nota: Puedes limpiar un poco la salida si utilizas la función round(). Intenta usarlo para redondear la salida a 4 dígitos._

```code
1 60.0
2 36.0
3 21.6
4 12.96
5 7.776
6 4.6656
7 2.7994
8 1.6796
9 1.0078
10 0.6047
```
