# Crear un cuadro de texto

```python
plt.text(0.6, 0.7, "eggs", size=50, rotation=30.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )
```

Creamos un cuadro de texto que contiene la palabra "eggs" utilizando el método `text()`. El parámetro `bbox` se utiliza para estilizar el cuadro. El parámetro `boxstyle` se establece en "round" para crear un cuadro redondeado, mientras que los parámetros `ec` y `fc` establecen los colores del borde y de la cara del cuadro, respectivamente. El parámetro `size` establece el tamaño de la fuente, el parámetro `rotation` establece el ángulo de rotación y los parámetros `ha` y `va` establecen la alineación horizontal y vertical del texto dentro del cuadro.
