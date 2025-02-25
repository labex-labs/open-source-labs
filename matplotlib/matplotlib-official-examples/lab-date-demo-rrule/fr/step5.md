# Fixez les dates et générez des données aléatoires

Vous devez fixer les dates de début et de fin et le delta, qui représente la différence entre chaque date. Vous devez également générer des données aléatoires pour l'exemple.

```python
date1 = datetime.date(1952, 1, 1)
date2 = datetime.date(2004, 4, 12)
delta = datetime.timedelta(days=100)

dates = drange(date1, date2, delta)
s = np.random.rand(len(dates))
```
