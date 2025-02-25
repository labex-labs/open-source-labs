# Crear otro cuadro de texto

```python
plt.text(0.55, 0.6, "spam", size=50, rotation=-25.,
         ha="right", va="top",
         bbox=dict(boxstyle="square",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )
```

Creamos otro cuadro de texto que contiene la palabra "spam". Esta vez establecemos el parámetro `boxstyle` en "square" para crear un cuadro cuadrado y los parámetros `ha` y `va` en "right" y "top" para alinear el texto a la derecha y arriba del cuadro.
