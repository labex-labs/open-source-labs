# MRO bei Mehrfachvererbung

Beim Mehrfachvererbung gibt es keinen einzigen Pfad zum obersten Element. Schauen wir uns ein Beispiel an.

```python
class A: pass
class B: pass
class C(A, B): pass
class D(B): pass
class E(C, D): pass
```

Was passiert, wenn Sie auf ein Attribut zugreifen?

```python
e = E()
e.attr
```

Es wird ein Attributsucheprozess durchgeführt, aber welche ist die Reihenfolge? Das ist ein Problem.

Python verwendet _kooperatives Mehrfachvererbung_, die bestimmte Regeln zur Klasseneinordnung befolgt.

- Kinder werden immer vor Eltern überprüft
- Eltern (wenn mehrere) werden immer in der aufgelisteten Reihenfolge überprüft.

Die MRO wird berechnet, indem alle Klassen in einer Hierarchie gemäß diesen Regeln sortiert werden.

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

Der zugrunde liegende Algorithmus wird als "C3 Linearization Algorithm" bezeichnet. Die genauen Details sind nicht wichtig, solange Sie sich daran erinnern, dass eine Klassenhierarchie die gleichen Einordnungsregeln befolgt, denen Sie folgen würden, wenn Ihr Haus in Flammen steht und Sie evakuieren müssen - Kinder zuerst, gefolgt von Eltern.
