# Ajoutez une nouvelle colonne pour le mois de mesure

Maintenant, nous voulons ajouter une nouvelle colonne à notre DataFrame qui contienne uniquement le mois de chaque mesure. Cela peut être réalisé à l'aide de l'accesseur `dt`.

```python
# add a new column for the month of each measurement
air_quality["month"] = air_quality["datetime"].dt.month
```
