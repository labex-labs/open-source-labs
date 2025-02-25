# Crear una función de formato

Creamos una función de formato que determina la etiqueta de la marca de tiempo a partir del valor en la marca de tiempo. Si el valor de la marca de tiempo es un entero en el rango de `xs`, se devuelve la etiqueta correspondiente de la lista `labels`. En caso contrario, se devuelve una cadena vacía.

```python
def format_fn(tick_val, tick_pos):
    if int(tick_val) in xs:
        return labels[int(tick_val)]
    else:
        return ''
```
