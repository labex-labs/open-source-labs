# Erstellen des Kreisdiagramms

Jetzt können wir das Kreisdiagramm erstellen. Wir beginnen, indem wir die Figur- und Achsenobjekte definieren:

```python
# make figure and assign axis objects
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
fig.subplots_adjust(wspace=0)
```

Dann legen wir die Parameter für das Kreisdiagramm fest und zeichnen es:

```python
# rotate so that first wedge is split by the x-axis
angle = -180 * overall_ratios[0]
wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle,
                     labels=labels, explode=explode)
```
