# Teil 3 : Listenmanipulation

Im ersten Teil haben Sie mit Zeichenketten gearbeitet, die Aktiensymbole enthielten. Beispielsweise:

```python
>>> symbols = 'HPQ AAPL IBM MSFT YHOO  GOOG'
>>>
```

Definieren Sie die obige Variable und teilen Sie sie mithilfe der `split()`-Operation von Zeichenketten in eine Liste von Namen auf:

```python
>>> symlist = symbols.split()
>>> symlist
['HPQ', 'AAPL', 'IBM', 'MSFT', 'YHOO', 'GOOG' ]
>>>
```

## Extrahieren und Neuzuweisen von Listelementen

Listen funktionieren wie Arrays, bei denen Sie Elemente nach numerischem Index auflisten und modifizieren können. Probieren Sie einige Aufrufe aus:

```python
>>> symlist[0]
'HPQ'
>>> symlist[1]
'AAPL'
>>> symlist[-1]
'GOOG'
>>> symlist[-2]
'YHOO'
>>>
```

Versuchen Sie, ein Element neu zuzuweisen:

```python
>>> symlist[2] = 'AIG'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG' ]
>>>
```

## Schleifen über Listelemente

Die `for`-Schleife arbeitet, indem sie über Daten in einer Sequenz wie einer Liste iteriert. Testen Sie dies, indem Sie die folgende Schleife eingeben und beobachten, was passiert:

```python
>>> for s in symlist:
        print('s =', s)

... schauen Sie sich die Ausgabe an...
```

## Mitgliedschaftstests

Verwenden Sie den `in`-Operator, um zu überprüfen, ob `'AIG'`, `'AA'` und `'CAT'` in der Liste von Symbolen enthalten sind.

```python
>>> 'AIG' in symlist
True
>>> 'AA' in symlist
False
>>>
```

## Anhängen, Einfügen und Löschen von Elementen

Verwenden Sie die `append()`-Methode, um das Symbol `'RHT'` am Ende von `symlist` hinzuzufügen.

```python
>>> symlist.append('RHT')
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

Verwenden Sie die `insert()`-Methode, um das Symbol `'AA'` als zweites Element in die Liste einzufügen.

```python
>>> symlist.insert(1,'AA')
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG', 'RHT']
>>>
```

Verwenden Sie die `remove()`-Methode, um `'MSFT'` aus der Liste zu entfernen.

```python
>>> symlist.remove('MSFT')
>>> symlist
['HPQ', 'AA', 'AAPL', 'AIG', 'YHOO', 'GOOG', 'RHT']
```

Versuchen Sie, `remove()` erneut aufzurufen, um zu sehen, was passiert, wenn das Element nicht gefunden werden kann.

```python
>>> symlist.remove('MSFT')
... beobachten Sie, was passiert...
>>>
```

Verwenden Sie die `index()`-Methode, um die Position von `'YHOO'` in der Liste zu finden.

```python
>>> symlist.index('YHOO')
4
>>> symlist[4]
'YHOO'
>>>
```

## Listen sortieren

Möchten Sie eine Liste sortieren? Verwenden Sie die `sort()`-Methode. Testen Sie es:

```python
>>> symlist.sort()
>>> symlist
['AA', 'AAPL', 'AIG', 'GOOG', 'HPQ', 'RHT', 'YHOO']
>>>
```

Möchten Sie in umgekehrter Reihenfolge sortieren? Probieren Sie dies:

```python
>>> symlist.sort(reverse=True)
>>> symlist
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>>
```

Hinweis: Sortieren einer Liste modifiziert deren Inhalt "in-place". Das heißt, die Elemente der Liste werden durcheinander gebracht, aber dabei wird keine neue Liste erstellt.

## Listen beliebiger Objekte

Listen können beliebige Objekte enthalten, einschließlich anderer Listen (z.B. geschachtelte Listen). Testen Sie dies:

```python
>>> nums = [101,102,103]
>>> items = [symlist, nums]
>>> items
[['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
```

Achten Sie genau auf die obige Ausgabe. `items` ist eine Liste mit zwei Elementen. Jedes Element ist eine Liste.

Versuchen Sie einige geschachtelte Listenaufrufe:

```python
>>> items[0]
['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA']
>>> items[0][1]
'RHT'
>>> items[0][1][2]
'T'
>>> items[1]
[101, 102, 103]
>>> items[1][1]
102
>>>
```
