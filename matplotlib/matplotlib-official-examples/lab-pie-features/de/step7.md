# Die Sektoren auseinanderdrücken

Wir können einen oder mehrere Sektoren des Kreisdiagramms auseinanderdrücken, indem wir eine Liste von Werten an den `explode`-Parameter der `pie()`-Funktion übergeben.

```python
explode = (0, 0.1, 0, 0)  # nur den 2. Sektor auseinanderdrücken (d.h. 'Hogs')

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow=True, startangle=90)
```
