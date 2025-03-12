# Speicherzuweisung von Wörterbüchern

In Python sind Wörterbücher (Dictionaries) genauso wie Listen eine grundlegende Datenstruktur. Ein wichtiger Aspekt, den man verstehen sollte, ist, wie sie Speicher zuweisen. Die Speicherzuweisung bezieht sich darauf, wie Python im Computer-Speicher Platz reserviert, um die Daten in Ihrem Wörterbuch zu speichern. Ähnlich wie Listen weisen Python-Wörterbücher auch Speicher in Blöcken zu. Lassen Sie uns untersuchen, wie die Speicherzuweisung bei Wörterbüchern funktioniert.

1. Zunächst müssen wir ein Wörterbuch erstellen, mit dem wir arbeiten können. In derselben Python-Shell (oder öffnen Sie eine neue, wenn Sie die alte geschlossen haben) erstellen wir ein Wörterbuch, das einen Datensatz darstellt. Ein Wörterbuch in Python ist eine Sammlung von Schlüssel-Wert-Paaren, wobei jeder Schlüssel eindeutig ist und zum Zugriff auf den entsprechenden Wert verwendet wird.

```python
import sys  # Import sys if you're starting a new session
row = {'route': '22', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354}
```

Hier haben wir das Modul `sys` importiert, das Zugang zu einigen Variablen bietet, die vom Python-Interpreter verwendet oder verwaltet werden, sowie zu Funktionen, die stark mit dem Interpreter interagieren. Anschließend haben wir ein Wörterbuch namens `row` mit vier Schlüssel-Wert-Paaren erstellt.

2. Nun, da wir unser Wörterbuch haben, möchten wir seine anfängliche Größe überprüfen. Die Größe eines Wörterbuchs bezieht sich auf die Menge an Speicher, die es im Computer belegt.

```python
sys.getsizeof(row)
```

Die Funktion `sys.getsizeof()` gibt die Größe eines Objekts in Bytes zurück. Wenn Sie diesen Code ausführen, sollten Sie einen Wert um die `240` Bytes sehen. Dies gibt Ihnen eine Vorstellung davon, wie viel Speicher das Wörterbuch anfänglich beansprucht.

3. Als Nächstes fügen wir dem Wörterbuch neue Schlüssel-Wert-Paare hinzu und beobachten, wie sich die Speicherzuweisung ändert. Das Hinzufügen von Elementen zu einem Wörterbuch ist eine häufige Operation, und es ist wichtig zu verstehen, wie sie sich auf den Speicher auswirkt.

```python
row['a'] = 1
sys.getsizeof(row)  # Size might remain the same

row['b'] = 2
sys.getsizeof(row)  # Size may increase
```

Wenn Sie das erste Schlüssel-Wert-Paar (`'a': 1`) hinzufügen, kann die Größe des Wörterbuchs gleich bleiben. Dies liegt daran, dass Python bereits einen bestimmten Speicherblock zugewiesen hat und möglicherweise genügend Platz in diesem Block für das neue Element vorhanden ist. Wenn Sie jedoch das zweite Schlüssel-Wert-Paar (`'b': 2`) hinzufügen, kann die Größe zunehmen. Sie werden feststellen, dass die Größe des Wörterbuchs plötzlich zunimmt, nachdem eine bestimmte Anzahl von Elementen hinzugefügt wurde. Dies liegt daran, dass Wörterbücher wie Listen Speicher in Blöcken zuweisen, um die Leistung zu optimieren. Das Zuweisen von Speicher in Blöcken reduziert die Anzahl der Mal, in denen Python vom System mehr Speicher anfordern muss, was den Prozess des Hinzufügens neuer Elemente beschleunigt.

4. Versuchen wir, ein Element aus dem Wörterbuch zu entfernen, um zu sehen, ob der Speicherverbrauch sinkt. Das Entfernen von Elementen aus einem Wörterbuch ist ebenfalls eine häufige Operation, und es ist interessant zu sehen, wie es sich auf den Speicher auswirkt.

```python
del row['b']
sys.getsizeof(row)
```

Interessanterweise reduziert das Entfernen eines Elements normalerweise nicht die Speicherzuweisung. Dies liegt daran, dass Python den zugewiesenen Speicher beibehält, um eine erneute Speicherzuweisung zu vermeiden, wenn erneut Elemente hinzugefügt werden. Die erneute Speicherzuweisung ist in Bezug auf die Leistung eine relativ teure Operation, daher versucht Python, sie so weit wie möglich zu vermeiden.

**Überlegungen zur Speichereffizienz:**

Wenn Sie mit großen Datensätzen arbeiten, bei denen Sie viele Datensätze erstellen müssen, ist die Verwendung von Wörterbüchern für jeden Datensatz möglicherweise nicht der speichereffizienteste Ansatz. Wörterbücher sind sehr flexibel und einfach zu verwenden, aber sie können eine beträchtliche Menge an Speicher verbrauchen, insbesondere wenn es um eine große Anzahl von Datensätzen geht. Hier sind einige Alternativen, die weniger Speicher verbrauchen:

- Tupel: Einfache unveränderliche Sequenzen. Ein Tupel ist eine Sammlung von Werten, die nach der Erstellung nicht geändert werden können. Es verbraucht weniger Speicher als ein Wörterbuch, da es keine Schlüssel speichern und die zugehörige Schlüssel-Wert-Zuordnung verwalten muss.
- Benannte Tupel (Named tuples): Tupel mit Feldnamen. Benannte Tupel sind ähnlich wie normale Tupel, aber sie ermöglichen es Ihnen, die Werte anhand des Namens zuzugreifen, was den Code lesbarer machen kann. Sie verbrauchen auch weniger Speicher als Wörterbücher.
- Klassen mit `__slots__`: Klassen, die explizit Attribute definieren, um die Verwendung eines Wörterbuchs für Instanzvariablen zu vermeiden. Wenn Sie `__slots__` in einer Klasse verwenden, erstellt Python kein Wörterbuch, um die Instanzvariablen zu speichern, was den Speicherverbrauch reduziert.

Diese Alternativen können den Speicherverbrauch bei der Verarbeitung vieler Datensätze erheblich reduzieren.
