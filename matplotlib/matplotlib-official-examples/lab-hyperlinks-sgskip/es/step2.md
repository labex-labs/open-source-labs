# Crear un diagrama de dispersión con enlaces hipervinculo

En este paso, crearemos un diagrama de dispersión y agregaremos enlaces hipervinculo a los marcadores. Aquí está el código para crear el diagrama de dispersión:

```python
fig = plt.figure()
s = plt.scatter([1, 2, 3], [4, 5, 6])
```

Para agregar enlaces hipervinculo, debemos utilizar el método `set_urls()` del objeto del diagrama de dispersión. Este método toma una lista de URLs como argumento. Aquí está el código actualizado:

```python
s.set_urls(['https://www.bbc.com/news', 'https://www.google.com/', None])
```

Los primeros dos marcadores tendrán enlaces hipervinculo a `https://www.bbc.com/news` y `https://www.google.com/`, respectivamente. El tercer marcador no tendrá un enlace hipervinculo. Finalmente, podemos guardar el gráfico como un archivo SVG utilizando `fig.savefig()`:

```python
fig.savefig('scatter.svg')
```
