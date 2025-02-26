# MRO en Herencia Múltiple

Con herencia múltiple, no hay un solo camino hacia la cima. Echemos un vistazo a un ejemplo.

```python
class A: pass
class B: pass
class C(A, B): pass
class D(B): pass
class E(C, D): pass
```

¿Qué pasa cuando se accede a un atributo?

```python
e = E()
e.attr
```

Se lleva a cabo un proceso de búsqueda de atributos, pero ¿cuál es el orden? Ese es el problema.

Python utiliza la _herencia múltiple cooperativa_ que obedece algunas reglas sobre el orden de las clases.

- Los hijos siempre se comprueban antes que los padres
- Los padres (si hay varios) siempre se comprueban en el orden en que se listan.

El MRO se calcula ordenando todas las clases de una jerarquía de acuerdo con esas reglas.

```python
>>> E.__mro__
(
  <class 'E'>,
  <class 'C'>,
  <class 'A'>,
  <class 'D'>,
  <class 'B'>,
  <class 'object'>)
>>>
```

El algoritmo subyacente se llama "Algoritmo de Linealización C3". Los detalles precisos no son importantes siempre y cuando recuerdes que una jerarquía de clases obedece las mismas reglas de orden que seguirías si tu casa estuviera en llamas y tuvieras que evacuar: los hijos primero, seguidos de los padres.
