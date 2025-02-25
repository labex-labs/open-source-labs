# Tamaño de la figura en píxeles

También podemos especificar el tamaño de la figura en píxeles. Para hacer esto, necesitamos convertir el valor en píxeles a pulgadas. Podemos obtener el factor de conversión de píxeles a pulgadas dividiendo 1 por el valor de dpi (puntos por pulgada). Luego podemos utilizar este valor como el parámetro figsize en la función subplots. El código siguiente muestra cómo crear una figura con un tamaño de 600 píxeles x 200 píxeles.

```python
px = 1/plt.rcParams['figure.dpi']  # píxel en pulgadas
plt.subplots(figsize=(600*px, 200*px))
plt.show()
```
