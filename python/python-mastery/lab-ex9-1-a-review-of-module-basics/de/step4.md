# from module import

Starten Sie Python neu und importieren Sie ein ausgewähltes Symbol aus einem Modul.

```python
>>> ############### [ RESTART ] ###############
>>> from simplemod import foo
simplemod geladen
>>> foo()
x ist 42
>>>
```

Beobachten Sie, wie dies das gesamte Modul geladen hat (achten Sie auf die Ausgabe der print-Funktion und wie die Variable `x` verwendet wird).

Wenn Sie `from` verwenden, ist das Modulobjekt selbst nicht sichtbar. Beispielsweise:

```python
>>> simplemod.foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name'simplemod' is not defined
>>>
```

Stellen Sie sicher, dass Sie verstehen, dass wenn Sie Dinge aus einem Modul exportieren, es sich lediglich um Namensreferenzen handelt. Beispielsweise: Versuchen Sie dies und erklären Sie es:

```python
>>> from simplemod import x,foo
>>> x
42
>>> foo()
x ist 42
>>> x = 13
>>> foo()
x ist 42                   #!! Bitte erklären
>>> x
13
>>>
```
