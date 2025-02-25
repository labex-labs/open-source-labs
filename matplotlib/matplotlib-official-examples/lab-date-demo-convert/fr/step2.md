# Définissez les dates et le delta

Ensuite, nous allons définir les valeurs de dates et de delta à l'aide de la bibliothèque datetime. La plage de dates ira du 2 mars 2000 au 6 mars 2000, avec un intervalle de 6 heures. Copiez et collez le code suivant :

```python
date1 = datetime.datetime(2000, 3, 2)
date2 = datetime.datetime(2000, 3, 6)
delta = datetime.timedelta(hours=6)
dates = drange(date1, date2, delta)
```
