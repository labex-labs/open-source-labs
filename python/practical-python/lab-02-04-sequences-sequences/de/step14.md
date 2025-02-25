# Übung 2.15: Ein praktisches Beispiel für enumerate()

Denken Sie daran, dass die Datei `missing.csv` Daten eines Aktienportfolios enthält, aber einige Zeilen fehlende Daten haben. Verwenden Sie `enumerate()`, um Ihr `pcost.py`-Programm so zu modifizieren, dass es eine Zeilennummer mit der Warnmeldung ausgibt, wenn es auf schlechtes Eingabedata stößt.

```python
>>> cost = portfolio_cost('/home/labex/project/missing.csv')
Zeile 4: Konvertieren nicht möglich: ['MSFT', '', '51.23']
Zeile 7: Konvertieren nicht möglich: ['IBM', '', '70.44']
>>>
```

Um dies zu tun, müssen Sie einige Teile Ihres Codes ändern.

```python
...
for rowno, row in enumerate(rows, start=1):
    try:
     ...
    except ValueError:
        print(f'Zeile {rowno}: Schlechte Zeile: {row}')
```
