# Typenangleichung

In der aktuellen `Stock`-Klasse gibt es eine `_types`-Klassenvariable, die die Umwandlungen angibt, wenn aus einer Datei gelesen wird, aber es gibt auch Eigenschaften, die die Typen erzwingen. Wer ist für diese Show verantwortlich? Ändern Sie die Eigenschaftsdefinitionen so, dass sie die im `_types`-Klassenvariable angegebenen Typen verwenden. Stellen Sie sicher, dass die Eigenschaften funktionieren, wenn die Typen über die Unterklassenbildung geändert werden. Beispielsweise:

```python
>>> from decimal import Decimal
>>> class DStock(Stock):
        _types = (str, int, Decimal)

>>> s = DStock('AA', 50, Decimal('91.1'))
>>> s.price = 92.3
Traceback (most recent call last):
...
TypeError: Erwartet einen Decimal
>>>
```

**Diskussion**

Die resultierende `Stock`-Klasse am Ende dieses Labs ist ein verwirrtes Gemisch aus Eigenschaften, Typüberprüfung, Konstruktoren und anderen Details. Stellen Sie sich vor, wie unangenehm es wäre, Code zu unterhalten, der dozens oder hundreds von solchen Klassendefinitionen aufwies.

Wir werden herausfinden, wie wir die Dinge erheblich vereinfachen können, aber dafür wird es einige Zeit und einige fortgeschrittene Techniken benötigen. Bleiben Sie dran.
