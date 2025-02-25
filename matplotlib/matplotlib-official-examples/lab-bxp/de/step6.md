# Anzeige verschiedener Elemente anpassen

Wir können die Anzeige verschiedener Elemente des Boxplot-Diagramms mithilfe verschiedener Parameter in der `bxp()`-Funktion anpassen. In diesem Beispiel zeigen wir, wie die Box, der Median, die Ausreißer, der Mittelpunkt und die Mittellinie angepasst werden können.

```python
# Customize the display of different elements
boxprops = dict(linestyle='--', linewidth=3, color='darkgoldenrod')
flierprops = dict(marker='o', markerfacecolor='green', markersize=12, linestyle='none')
medianprops = dict(linestyle='-.', linewidth=2.5, color='firebrick')
meanpointprops = dict(marker='D', markeredgecolor='black', markerfacecolor='firebrick')
meanlineprops = dict(linestyle='--', linewidth=2.5, color='purple')

plt.bxp(stats, boxprops=boxprops, flierprops=flierprops, medianprops=medianprops, meanprops=meanpointprops, meanline=True, showmeans=True)
plt.show()
```
