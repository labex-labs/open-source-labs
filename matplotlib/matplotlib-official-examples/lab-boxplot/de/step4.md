# Einzelne Komponenten entfernen

Wir können einzelne Komponenten des Boxplots entfernen, indem wir die verschiedenen Schlüsselwortargumente verwenden, die in der `boxplot()`-Funktion zur Verfügung stehen. Beispielsweise können wir die Mittelwerte entfernen, indem wir `showmeans` auf False setzen. Wir können auch die Box und die Schnurrbögen entfernen, indem wir `showbox` und `showcaps` jeweils auf False setzen.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 8), sharey=True)
axs[0, 0].boxplot(data, labels=labels)
axs[0, 0].set_title('Default')

axs[0, 1].boxplot(data, labels=labels, showmeans=False)
axs[0, 1].set_title('No Means')

axs[1, 0].boxplot(data, labels=labels, showbox=False, showcaps=False)
axs[1, 0].set_title('No Box or Whiskers')

axs[1, 1].boxplot(data, labels=labels, showfliers=False)
axs[1, 1].set_title('No Outliers')

plt.show()
```
