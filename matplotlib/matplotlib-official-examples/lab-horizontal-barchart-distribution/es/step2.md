# Preparar los datos

Necesitamos definir las categorías y los resultados de la encuesta. En este ejemplo, tenemos una encuesta en la que las personas calificaron su acuerdo a preguntas en una escala de cinco elementos. Definiremos las categorías como `category_names` y los resultados de la encuesta como `results`.

```python
category_names = ['Fuerte desacuerdo', 'Desacuerdo',
                  'Ni de acuerdo ni de desacuerdo', 'Acuerdo', 'Fuerte acuerdo']
results = {
    'Pregunta 1': [10, 15, 17, 32, 26],
    'Pregunta 2': [26, 22, 29, 10, 13],
    'Pregunta 3': [35, 37, 7, 2, 19],
    'Pregunta 4': [32, 11, 9, 15, 33],
    'Pregunta 5': [21, 29, 5, 5, 40],
    'Pregunta 6': [8, 19, 5, 30, 38]
}
```
