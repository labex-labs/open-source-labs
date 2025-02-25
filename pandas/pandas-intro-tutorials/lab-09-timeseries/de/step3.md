# Fügen einer neuen Spalte für den Monat der Messung hinzu

Jetzt möchten wir unserer DataFrame eine neue Spalte hinzufügen, die nur den Monat jeder Messung enthält. Dies kann mit dem `dt`-Accessor erreicht werden.

```python
# add a new column for the month of each measurement
air_quality["month"] = air_quality["datetime"].dt.month
```
