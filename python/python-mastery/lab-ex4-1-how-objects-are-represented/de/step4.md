# Verständnis der Beziehung zwischen Klassen und Instanzen

Nun werden wir untersuchen, wie Klassen und Instanzen in Python zusammenhängen und wie die Methodensuche funktioniert. Dies ist ein wichtiges Konzept, da es Ihnen hilft zu verstehen, wie Python Methoden und Attribute findet und verwendet, wenn Sie mit Objekten arbeiten.

Zunächst überprüfen wir, zu welcher Klasse unsere Instanzen gehören. Die Kenntnis der Klasse einer Instanz ist von entscheidender Bedeutung, da sie uns sagt, wo Python nach Methoden und Attributen sucht, die sich auf diese Instanz beziehen.

```python
>>> goog.__class__
<class '__main__.SimpleStock'>
>>> ibm.__class__
<class '__main__.SimpleStock'>
```

Beide Instanzen haben eine Referenz zurück zur `SimpleStock`-Klasse. Diese Referenz ist wie ein Zeiger, den Python verwendet, wenn es Methoden suchen muss. Wenn Sie eine Methode auf einer Instanz aufrufen, verwendet Python diese Referenz, um die entsprechende Methodendefinition zu finden.

Wenn Sie eine Methode auf einer Instanz aufrufen, folgt Python diesen Schritten:

1. Es sucht nach dem Attribut im `__dict__` der Instanz. Das `__dict__` einer Instanz ist wie ein Speicherbereich, in dem alle instanzspezifischen Attribute gespeichert sind.
2. Wenn es nicht gefunden wird, überprüft es das `__dict__` der Klasse. Das `__dict__` der Klasse speichert alle Attribute und Methoden, die allen Instanzen dieser Klasse gemeinsam sind.
3. Wenn es in der Klasse gefunden wird, gibt es dieses Attribut zurück.

Lassen Sie uns dies in Aktion sehen. Zunächst überprüfen wir, ob die `cost`-Methode nicht in den Instanz-Dictionaries enthalten ist. Dieser Schritt hilft uns zu verstehen, dass die `cost`-Methode nicht für jede Instanz spezifisch ist, sondern auf Klassenebene definiert ist.

```python
>>> 'cost' in goog.__dict__
False
>>> 'cost' in ibm.__dict__
False
```

Woher kommt also die `cost`-Methode? Lassen Sie uns die Klasse überprüfen. Indem wir uns das `__dict__` der Klasse ansehen, können wir herausfinden, wo die `cost`-Methode definiert ist.

```python
>>> SimpleStock.__dict__['cost']
<function SimpleStock.cost at 0x7f...>
```

Die Methode ist in der Klasse definiert, nicht in den Instanzen. Wenn Sie `goog.cost()` aufrufen, findet Python `cost` nicht in `goog.__dict__`, sucht also in `SimpleStock.__dict__` und findet es dort.

Sie können die Methode tatsächlich direkt aus dem Klassen-Dictionary aufrufen, indem Sie die Instanz als erstes Argument übergeben (das dann `self` wird). Dies zeigt, wie Python intern Methoden aufruft, wenn Sie die normale Syntax `instanz.methode()` verwenden.

```python
>>> SimpleStock.__dict__['cost'](goog)
49010.0
>>> SimpleStock.__dict__['cost'](ibm)
4561.5
```

Das ist im Wesentlichen, was Python im Hintergrund macht, wenn Sie `goog.cost()` aufrufen.

Nun fügen wir ein Klassenattribut hinzu. Klassenattribute werden von allen Instanzen geteilt. Das bedeutet, dass alle Instanzen der Klasse auf dieses Attribut zugreifen können und es nur einmal auf Klassenebene gespeichert wird.

```python
>>> SimpleStock.exchange = 'NASDAQ'
>>> goog.exchange
'NASDAQ'
>>> ibm.exchange
'NASDAQ'
```

Beide Instanzen können auf das `exchange`-Attribut zugreifen, aber es ist nicht in ihren individuellen Dictionaries gespeichert. Lassen Sie uns dies überprüfen, indem wir die Instanz- und Klassen-Dictionaries überprüfen.

```python
>>> 'exchange' in goog.__dict__
False
>>> 'exchange' in SimpleStock.__dict__
True
>>> SimpleStock.__dict__['exchange']
'NASDAQ'
```

Dies zeigt, dass:

1. Klassenattribute von allen Instanzen geteilt werden. Alle Instanzen können auf dasselbe Klassenattribut zugreifen, ohne ihre eigene Kopie zu haben.
2. Python überprüft zunächst das Instanz-Dictionary und dann das Klassen-Dictionary. Dies ist die Reihenfolge, in der Python nach Attributen sucht, wenn Sie versuchen, auf sie in einer Instanz zuzugreifen.
3. Klassen fungieren als Repository für geteilte Daten und Verhalten (Methoden). Die Klasse speichert alle gemeinsamen Attribute und Methoden, die von allen ihren Instanzen verwendet werden können.

Wenn wir ein Instanzattribut mit demselben Namen ändern, überdeckt es das Klassenattribut. Das bedeutet, dass wenn Sie auf das Attribut in dieser Instanz zugreifen, Python den instanzspezifischen Wert anstelle des Werts auf Klassenebene verwenden wird.

```python
>>> ibm.exchange = 'NYSE'
>>> ibm.exchange
'NYSE'
>>> goog.exchange  # Noch immer das Klassenattribut
'NASDAQ'
>>> ibm.__dict__['exchange']
'NYSE'
```

Jetzt hat `ibm` sein eigenes `exchange`-Attribut, das das Klassenattribut überdeckt, während `goog` weiterhin das Klassenattribut verwendet.
