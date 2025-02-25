# Ganzzahl in römische Zahlen

Schreiben Sie eine Funktion `to_roman_numeral(num)`, die eine Ganzzahl `num` zwischen 1 und 3999 (einschließlich) nimmt und ihre römische Zahlenrepräsentation als Zeichenfolge zurückgibt.

Um eine Ganzzahl in ihre römische Zahlenrepräsentation umzuwandeln, können Sie eine Suchliste verwenden, die Tupel im Format (römischer Wert, Ganzzahl) enthält. Anschließend können Sie eine `for-Schleife` verwenden, um über die Werte in der Suchliste zu iterieren und `divmod()` verwenden, um `num` mit dem Rest zu aktualisieren und die römische Zahlenrepräsentation zum Ergebnis hinzuzufügen.

Ihre Funktion sollte die römische Zahlenrepräsentation der eingegebenen Ganzzahl zurückgeben.

```python
def to_roman_numeral(num):
  lookup = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I'),
  ]
  res = ''
  for (n, roman) in lookup:
    (d, num) = divmod(num, n)
    res += roman * d
  return res
```

```python
to_roman_numeral(3) # 'III'
to_roman_numeral(11) # 'XI'
to_roman_numeral(1998) # 'MCMXCVIII'
```
