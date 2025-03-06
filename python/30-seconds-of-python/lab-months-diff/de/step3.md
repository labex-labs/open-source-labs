# Testen mit verschiedenen Datenszenarien

Um besser zu verstehen, wie unsere `months_diff`-Funktion mit verschiedenen Datenszenarien funktioniert, erstellen wir eine separate Testdatei. Dieser Ansatz ist in der Softwareentwicklung üblich, um zu überprüfen, ob unser Code wie erwartet funktioniert.

Erstellen Sie eine neue Datei namens `month_diff_test.py` im Verzeichnis `/home/labex/project`:

```python
from datetime import date
from month_difference import months_diff

# Test scenario 1: Dates in the same month
date1 = date(2023, 5, 5)
date2 = date(2023, 5, 25)
print(f"Same month: {months_diff(date1, date2)} month(s)")

# Test scenario 2: Consecutive months
date3 = date(2023, 6, 28)
date4 = date(2023, 7, 15)
print(f"Consecutive months: {months_diff(date3, date4)} month(s)")

# Test scenario 3: Dates crossing year boundary
date5 = date(2023, 12, 20)
date6 = date(2024, 1, 10)
print(f"Across years: {months_diff(date5, date6)} month(s)")

# Test scenario 4: Several months apart
date7 = date(2023, 3, 10)
date8 = date(2023, 9, 20)
print(f"Several months: {months_diff(date7, date8)} month(s)")

# Test scenario 5: Dates in reverse order (negative result)
print(f"Reverse order: {months_diff(date8, date7)} month(s)")

# Test scenario 6: Exact multiples of 30 days
date9 = date(2023, 1, 1)
date10 = date(2023, 1, 31)  # 30 days
date11 = date(2023, 3, 2)   # 60 days
print(f"30 days exactly: {months_diff(date9, date10)} month(s)")
print(f"60 days exactly: {months_diff(date9, date11)} month(s)")
```

Speichern Sie diese Datei und führen Sie sie aus:

```bash
python3 ~/project/month_diff_test.py
```

Sie sollten eine Ausgabe ähnlich der folgenden sehen:

```
Same month: 1 month(s)
Consecutive months: 1 month(s)
Across years: 1 month(s)
Several months: 7 month(s)
Reverse order: -7 month(s)
30 days exactly: 1 month(s)
60 days exactly: 2 month(s)
```

Lassen Sie uns diese Ergebnisse analysieren:

1. **Gleicher Monat**: Selbst innerhalb desselben Monats gibt unsere Funktion 1 Monat zurück. Dies liegt daran, dass auch ein Teilmonat als ganzer Monat gezählt wird.

2. **Aufeinanderfolgende Monate**: Für Daten in aufeinanderfolgenden Monaten gibt die Funktion 1 Monat zurück.

3. **Über Jahresgrenzen hinweg**: Für Daten, die die Jahresgrenze überschreiten, berechnet die Funktion weiterhin korrekt.

4. **Mehrere Monate**: Für Daten, die mehrere Monate auseinanderliegen, berechnet die Funktion die entsprechende Anzahl von Monaten.

5. **Umgekehrte Reihenfolge**: Wenn das Enddatum vor dem Startdatum liegt, erhalten wir ein negatives Ergebnis, was für Szenarien wie die Berechnung der verbleibenden Zeit sinnvoll ist.

6. **Genau Vielfache**: Für genau 30 Tage erhalten wir 1 Monat. Für 60 Tage erhalten wir 2 Monate. Dies bestätigt, dass unsere Funktion wie erwartet mit genauen Vielfachen unserer Monatsdefinition funktioniert.

Unsere `months_diff`-Funktion behandelt alle diese Testfälle korrekt, wenn wir einen Monat als 30 Tage definieren.
