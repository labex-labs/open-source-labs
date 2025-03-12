# Hinzufügen und Ändern von Objektattributen

In Python werden Objekte auf der Grundlage von Dictionaries implementiert. Diese Implementierung verleiht Python eine hohe Flexibilität bei der Behandlung von Objektattributen. Im Gegensatz zu einigen anderen Programmiersprachen beschränkt Python die Attribute eines Objekts nicht nur auf diejenigen, die in seiner Klasse definiert sind. Das bedeutet, dass Sie einem Objekt jederzeit neue Attribute hinzufügen können, auch nachdem das Objekt erstellt wurde.

Lassen Sie uns diese Flexibilität erkunden, indem wir einem unserer Objekte ein neues Attribut hinzufügen. Nehmen wir an, wir haben eine Instanz namens `goog` einer Klasse. Wir fügen ihr ein `date`-Attribut hinzu:

```python
>>> goog.date = "6/11/2007"
>>> goog.__dict__
{'name': 'GOOG', 'shares': 100, 'price': 490.1, 'date': '6/11/2007'}
```

Hier haben wir ein neues Attribut `date` zur `goog`-Instanz hinzugefügt. Beachten Sie, dass dieses `date`-Attribut in der `SimpleStock`-Klasse nicht definiert war. Dieses neue Attribut existiert nur in der `goog`-Instanz. Um dies zu bestätigen, überprüfen wir die `ibm`-Instanz:

```python
>>> ibm.__dict__
{'name': 'IBM', 'shares': 50, 'price': 91.23}
>>> hasattr(ibm, 'date')
False
```

Wie wir sehen können, hat die `ibm`-Instanz kein `date`-Attribut. Dies zeigt drei wichtige Eigenschaften von Python-Objekten:

1. Jede Instanz hat ihre eigene eindeutige Menge an Attributen.
2. Attributen können einem Objekt nach seiner Erstellung hinzugefügt werden.
3. Das Hinzufügen eines Attributs zu einer Instanz wirkt sich nicht auf andere Instanzen aus.

Jetzt versuchen wir eine andere Möglichkeit, ein Attribut hinzuzufügen. Anstatt die Punktnotation zu verwenden, manipulieren wir direkt das zugrunde liegende Dictionary des Objekts. In Python hat jedes Objekt ein spezielles Attribut `__dict__`, das alle seine Attribute als Schlüssel-Wert-Paare speichert.

```python
>>> goog.__dict__['time'] = '9:45am'
>>> goog.time
'9:45am'
>>> goog.__dict__
{'name': 'GOOG', 'shares': 100, 'price': 490.1, 'date': '6/11/2007', 'time': '9:45am'}
```

Indem wir das `__dict__`-Dictionary direkt modifizieren, haben wir ein neues Attribut `time` zur `goog`-Instanz hinzugefügt. Wenn wir auf `goog.time` zugreifen, sucht Python nach dem 'time'-Schlüssel im `__dict__`-Dictionary und gibt den entsprechenden Wert zurück.

Diese Beispiele zeigen, dass Python-Objekte im Wesentlichen Dictionaries mit einigen zusätzlichen Funktionen sind. Die Flexibilität von Python-Objekten ermöglicht dynamische Modifikationen, was in der Programmierung sehr leistungsstark und praktisch ist.
