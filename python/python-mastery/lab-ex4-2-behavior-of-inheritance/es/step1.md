# Las direcciones de la herencia

Python tiene dos "direcciones" diferentes de herencia. La primera se encuentra en el concepto de "herencia simple" donde una serie de clases heredan de un solo padre. Por ejemplo, pruebe este ejemplo:

```python
>>> class A:
        def spam(self):
            print('A.spam')

>>> class B(A):
        def spam(self):
            print('B.spam')
            super().spam()

>>> class C(B):
        def spam(self):
            print('C.spam')
            super().spam()


>>> C.__mro__
(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
>>> c = C()
>>> c.spam()
C.spam
B.spam
A.spam
>>>
```

Observe que el atributo `__mro__` de la clase `C` codifica a todos sus ancestros en orden. Cuando se invoca el método `spam()`, recorre la jerarquía clase por clase siguiendo el MRO.

Con la herencia múltiple, se obtiene un tipo diferente de herencia que permite que diferentes clases se combinen. Pruebe este ejemplo:

```python
>>> class Base:
        def spam(self):
            print('Base.spam')

>>> class X(Base):
        def spam(self):
            print('X.spam')
            super().spam()

>>> class Y(Base):
        def spam(self):
            print('Y.spam')
            super().spam()

>>> class Z(Base):
        def spam(self):
            print('Z.spam')
            super().spam()

>>>
```

Tenga en cuenta que todas las clases anteriores heredan de un padre común `Base`. Sin embargo, las clases `X`, `Y` y `Z` no están directamente relacionadas entre sí (no hay una cadena de herencia que las una).

Sin embargo, observe lo que sucede en la herencia múltiple:

```python
>>> class M(X,Y,Z):
        pass

>>> M.__mro__
(<class '__main__.M'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class '__main__.Base'>, <class 'object'>)
>>> m = M()
>>> m.spam()
X.spam
Y.spam
Z.spam
Base.spam
>>>
```

Aquí, se ven todas las clases apiladas juntas en el orden proporcionado por la subclase. Suponga que la subclase reordena el orden de las clases:

```python
>>> class N(Z,Y,X):
        pass

>>> N.__mro__
(<class '__main__.N'>, <class '__main__.Z'>, <class '__main__.Y'>, <class '__main__.X'>, <class '__main__.Base'>, <class 'object'>)
>>> n = N()
>>> n.spam()
Z.spam
Y.spam
X.spam
Base.spam
>>>
```

Aquí, se ve que el orden de los padres se invierte. Presta atención cuidadosamente a lo que está haciendo `super()` en ambos casos. No delega en el padre inmediato de cada clase, sino que se mueve a la siguiente clase en el MRO. No solo eso, el orden exacto está controlado por el hijo. Esto es bastante extraño.

También observe que el padre común `Base` sirve para terminar la cadena de operaciones de `super()`. Específicamente, el método `Base.spam()` no llama a ningún método más. También aparece al final del MRO ya que es el padre de todas las clases que se están combinando.
