# Arbeiten mit Python-Wörterbüchern

In Python sind Wörterbücher (Dictionaries) eine grundlegende Datenstruktur. Sie sind Schlüssel-Wert-Speicher, was bedeutet, dass sie es Ihnen ermöglichen, einen Wert (den Wert) einem anderen (dem Schlüssel) zuordnen. Dies ist äußerst nützlich, wenn Sie mit Daten arbeiten, die natürliche Schlüssel-Wert-Beziehungen aufweisen. Beispielsweise möchten Sie möglicherweise den Namen einer Person (den Schlüssel) mit ihrem Alter (dem Wert) verknüpfen, oder wie wir in diesem Lab sehen werden, Aktiensymbole (Schlüssel) mit ihren Preisen (Werten) verknüpfen.

## Erstellen und Zugreifen auf Wörterbücher

Beginnen wir damit, eine neue Python-Interaktive Sitzung zu öffnen. Dies ist wie das Betreten einer speziellen Umgebung, in der Sie Python-Code Zeile für Zeile schreiben und ausführen können. Um diese Sitzung zu starten, öffnen Sie Ihr Terminal und geben Sie den folgenden Befehl ein:

```bash
python3
```

Sobald Sie in der Python-Interaktiven Sitzung sind, können Sie ein Wörterbuch erstellen. In unserem Fall werden wir ein Wörterbuch erstellen, das Aktiensymbole ihren Preisen zuordnet. So geht's:

```python
>>> prices = {'IBM': 91.1, 'GOOG': 490.1, 'AAPL': 312.23}
>>> prices
{'IBM': 91.1, 'GOOG': 490.1, 'AAPL': 312.23}
```

In der ersten Zeile erstellen wir ein Wörterbuch namens `prices` und weisen es einigen Schlüssel-Wert-Paaren zu. Die Schlüssel sind die Aktiensymbole (`IBM`, `GOOG`, `AAPL`), und die Werte sind die entsprechenden Preise. Die zweite Zeile zeigt uns einfach den Inhalt des `prices`-Wörterbuchs.

Jetzt sehen wir uns an, wie man die Werte im Wörterbuch mithilfe der Schlüssel zugreift und modifiziert.

```python
>>> prices['IBM']    # Greife auf den Wert für den Schlüssel 'IBM' zu
91.1

>>> prices['IBM'] = 123.45    # Aktualisiere einen vorhandenen Wert
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'AAPL': 312.23}

>>> prices['HPQ'] = 26.15    # Füge ein neues Schlüssel-Wert-Paar hinzu
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'AAPL': 312.23, 'HPQ': 26.15}
```

In der ersten Zeile greifen wir auf den Wert zu, der mit dem Schlüssel `IBM` verknüpft ist. In der zweiten und dritten Zeile aktualisieren wir den Wert für den Schlüssel `IBM` und fügen dann ein neues Schlüssel-Wert-Paar hinzu (`HPQ` mit einem Preis von `26.15`).

## Abrufen der Wörterbuchschlüssel

Manchmal möchten Sie möglicherweise eine Liste aller Schlüssel in einem Wörterbuch erhalten. Es gibt ein paar Möglichkeiten, dies zu tun.

```python
>>> list(prices)    # Konvertiere die Wörterbuchschlüssel in eine Liste
['IBM', 'GOOG', 'AAPL', 'HPQ']
```

Hier verwenden wir die `list()`-Funktion, um die Schlüssel des `prices`-Wörterbuchs in eine Liste zu konvertieren.

Sie können auch die `keys()`-Methode verwenden, die ein spezielles Objekt namens `dict_keys` zurückgibt.

```python
>>> prices.keys()    # Gibt ein dict_keys-Objekt zurück
dict_keys(['IBM', 'GOOG', 'AAPL', 'HPQ'])
```

## Abrufen der Wörterbuchwerte

In ähnlicher Weise möchten Sie möglicherweise alle Werte in einem Wörterbuch erhalten. Sie können dazu die `values()`-Methode verwenden.

```python
>>> prices.values()    # Gibt ein dict_values-Objekt zurück
dict_values([123.45, 490.1, 312.23, 26.15])
```

Diese Methode gibt ein `dict_values`-Objekt zurück, das alle Werte im `prices`-Wörterbuch enthält.

## Löschen von Einträgen

Wenn Sie ein Schlüssel-Wert-Paar aus einem Wörterbuch entfernen möchten, können Sie das `del`-Schlüsselwort verwenden.

```python
>>> del prices['AAPL']    # Lösche den Eintrag 'AAPL'
>>> prices
{'IBM': 123.45, 'GOOG': 490.1, 'HPQ': 26.15}
```

Hier löschen wir das Schlüssel-Wert-Paar mit dem Schlüssel `AAPL` aus dem `prices`-Wörterbuch.

## Prüfen, ob ein Schlüssel existiert

Um zu prüfen, ob ein Schlüssel in einem Wörterbuch existiert, können Sie den `in`-Operator verwenden.

```python
>>> 'IBM' in prices
True
>>> 'AAPL' in prices
False
```

Der `in`-Operator gibt `True` zurück, wenn der Schlüssel im Wörterbuch existiert, und `False` sonst.

## Wörterbuchmethoden

Wörterbücher haben mehrere nützliche Methoden. Schauen wir uns ein paar davon an.

```python
>>> prices.get('MSFT', 0)    # Hole den Wert oder den Standardwert, wenn der Schlüssel nicht existiert
0
>>> prices.get('IBM', 0)
123.45

>>> prices.update({'MSFT': 25.0, 'GOOG': 500.0})    # Aktualisiere mehrere Werte
>>> prices
{'IBM': 123.45, 'GOOG': 500.0, 'HPQ': 26.15, 'MSFT': 25.0}
```

Die `get()`-Methode versucht, den Wert zu erhalten, der mit einem Schlüssel verknüpft ist. Wenn der Schlüssel nicht existiert, gibt sie einen Standardwert zurück (in diesem Fall `0`). Die `update()`-Methode wird verwendet, um mehrere Schlüssel-Wert-Paare im Wörterbuch auf einmal zu aktualisieren.

Wenn Sie mit der Arbeit in der Python-Interaktiven Sitzung fertig sind, können Sie sie beenden, indem Sie eingeben:

```python
>>> exit()
```
