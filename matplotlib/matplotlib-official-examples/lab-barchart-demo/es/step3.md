# Definir funciones auxiliares

Definimos dos funciones auxiliares. La primera función, `to_ordinal`, convierte un número entero en una cadena ordinal (por ejemplo, 2 -> '2nd'). La segunda función, `format_score`, crea etiquetas de puntuación para el eje y derecho como el nombre de la prueba seguido de la unidad de medida (si la hay), dividido en dos líneas.

```python
def to_ordinal(num):
    suffixes = {str(i): v
                for i, v in enumerate(['th', 'st', 'nd', 'rd', 'th',
                                       'th', 'th', 'th', 'th', 'th'])}
    v = str(num)
    if v in {'11', '12', '13'}:
        return v + 'th'
    return v + suffixes[v[-1]]

def format_score(score):
    return f'{score.value}\n{score.unit}' if score.unit else str(score.value)
```
