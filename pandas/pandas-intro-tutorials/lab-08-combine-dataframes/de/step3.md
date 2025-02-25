# Zusammenführen der Datensätze

Als nächstes werden wir die Messungen von Nitrat und Feinstaub mithilfe der `concat`-Funktion in eine einzelne Tabelle zusammenführen.

```python
# Concatenate the two dataframes
air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
```
