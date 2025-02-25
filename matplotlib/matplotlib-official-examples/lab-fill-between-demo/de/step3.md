# Selektives Füllen horizontaler Bereiche

Der Parameter _where_ ermöglicht es, die x-Bereiche anzugeben, die gefüllt werden sollen. Es ist ein boolescher Array der gleichen Größe wie _x_. Nur die x-Bereiche von aufeinanderfolgenden _True_-Sequenzen werden gefüllt. Folglich wird der Bereich zwischen benachbarten _True_- und _False_-Werten niemals gefüllt. Es wird daher empfohlen, `interpolate=True` festzulegen, es sei denn, die x-Abstände der Datenpunkte sind genug fein, sodass der obige Effekt nicht auffällt.

```python
x = np.array([0, 1, 2, 3])
y1 = np.array([0.8, 0.8, 0.2, 0.2])
y2 = np.array([0, 0, 1, 1])

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

ax1.set_title('interpolation=False')
ax1.plot(x, y1, 'o--')
ax1.plot(x, y2, 'o--')
ax1.fill_between(x, y1, y2, where=(y1 > y2), color='C0', alpha=0.3)
ax1.fill_between(x, y1, y2, where=(y1 < y2), color='C1', alpha=0.3)

ax2.set_title('interpolation=True')
ax2.plot(x, y1, 'o--')
ax2.plot(x, y2, 'o--')
ax2.fill_between(x, y1, y2, where=(y1 > y2), color='C0', alpha=0.3,
                 interpolate=True)
ax2.fill_between(x, y1, y2, where=(y1 <= y2), color='C1', alpha=0.3,
                 interpolate=True)
fig.tight_layout()
```
