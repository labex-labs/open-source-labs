# Preparar los datos

A continuación, prepararemos los datos para nuestro gráfico. Tenemos tres especies de pingüinos y tres atributos, por lo que crearemos un diccionario con los promedios de cada atributo por especie.

```python
species = ("Adelie", "Chinstrap", "Gentoo")
penguin_means = {
    'Bill Depth': (18.35, 18.43, 14.98),
    'Bill Length': (38.79, 48.83, 47.50),
    'Flipper Length': (189.95, 195.82, 217.19),
}
```
