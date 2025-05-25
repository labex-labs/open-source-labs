# Definir as datas e o delta

Em seguida, definiremos as datas e os valores delta usando a biblioteca datetime. O intervalo de datas será de 2 de março de 2000 a 6 de março de 2000, com um intervalo de 6 horas. Copie e cole o seguinte código:

```python
date1 = datetime.datetime(2000, 3, 2)
date2 = datetime.datetime(2000, 3, 6)
delta = datetime.timedelta(hours=6)
dates = drange(date1, date2, delta)
```
