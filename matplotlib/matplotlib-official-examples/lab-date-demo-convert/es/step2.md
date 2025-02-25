# Definir las fechas y el delta

A continuación, definiremos las fechas y los valores de delta utilizando la biblioteca datetime. El rango de fechas será desde el 2 de marzo de 2000 hasta el 6 de marzo de 2000, con un intervalo de 6 horas. Copie y pegue el siguiente código:

```python
date1 = datetime.datetime(2000, 3, 2)
date2 = datetime.datetime(2000, 3, 6)
delta = datetime.timedelta(hours=6)
dates = drange(date1, date2, delta)
```
