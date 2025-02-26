# Módulo `itertools`

El `itertools` es un módulo de la biblioteca con varias funciones diseñadas para ayudar con iteradores/generadores.

```python
itertools.chain(s1,s2)
itertools.count(n)
itertools.cycle(s)
itertools.dropwhile(predicate, s)
itertools.groupby(s)
itertools.ifilter(predicate, s)
itertools.imap(function, s1,... sN)
itertools.repeat(s, n)
itertools.tee(s, ncopies)
itertools.izip(s1,..., sN)
```

Todas las funciones procesan los datos de forma iterativa. Implementan varios tipos de patrones de iteración.

Más información en el tutorial [Generator Tricks for Systems Programmers](http://www.dabeaz.com/generators/) de PyCon '08.

En los ejercicios anteriores, escribió un código que seguía las líneas que se escribían en un archivo de registro y las analizaba en una secuencia de filas. Este ejercicio continúa construyendo sobre eso. Asegúrese de que `stocksim.py` siga en ejecución.
