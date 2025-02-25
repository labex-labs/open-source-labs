# Übung 1.19: Extrahieren und Neuzuweisen von Listelementen

Versuchen Sie einige Zugriffe:

```python
>>> symlist[0]
'HPQ'
>>> symlist[1]
'AAPL'
>>> symlist[-1]
'GOOG'
>>> symlist[-2]
'DOA'
>>>
```

Versuchen Sie, einen Wert neu zuzuweisen:

```python
>>> symlist[2] = 'AIG'
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'DOA', 'GOOG']
>>>
```

Nehmen Sie einige Slices:

```python
>>> symlist[0:3]
['HPQ', 'AAPL', 'AIG']
>>> symlist[-2:]
['DOA', 'GOOG']
>>>
```

Erstellen Sie eine leere Liste und fügen Sie einem Element hinzu.

```python
>>> mysyms = []
>>> mysyms.append('GOOG')
>>> mysyms
['GOOG']
```

Sie können einen Teil einer Liste an eine andere Liste neu zuweisen. Beispielsweise:

```python
>>> symlist[-2:] = mysyms
>>> symlist
['HPQ', 'AAPL', 'AIG', 'MSFT', 'YHOO', 'GOOG']
>>>
```

Wenn Sie dies tun, wird die Liste auf der linken Seite (`symlist`) entsprechend vergrößert oder verkleinert, um die rechte Seite (`mysyms`) zu passen. Beispielsweise wurden in obigem Beispiel die letzten beiden Elemente von `symlist` durch das einzelne Element in der Liste `mysyms` ersetzt.
