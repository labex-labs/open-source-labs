# Spaltenbezeichnungen in Kleinbuchstaben umwandeln

Schließlich werden wir die Spaltenbezeichnungen mit einer Funktion in Kleinbuchstaben umwandeln.

```python
# Convert column labels to lowercase
air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
```
