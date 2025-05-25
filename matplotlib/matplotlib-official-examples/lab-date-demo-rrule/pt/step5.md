# Definir as datas e gerar dados aleatórios

Você precisa definir as datas de início e fim e o delta, que representa a diferença entre cada data. Você também precisa gerar dados aleatórios para o exemplo.

```python
date1 = datetime.date(1952, 1, 1)
date2 = datetime.date(2004, 4, 12)
delta = datetime.timedelta(days=100)

dates = drange(date1, date2, delta)
s = np.random.rand(len(dates))
```
