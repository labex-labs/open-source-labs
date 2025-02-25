# Übung 1.14: Stringverkettung

Obwohl String-Daten schreibgeschützt sind, können Sie jederzeit eine Variable neu zuweisen, um einen neu erstellten String zu erhalten.

Versuchen Sie die folgende Anweisung, die ein neues Symbol "GOOG" am Ende von `symbols` anfügt:

```python
>>> symbols = symbols + 'GOOG'
>>> symbols
'AAPL,IBM,MSFT,YHOO,SCOGOOG'
>>>
```

Ups! Das war nicht das, was Sie wollten. Beheben Sie es, so dass die Variable `symbols` den Wert `'AAPL,IBM,MSFT,YHOO,SCO,GOOG'` enthält.

```python
>>> symbols =?
>>> symbols
'AAPL,IBM,MSFT,YHOO,SCO,GOOG'
>>>
```

Fügen Sie `'HPQ'` am Anfang der Zeichenkette hinzu:

```python
>>> symbols =?
>>> symbols
'HPQ,AAPL,IBM,MSFT,YHOO,SCO,GOOG'
>>>
```

In diesen Beispielen sieht es so aus, als würde die ursprüngliche Zeichenkette modifiziert werden, was offensichtlich gegen die schreibgeschützte Natur von Zeichenketten verstößt. Tatsächlich nicht. Jede Operation auf Zeichenketten erzeugt jeweils einen völlig neuen String. Wenn die Variablenname `symbols` neu zugewiesen wird, verweist er auf den neu erstellten String. Danach wird die alte Zeichenkette zerstört, da sie nicht mehr verwendet wird.
