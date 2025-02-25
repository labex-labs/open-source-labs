# Crea una función para establecer parámetros predeterminados

Para crear una función que establezca los parámetros predeterminados para tus figuras, puedes utilizar el método `rcParams.update()`. Este método toma un diccionario de nombres y valores de parámetros, y actualiza los valores predeterminados actuales con los nuevos. Aquí te presento un ejemplo de una función que establece algunos parámetros predeterminados para figuras destinadas a publicaciones:

```python
def set_pub():
    rcParams.update({
        "font.weight": "bold",  # fuentes en negrita
        "tick.labelsize": 15,   # etiquetas de los ejes con tamaño grande
        "lines.linewidth": 1,   # líneas gruesas
        "lines.color": "k",     # líneas negras
        "grid.color": "0.5",    # líneas de cuadrícula en gris
        "grid.linestyle": "-",  # líneas de cuadrícula sólidas
        "grid.linewidth": 0.5,  # líneas de cuadrícula delgadas
        "savefig.dpi": 300,     # salida con mayor resolución.
    })
```
