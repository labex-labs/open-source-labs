# Teil 2 : Zeichenkettenmanipulation

Definieren Sie eine Zeichenkette, die eine Reihe von Aktiensymbole enthält, wie folgt:

```python
>>> symbols = 'AAPL IBM MSFT YHOO SCO'
```

Lassen Sie uns nun mit verschiedenen Zeichenkettenoperationen experimentieren:

## Extrahieren einzelner Zeichen und Teilzeichenketten

Zeichenketten sind Arrays von Zeichen. Versuchen Sie, einige Zeichen zu extrahieren:

```python
>>> symbols[0]
'A'
>>> symbols[1]
'A'
>>> symbols[2]
'P'
>>> symbols[-1]        # Letztes Zeichen
'O'
>>> symbols[-2]        # Zweites vorletztes Zeichen
'C'
>>>
```

Versuchen Sie, einige Slices zu nehmen:

```python
>>> symbols[:4]
'AAPL'
>>> symbols[-3:]
'SCO'
>>> symbols[5:8]
'IBM'
>>>
```

## Zeichenketten als schreibgeschützte Objekte

Zeichenketten sind schreibgeschützt. Verifizieren Sie dies, indem Sie versuchen, das erste Zeichen von `symbols` in einen Kleinbuchstaben 'a' umzuwandeln.

```python
>>> symbols[0] = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
```

## Zeichenkettenverkettung

Obwohl Zeichenkettendaten schreibgeschützt sind, können Sie jederzeit eine Variable neu zuweisen, um eine neu erstellte Zeichenkette zu erhalten. Versuchen Sie den folgenden Ausdruck, der ein neues Symbol "GOOG" am Ende von `symbols` anhängt:

```python
>>> symbols += ' GOOG'
>>> symbols
... schauen Sie sich das Ergebnis an...
```

Versuchen Sie nun, "HPQ" am Anfang von `symbols` hinzuzufügen, wie folgt:

```python
>>> symbols = 'HPQ'+ symbols
>>> symbols
... schauen Sie sich das Ergebnis an...
```

Es sollte in beiden dieser Beispiele bemerkt werden, dass die ursprüngliche Zeichenkette `symbols` _NICHT_ "in-place" geändert wird. Stattdessen wird eine völlig neue Zeichenkette erstellt. Der Variablennamen `symbols` wird lediglich an das Ergebnis gebunden. Danach wird die alte Zeichenkette zerstört, da sie nicht mehr verwendet wird.

## Mitgliedschaftstest (Teilzeichenkettenprüfung)

Experimentieren Sie mit dem `in`-Operator, um nach Teilzeichenketten zu suchen. Am interaktiven Prompt können Sie diese Operationen ausprobieren:

```python
>>> 'IBM' in symbols
True
>>> 'AA' in symbols
True
>>> 'CAT' in symbols
False
>>>
```

Stellen Sie sicher, dass Sie verstehen, warum die Prüfung auf "AA" `True` zurückgegeben hat.

## Zeichenkettenmethoden

Am Python-interaktiven Prompt können Sie versuchen, einige Zeichenkettenmethoden auszuprobieren.

```python
>>> symbols.lower()
'hpq aapl ibm msft yhoo sco goog'
>>> symbols
'HPQ AAPL IBM MSFT YHOO SCO GOOG'
```

Denken Sie daran, dass Zeichenketten immer schreibgeschützt sind. Wenn Sie das Ergebnis einer Operation speichern möchten, müssen Sie es in eine Variable ablegen:

```python
>>> lowersyms = symbols.lower()
>>> lowersyms
'hpq aapl ibm msft yhoo sco goog'
>>>
```

Versuchen Sie einige weitere Operationen:

```python
>>> symbols.find('MSFT')
13
>>> symbols[13:17]
'MSFT'
>>> symbols = symbols.replace('SCO','')
>>> symbols
'HPQ AAPL IBM MSFT YHOO  GOOG'
>>>
```
