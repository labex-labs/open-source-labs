# Leyendo Atributos con Herencia Simple

En jerarquías de herencia, los atributos se encuentran recorriendo el árbol de herencia en orden ascendente.

```python
class A: pass
class B(A): pass
class C(A): pass
class D(B): pass
class E(D): pass
```

Con herencia simple, hay un solo camino hacia la cima. Se detiene con la primera coincidencia.
