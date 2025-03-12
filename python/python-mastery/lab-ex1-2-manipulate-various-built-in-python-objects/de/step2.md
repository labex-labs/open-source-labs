# Arbeiten mit Python-Strings

Strings sind einer der am häufigsten verwendeten Datentypen in Python. Sie werden verwendet, um Text darzustellen und können Buchstaben, Zahlen und Symbole enthalten. In diesem Schritt werden wir verschiedene String-Operationen untersuchen, die essentielle Fähigkeiten für die Arbeit mit Textdaten in Python sind.

## Erstellen und Definieren von Strings

Um mit Strings in Python zu beginnen, müssen wir zunächst eine Python-Interaktive Shell öffnen. Diese Shell ermöglicht es uns, Python-Code Zeile für Zeile zu schreiben und auszuführen, was ideal für das Lernen und Testen ist. Öffnen Sie erneut eine Python-Interaktive Shell mit dem folgenden Befehl:

```bash
python3
```

Sobald die Shell geöffnet ist, können wir einen String definieren. In diesem Beispiel erstellen wir einen String, der Aktiensymbole enthält. Ein String in Python kann definiert werden, indem man Text in einfache Anführungszeichen (`'`) oder doppelte Anführungszeichen (`"`) einschließt. So definieren wir unseren String:

```python
>>> symbols = 'AAPL IBM MSFT YHOO SCO'
>>> symbols
'AAPL IBM MSFT YHOO SCO'
```

Wir haben jetzt eine String-Variable namens `symbols` erstellt und ihr einen Wert zugewiesen. Wenn wir den Variablennamen eingeben und Enter drücken, zeigt Python den Wert des Strings an.

## Zugriff auf Zeichen und Teilstrings

In Python können Strings indiziert werden, um einzelne Zeichen zuzugreifen. Die Indizierung beginnt bei 0, was bedeutet, dass das erste Zeichen eines Strings den Index 0 hat, das zweite den Index 1 usw. Negative Indizierung wird ebenfalls unterstützt, wobei -1 auf das letzte Zeichen, -2 auf das vorletzte Zeichen usw. verweist.

Schauen wir uns an, wie wir auf einzelne Zeichen in unserem `symbols`-String zugreifen können:

```python
>>> symbols[0]    # Erstes Zeichen
'A'
>>> symbols[1]    # Zweites Zeichen
'A'
>>> symbols[2]    # Drittes Zeichen
'P'
>>> symbols[-1]   # Letztes Zeichen
'O'
>>> symbols[-2]   # Vorletztes Zeichen
'C'
```

Wir können auch Teilstrings mithilfe von Slicing extrahieren. Slicing ermöglicht es uns, einen Teil des Strings zu erhalten, indem wir einen Start- und einen Endindex angeben. Die Syntax für Slicing ist `string[start:end]`, wobei der Teilstring die Zeichen vom Startindex bis (aber nicht einschließlich) des Endindexes enthält.

```python
>>> symbols[:4]    # Erste 4 Zeichen
'AAPL'
>>> symbols[-3:]   # Letzte 3 Zeichen
'SCO'
>>> symbols[5:8]   # Zeichen von Index 5 bis 7
'IBM'
```

## Unveränderlichkeit von Strings

Strings in Python sind unveränderlich (immutable), was bedeutet, dass Sie, sobald ein String erstellt ist, seine einzelnen Zeichen nicht ändern können. Wenn Sie versuchen, ein Zeichen in einem String zu ändern, wird Python einen Fehler ausgeben.

Versuchen wir, das erste Zeichen unseres `symbols`-Strings zu ändern:

```python
>>> symbols[0] = 'a'    # Dies wird einen Fehler verursachen
```

Sie sollten einen Fehler wie diesen sehen:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

Dieser Fehler zeigt an, dass wir einem einzelnen Zeichen in einem String keinen neuen Wert zuweisen können, da Strings unveränderlich sind.

## String-Konkatenation

Obwohl wir Strings nicht direkt ändern können, können wir neue Strings durch Konkatenation erstellen. Konkatenation bedeutet, zwei oder mehr Strings zusammenzufügen. In Python können wir den `+`-Operator verwenden, um Strings zu konkatenieren.

```python
>>> symbols += ' GOOG'    # Füge ein neues Symbol hinzu
>>> symbols
'AAPL IBM MSFT YHOO SCO GOOG'

>>> symbols = 'HPQ ' + symbols    # Füge ein neues Symbol am Anfang hinzu
>>> symbols
'HPQ AAPL IBM MSFT YHOO SCO GOOG'
```

Es ist wichtig zu beachten, dass diese Operationen neue Strings erstellen, anstatt den ursprünglichen String zu ändern. Der ursprüngliche String bleibt unverändert, und ein neuer String wird mit dem kombinierten Wert erstellt.

## Prüfen auf Teilstrings

Um zu überprüfen, ob ein Teilstring in einem String vorhanden ist, können wir den `in`-Operator verwenden. Der `in`-Operator gibt `True` zurück, wenn der Teilstring im String gefunden wird, und `False` sonst.

```python
>>> 'IBM' in symbols
True
>>> 'AA' in symbols
True
>>> 'CAT' in symbols
False
```

Beachten Sie, dass 'AA' `True` zurückgibt, weil es in "AAPL" gefunden wird. Dies ist eine nützliche Methode, um nach spezifischem Text in einem größeren String zu suchen.

## String-Methoden

Python-Strings verfügen über zahlreiche eingebaute Methoden, die es uns ermöglichen, verschiedene Operationen auf Strings auszuführen. Diese Methoden sind Funktionen, die mit dem String-Objekt verknüpft sind und mit der Punktnotation (`string.method()`) aufgerufen werden können.

```python
>>> symbols.lower()    # Konvertiere in Kleinbuchstaben
'hpq aapl ibm msft yhoo sco goog'

>>> symbols    # Ursprünglicher String bleibt unverändert
'HPQ AAPL IBM MSFT YHOO SCO GOOG'

>>> lowersyms = symbols.lower()    # Speichere das Ergebnis in einer neuen Variablen
>>> lowersyms
'hpq aapl ibm msft yhoo sco goog'

>>> symbols.find('MSFT')    # Finde den Startindex eines Teilstrings
13
>>> symbols[13:17]    # Überprüfe den Teilstring an dieser Position
'MSFT'

>>> symbols = symbols.replace('SCO','')    # Ersetze einen Teilstring
>>> symbols
'HPQ AAPL IBM MSFT YHOO  GOOG'
```

Wenn Sie mit den Experimenten fertig sind, können Sie die Python-Shell mit dem folgenden Befehl beenden:

```python
>>> exit()
```
