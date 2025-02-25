# Rééchantillonnage de données de séries temporelles

La méthode `resample` est un moyen puissant de changer la fréquence des données de séries temporelles. Ici, nous allons agréger les données de séries temporelles horaires actuelles pour obtenir la valeur maximale mensuelle à chaque station de mesure.

```python
# By pivoting the data, the datetime information became the index of the table.
no_2 = air_quality.pivot(index="datetime", columns="location", values="value")
no_2.head()

# Create a plot of the values in the different stations from the 20th of May till the end of 21st of May
no_2["2019-05-20":"2019-05-21"].plot()

# resample time series data
monthly_max = no_2.resample("M").max()
monthly_max
```
