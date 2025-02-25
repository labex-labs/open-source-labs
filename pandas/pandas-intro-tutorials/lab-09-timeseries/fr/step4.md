# Calculez la concentration moyenne en NO2 pour chaque jour de la semaine

Nous pouvons maintenant calculer la concentration moyenne en NO2 pour chaque jour de la semaine à chaque emplacement de mesure. Cela peut être fait à l'aide de la méthode `groupby`.

```python
# calculate the average NO2 concentration for each day of the week
average_NO2 = air_quality.groupby([air_quality["datetime"].dt.weekday, "location"])["value"].mean()
```
