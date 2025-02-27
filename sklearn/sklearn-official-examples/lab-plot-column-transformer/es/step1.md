# Conjunto de datos

Usaremos el conjunto de datos 20 newsgroups, que consta de publicaciones de grupos de noticias sobre 20 temas. El conjunto de datos se divide en subconjuntos de entrenamiento y prueba en función de los mensajes publicados antes y después de una fecha específica. Solo usaremos publicaciones de 2 categorías para acelerar el tiempo de ejecución.

```python
categorias = ["sci.med", "sci.space"]
X_train, y_train = fetch_20newsgroups(
    random_state=1,
    subset="train",
    categorias=categorias,
    remove=("footers", "quotes"),
    return_X_y=True,
)
X_test, y_test = fetch_20newsgroups(
    random_state=1,
    subset="test",
    categorias=categorias,
    remove=("footers", "quotes"),
    return_X_y=True,
)
```
