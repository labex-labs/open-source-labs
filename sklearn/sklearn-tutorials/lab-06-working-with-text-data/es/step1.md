# Carga de los datos de texto

En primer lugar, necesitamos cargar los datos de texto con los que vamos a trabajar. Utilizaremos el conjunto de datos 20 Newsgroups, que contiene artículos de noticias de veinte temas diferentes. Para cargar el conjunto de datos, podemos utilizar la función `fetch_20newsgroups` de scikit-learn.

```python
from sklearn.datasets import fetch_20newsgroups

# Carga el conjunto de datos
categories = ['alt.atheism','soc.religion.christian', 'comp.graphics','sci.med']
twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
```

Ahora ya hemos cargado los datos y podemos explorar su estructura y contenido.
