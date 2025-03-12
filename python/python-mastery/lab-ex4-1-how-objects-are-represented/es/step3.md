# Agregar y modificar atributos de objetos

En Python, los objetos se implementan basados en diccionarios. Esta implementación le otorga a Python un alto grado de flexibilidad al tratar con atributos de objetos. A diferencia de algunos otros lenguajes de programación, Python no limita los atributos de un objeto solo a aquellos definidos en su clase. Esto significa que puedes agregar nuevos atributos a un objeto en cualquier momento, incluso después de que el objeto haya sido creado.

Exploremos esta flexibilidad agregando un nuevo atributo a una de nuestras instancias. Supongamos que tenemos una instancia llamada `goog` de una clase. Agregaremos un atributo `date` a ella:

```python
>>> goog.date = "6/11/2007"
>>> goog.__dict__
{'name': 'GOOG', 'shares': 100, 'price': 490.1, 'date': '6/11/2007'}
```

Aquí, agregamos un nuevo atributo `date` a la instancia `goog`. Observe que este atributo `date` no estaba definido en la clase `SimpleStock`. Este nuevo atributo existe solo en la instancia `goog`. Para confirmar esto, veamos la instancia `ibm`:

```python
>>> ibm.__dict__
{'name': 'IBM', 'shares': 50, 'price': 91.23}
>>> hasattr(ibm, 'date')
False
```

Como podemos ver, la instancia `ibm` no tiene el atributo `date`. Esto muestra tres características importantes de los objetos de Python:

1. Cada instancia tiene su propio conjunto único de atributos.
2. Los atributos se pueden agregar a un objeto después de que haya sido creado.
3. Agregar un atributo a una instancia no afecta a otras instancias.

Ahora, probemos una forma diferente de agregar un atributo. En lugar de usar la notación de punto, manipularemos directamente el diccionario subyacente del objeto. En Python, cada objeto tiene un atributo especial `__dict__` que almacena todos sus atributos como pares clave - valor.

```python
>>> goog.__dict__['time'] = '9:45am'
>>> goog.time
'9:45am'
>>> goog.__dict__
{'name': 'GOOG', 'shares': 100, 'price': 490.1, 'date': '6/11/2007', 'time': '9:45am'}
```

Al modificar directamente el diccionario `__dict__`, agregamos un nuevo atributo `time` a la instancia `goog`. Cuando accedemos a `goog.time`, Python busca la clave 'time' en el diccionario `__dict__` y devuelve su valor correspondiente.

Estos ejemplos ilustran que los objetos de Python son esencialmente diccionarios con algunas características adicionales. La flexibilidad de los objetos de Python permite una modificación dinámica, lo cual es muy poderoso y conveniente en la programación.
