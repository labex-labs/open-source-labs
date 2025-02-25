# Die Teilplots erstellen

Wir können Teilplots mit der `plt.subplot()`-Methode erstellen. In diesem Beispiel werden wir drei Teilplots erstellen, wobei der erste Teilplot die erste Zeile und alle drei Spalten einnimmt, und der zweite und dritte Teilplot die zweite bzw. dritte Zeile einnehmen und die x-Achse mit dem ersten Teilplot teilen.

```python
ax1 = plt.subplot(311)
ax2 = plt.subplot(312, sharex=ax1)
ax3 = plt.subplot(313, sharex=ax1, sharey=ax1)
```
