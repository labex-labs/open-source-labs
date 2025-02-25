# Ganzzahl in römische Zahlen - Herausforderung

## Problemstellung

Schreiben Sie eine Funktion `to_roman_numeral(num)`, die eine Ganzzahl `num` zwischen 1 und 3999 (einschließlich) annimmt und ihre römische Zahlenrepräsentation als Zeichenfolge zurückgibt.

Um eine Ganzzahl in ihre römische Zahlenrepräsentation umzuwandeln, können Sie eine Suchliste verwenden, die Tupel im Format (römischer Wert, Ganzzahl) enthält. Anschließend können Sie eine `for-Schleife` verwenden, um über die Werte in der Suchliste zu iterieren und `divmod()` verwenden, um `num` mit dem Rest zu aktualisieren und die römische Zahlenrepräsentation zum Ergebnis hinzuzufügen.

Ihre Funktion sollte die römische Zahlenrepräsentation der eingegebenen Ganzzahl zurückgeben.

## Beispiel

```python
to_roman_numeral(3) # 'III'
to_roman_numeral(11) # 'XI'
to_roman_numeral(1998) # 'MCMXCVIII'
```
