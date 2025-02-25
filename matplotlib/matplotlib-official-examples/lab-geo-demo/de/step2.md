# Erstellen eines Diagramms und von Teildiagrammen

In diesem Schritt werden wir ein Diagramm und vier Teildiagramme für jede der Projektionen erstellen, die wir erstellen werden. Wir werden die `plt.subplots()`-Methode verwenden, um ein Diagramm und Teildiagramme zu erstellen.

```python
fig, axs = plt.subplots(nrows=2, ncols=2, subplot_kw={'projection': 'aitoff'})
```
