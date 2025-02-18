# Y-Positionierung über rcParams

Setzen Sie die Parameter `titley` und `titlepad` von `rcParams`, um die vertikale Position des Titels anzupassen.

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.xaxis.set_label_position('top')
ax.set_xlabel('X-label')
plt.rcParams['axes.titley'] = 1.0
plt.rcParams['axes.titlepad'] = -14
ax.set_title('RCParam Y Positioning')
```
