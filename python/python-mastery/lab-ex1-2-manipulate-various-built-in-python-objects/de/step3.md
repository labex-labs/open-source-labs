# Arbeiten mit Python-Listen

Listen sind ein Typ von Datenstruktur in Python. Eine Datenstruktur ist eine Möglichkeit, Daten zu organisieren und zu speichern, damit sie effizient verwendet werden können. Listen sind sehr vielseitig, da sie verschiedene Typen von Elementen speichern können, wie Zahlen, Strings oder sogar andere Listen. In diesem Schritt werden wir lernen, wie man verschiedene Operationen auf Listen ausführt.

## Erstellen von Listen aus Strings

Um mit Python-Listen zu beginnen, müssen wir zunächst eine Python-Interaktive Sitzung öffnen. Dies ist wie eine spezielle Umgebung, in der wir sofort Python-Code schreiben und ausführen können. Um diese Sitzung zu starten, geben Sie den folgenden Befehl in Ihrem Terminal ein:

```bash
python3
```

Sobald Sie in der Python-Interaktiven Sitzung sind, werden wir eine Liste aus einem String erstellen. Ein String ist einfach eine Folge von Zeichen. Wir werden einen String definieren, der einige Aktiensymbole enthält, die durch Leerzeichen getrennt sind. Dann werden wir diesen String in eine Liste umwandeln. Jedes Aktiensymbol wird ein Element in der Liste.

```python
>>> symbols = 'HPQ AAPL IBM MSFT YHOO GOOG'
>>> symlist = symbols.split()    # Teilt den String an Leerzeichen auf
>>> symlist
['HPQ', 'AAPL', 'IBM', 'MSFT', 'YHOO', 'GOOG']
```

Die `split()`-Methode wird verwendet, um den String an jeder Stelle, an der ein Leerzeichen ist, in Teile zu zerlegen. Jeder Teil wird dann ein Element in der neuen Liste.

## Zugriff auf und Modifikation von Listenelementen

Genau wie Strings unterstützen Listen Indizierung. Indizierung bedeutet, dass wir auf einzelne Elemente in der Liste anhand ihrer Position zugreifen können. In Python hat das erste Element in einer Liste den Index 0, das zweite den Index 1 und so weiter. Wir können auch negative Indizierung verwenden, um Elemente vom Ende der Liste aus zuzugreifen. Das letzte Element hat den Index -1, das vorletzte den Index -2 und so weiter.

Im Gegensatz zu Strings können Listenelemente modifiziert werden. Dies bedeutet, dass wir den Wert eines Elements in der Liste ändern können.

```python
>>> symlist[0]    # Erstes Element
'HPQ'
>>> symlist[1]    # Zweites Element
'AAPL'
>>> symlist[-1]   # Letztes Element
'GOOG'
>>> symlist[-2]   # Vorletztes Element
'YHOO'

>>> symlist[2] = 'AIG'    # Ersetze das dritte Element
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']
```

## Iterieren durch Listen

Oft müssen wir die gleiche Operation auf jedes Element in einer Liste anwenden. Wir können dazu eine `for`-Schleife verwenden. Eine `for`-Schleife ermöglicht es uns, jedes Element in der Liste nacheinander zu durchlaufen und eine bestimmte Aktion darauf auszuführen.

```python
>>> for s in symlist:
...     print('s =', s)
...
```

Wenn Sie diesen Code ausführen, werden Sie jedes Element in der Liste mit der Bezeichnung `s =` ausgegeben sehen.

```
s = HPQ
s = AAPL
s = AIG
s = MSFT
s = YHOO
s = GOOG
```

## Prüfen auf Mitgliedschaft

Manchmal müssen wir prüfen, ob ein bestimmtes Element in einer Liste existiert. Wir können dazu den `in`-Operator verwenden. Der `in`-Operator gibt `True` zurück, wenn das Element in der Liste ist, und `False`, wenn es nicht ist.

```python
>>> 'AIG' in symlist
True
>>> 'AA' in symlist
False
>>> 'CAT' in symlist
False
```

## Hinzufügen und Entfernen von Elementen

Listen haben eingebaute Methoden, die es uns ermöglichen, Elemente hinzuzufügen und zu entfernen. Die `append()`-Methode fügt ein Element am Ende der Liste hinzu. Die `insert()`-Methode fügt ein Element an einer bestimmten Position in der Liste ein. Die `remove()`-Methode entfernt ein Element aus der Liste anhand seines Werts.

```python
>>> symlist.append('RHT')    # Füge ein Element am Ende hinzu
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']

>>> symlist.insert(1, 'AA')    # Füge an einer bestimmten Position ein
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']

>>> symlist.remove('MSFT')    # Entferne anhand des Werts
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']
```

Wenn Sie versuchen, ein Element zu entfernen, das nicht in der Liste existiert, wird Python einen Fehler ausgeben.

```python
>>> symlist.remove('MSFT')
```

Sie werden eine Fehlermeldung wie diese sehen:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```

Wir können auch die Position eines Elements in der Liste mithilfe der `index()`-Methode finden.

```python
>>> symlist.index('YHOO')
4
>>> symlist[4]    # Überprüfe das Element an dieser Position
'YHOO'
```

## Sortieren von Listen

Listen können "in-place" sortiert werden, was bedeutet, dass die ursprüngliche Liste modifiziert wird. Wir können eine Liste alphabetisch oder in umgekehrter Reihenfolge sortieren.

```python
>>> symlist.sort()    # Sortiere alphabetisch
>>> symlist
['AA', 'AAPL', 'AIG', 'GOOG', 'HPQ', 'RHT', 'YHOO']

>>> symlist.sort(reverse=True)    # Sortiere in umgekehrter Reihenfolge
>>> symlist
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
```

## Verschachtelte Listen

Listen können jedes Objekt enthalten, einschließlich anderer Listen. Dies wird eine verschachtelte Liste genannt.

```python
>>> nums = [101, 102, 103]
>>> items = [symlist, nums]
>>> items
[['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
```

Um auf Elemente in einer verschachtelten Liste zuzugreifen, verwenden wir mehrere Indizes. Der erste Index wählt das äußere Listenelement aus, und der zweite Index wählt das innere Listenelement aus.

```python
>>> items[0]    # Erstes Element (die symlist)
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> items[0][1]    # Zweites Element in symlist
'RHT'
>>> items[0][1][2]    # Drittes Zeichen in 'RHT'
'T'
>>> items[1]    # Zweites Element (die nums-Liste)
[101, 102, 103]
>>> items[1][1]    # Zweites Element in nums
102
```

Wenn Sie mit der Arbeit in der Python-Interaktiven Sitzung fertig sind, können Sie sie beenden, indem Sie eingeben:

```python
>>> exit()
```
