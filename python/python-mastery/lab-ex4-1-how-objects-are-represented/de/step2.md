# Erkundung des internen Dictionaries von Objekten

In Python sind Objekte ein grundlegendes Konzept. Ein Objekt kann als ein Behälter angesehen werden, der Daten enthält und bestimmte Verhaltensweisen hat. Einer der interessanten Aspekte von Python-Objekten ist die Art und Weise, wie sie ihre Attribute speichern. Attribute sind wie Variablen, die zu einem Objekt gehören. Python speichert diese Attribute in einem speziellen Dictionary, auf das über das `__dict__`-Attribut zugegriffen werden kann. Dieses Dictionary ist ein interner Bestandteil des Objekts, und hier hält Python alle Daten, die mit diesem Objekt verbunden sind, fest.

Schauen wir uns diese interne Struktur genauer an, indem wir unsere `SimpleStock`-Instanzen verwenden. In Python ist eine Instanz ein individuelles Objekt, das aus einer Klasse erstellt wird. Wenn beispielsweise `SimpleStock` eine Klasse ist, sind `goog` und `ibm` Instanzen dieser Klasse.

Um das interne Dictionary dieser Instanzen zu sehen, können wir die Python interaktive Shell verwenden. Die Python interaktive Shell ist ein ausgezeichnetes Werkzeug, um schnell Code zu testen und die Ergebnisse zu sehen. Geben Sie in der Python interaktiven Shell die folgenden Befehle ein, um das `__dict__`-Attribut unserer Instanzen zu untersuchen:

```python
>>> goog.__dict__
{'name': 'GOOG', 'shares': 100, 'price': 490.1}
>>> ibm.__dict__
{'name': 'IBM', 'shares': 50, 'price': 91.23}
```

Wenn Sie diese Befehle ausführen, zeigt die Ausgabe, dass jede Instanz ihr eigenes internes Dictionary hat. Dieses Dictionary enthält alle Instanzattribute. Beispielsweise werden im `goog`-Objekt die Attribute `name`, `shares` und `price` zusammen mit ihren entsprechenden Werten im Dictionary gespeichert. So implementiert Python Objektattribute im Hintergrund. Jedes Objekt hat ein privates Dictionary, das alle seine Attribute enthält.

Es ist wichtig zu verstehen, was das `__dict__`-Attribut über die interne Implementierung unserer Objekte verrät:

1. Die Schlüssel im Dictionary entsprechen den Attributnamen. Beispielsweise entspricht im `goog`-Objekt der Schlüssel `'name'` dem `name`-Attribut des Objekts.
2. Die Werte im Dictionary sind die Attributwerte. Der Wert `'GOOG'` ist also der Wert des `name`-Attributs für die `goog`-Instanz.
3. Jede Instanz hat ihr eigenes separates `__dict__`. Dies bedeutet, dass die Attribute einer Instanz unabhängig von den Attributen einer anderen Instanz sind. Beispielsweise kann das `shares`-Attribut der `goog`-Instanz von dem `shares`-Attribut der `ibm`-Instanz unterschiedlich sein.

Dieser auf einem Dictionary basierende Ansatz ermöglicht es Python, mit Objekten sehr flexibel zu sein. Wie wir im nächsten Schritt sehen werden, können wir diese Flexibilität nutzen, um Objektattribute auf verschiedene Weise zu ändern und darauf zuzugreifen.
