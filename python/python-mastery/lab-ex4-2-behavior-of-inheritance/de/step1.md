# Die Richtungen der Vererbung

Python hat zwei verschiedene "Richtungen" der Vererbung. Die erste findet sich im Konzept der "einfachen Vererbung", bei der eine Reihe von Klassen von einem einzigen Elternteil erben. Beispielsweise probieren Sie dieses Beispiel:

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

Beobachten Sie, dass das `__mro__`-Attribut der Klasse `C` alle seine Vorfahren in der richtigen Reihenfolge codiert. Wenn Sie die `spam()`-Methode aufrufen, läuft es die MRO Klasse für Klasse auf der Hierarchie entlang.

Beim Mehrfachvererbung erhalten Sie eine andere Art der Vererbung, die es ermöglicht, verschiedene Klassen zusammenzusetzen. Versuchen Sie dieses Beispiel:

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

Bemerken Sie, dass alle oben genannten Klassen von einem gemeinsamen Elternteil `Base` erben. Die Klassen `X`, `Y` und `Z` sind jedoch nicht direkt miteinander verwandt (es gibt keine Vererbungslinie, die diese Klassen miteinander verknüpft).

Beobachten Sie jedoch, was passiert bei der Mehrfachvererbung:

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

Hier sehen Sie, dass alle Klassen in der von der Unterklasse angegebenen Reihenfolge zusammen gestapelt werden. Nehmen Sie an, die Unterklasse ändert die Klassenreihenfolge:

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

Hier sehen Sie, dass die Reihenfolge der Eltern umgedreht wird. Achten Sie genau darauf, was `super()` in beiden Fällen tut. Es delegiert nicht an den unmittelbaren Elternteil jeder Klasse - stattdessen springt es zur nächsten Klasse in der MRO. Nicht nur das, die genaue Reihenfolge wird von der Kindklasse kontrolliert. Dies ist ziemlich seltsam.

Beachten Sie auch, dass der gemeinsame Elternteil `Base` dazu dient, die Kette der `super()`-Operationen zu beenden. Genauer gesagt ruft die `Base.spam()`-Methode keine weiteren Methoden auf. Es erscheint auch am Ende der MRO, da es der Elternteil aller zusammenzusetzenden Klassen ist.
