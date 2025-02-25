# Potenzsummen-Herausforderung

## Problemstellung

Schreiben Sie eine Python-Funktion namens `sum_of_powers`, die drei Parameter annimmt:

- `end` - eine Ganzzahl, die das Ende des Bereichs (inklusiv) repräsentiert
- `power` - eine Ganzzahl, die die Potenz angibt, zu der jede Zahl im Bereich erhöht werden soll (Standardwert ist 2)
- `start` - eine Ganzzahl, die den Anfang des Bereichs repräsentiert (Standardwert ist 1)

Die Funktion sollte die Summe der Potenzen aller Zahlen von `start` bis `end` (inklusiv beider) zurückgeben.

Um dieses Problem zu lösen, können Sie die folgenden Schritte ausführen:

1. Verwenden Sie `range()` in Kombination mit einer Listenkomprehension, um eine Liste von Elementen im gewünschten Bereich zu erstellen, die zur angegebenen `power` erhöht sind.
2. Verwenden Sie `sum()`, um die Werte zusammenzuzählen.

## Beispiel

```python
sum_of_powers(10) # gibt 385 zurück
sum_of_powers(10, 3) # gibt 3025 zurück
sum_of_powers(10, 3, 5) # gibt 2925 zurück
```
