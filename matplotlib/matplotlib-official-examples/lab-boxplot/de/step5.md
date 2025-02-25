# Anpassen der Boxplot-Styles

Wir können auch die Styles des Boxplots anpassen, indem wir die verschiedenen Schlüsselwortargumente verwenden, die in der `boxplot()`-Funktion zur Verfügung stehen. Beispielsweise können wir die Farbe und den Linienstil der Box ändern, indem wir `boxprops` setzen. Wir können auch den Stil der Medianen, Mittelwerte und Mittelwerlinien ändern, indem wir `medianprops`, `meanprops` und `meanlineprops` jeweils setzen.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 8), sharey=True)
axs[0, 0].boxplot(data, labels=labels)
axs[0, 0].set_title('Default')

boxprops = dict(linestyle='--', linewidth=2, color='red')
axs[0, 1].boxplot(data, labels=labels, boxprops=boxprops)
axs[0, 1].set_title('Custom Box')

medianprops = dict(linestyle='-', linewidth=2, color='blue')
meanprops = dict(marker='D', markeredgecolor='black', markerfacecolor='green')
meanlineprops = dict(linestyle='--', linewidth=2, color='red')
axs[1, 0].boxplot(data, labels=labels, medianprops=medianprops, meanprops=meanprops, meanline=True, meanlineprops=meanlineprops)
axs[1, 0].set_title('Custom Median, Mean, and Mean Line')

flierprops = dict(marker='o', markerfacecolor='red', markersize=8, markeredgecolor='none')
axs[1, 1].boxplot(data, labels=labels, flierprops=flierprops)
axs[1, 1].set_title('Custom Outliers')

plt.show()
```
