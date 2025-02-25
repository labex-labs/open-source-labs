# Summe der Potenzen

Schreiben Sie eine Python-Funktion namens `sum_of_powers`, die drei Parameter annimmt:

- `end` - eine Ganzzahl, die das Ende des Bereichs (inklusive) repräsentiert
- `power` - eine Ganzzahl, die die Potenz angibt, zu der jede Zahl im Bereich erhöht werden soll (Standardwert ist 2)
- `start` - eine Ganzzahl, die den Anfang des Bereichs repräsentiert (Standardwert ist 1)

Die Funktion sollte die Summe der Potenzen aller Zahlen von `start` bis `end` (inklusive beider) zurückgeben.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Verwenden Sie `range()` in Kombination mit einer Listenkomprehension, um eine Liste von Elementen im gewünschten Bereich zu erstellen, die zur angegebenen `power` erhöht sind.
2. Verwenden Sie `sum()`, um die Werte zusammenzuzählen.

```python
def sum_of_powers(end, power = 2, start = 1):
  return sum([(i) ** power for i in range(start, end + 1)])
```

```python
sum_of_powers(10) # 385
sum_of_powers(10, 3) # 3025
sum_of_powers(10, 3, 5) # 2925
```
