# Berechnen der durchschnittlichen NO2-Konzentration für jeden Wochentag

Wir können jetzt die durchschnittliche NO2-Konzentration für jeden Wochentag an jedem Messort berechnen. Dies kann mit der `groupby`-Methode durchgeführt werden.

```python
# calculate the average NO2 concentration for each day of the week
average_NO2 = air_quality.groupby([air_quality["datetime"].dt.weekday, "location"])["value"].mean()
```
