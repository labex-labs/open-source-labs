# Vuelta a la memoria

En los datos del autobús CTA, determinamos que había 181 rutas de autobús únicas.

```python
>>> routes = { row['route'] for row in rows }
>>> len(routes)
181
>>>
```

Pregunta: ¿Cuántos objetos de cadena de ruta únicos se encuentran en los datos de viajes? En lugar de crear un conjunto de rutas, crea un conjunto de identificadores de objeto en su lugar:

```python
>>> routeids = { id(row['route']) for row in rows }
>>> len(routeids)
542305
>>>
```

Piensa un momento en esto: solo hay 181 nombres de ruta distintos, pero la lista resultante de diccionarios contiene 542305 cadenas de ruta diferentes. Quizás esto se podría corregir con un poco de caché o reutilización de objetos. Resulta que Python tiene una función que se puede usar para cachear cadenas, `sys.intern()`. Por ejemplo:

```python
>>> a = 'hello world'
>>> b = 'hello world'
>>> a is b
False
>>> import sys
>>> a = sys.intern(a)
>>> b = sys.intern(b)
>>> a is b
True
>>>
```

Reinicie Python y pruebe esto:

````python
>>> # ------------------ RESTART ---------```
>>> import tracemalloc
>>> tracemalloc.start()
>>> from sys import intern
>>> import reader
>>> rows = reader.read_csv_as_dicts('ctabus.csv', [intern, str, str, int])
>>> routeids = { id(row['route']) for row in rows }
>>> len(routeids)
181
>>>
````

Eche un vistazo al uso de memoria.

```python
>>> tracemalloc.get_traced_memory()
... look at result...
>>>
```

La memoria debería bajar bastante. Observación: También hay mucha repetición en lo que respecta a las fechas. ¿Qué pasa si también se cachean las cadenas de fecha?

````python
>>> # ------------------ RESTART ---------```
>>> import tracemalloc
>>> tracemalloc.start()
>>> from sys import intern
>>> import reader
>>> rows = reader.read_csv_as_dicts('ctabus.csv', [intern, intern, str, int])
>>> tracemalloc.get_traced_memory()
... look at result...
>>>
````
