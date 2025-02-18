# Posicionamiento vertical con rcParams

Establece los parámetros `titley` y `titlepad` de `rcParams` para ajustar la posición vertical del título.

```python
fig, ax = plt.subplots()
ax.plot(range(10))
ax.xaxis.set_label_position('top')
ax.set_xlabel('X-label')
plt.rcParams['axes.titley'] = 1.0
plt.rcParams['axes.titlepad'] = -14
ax.set_title('RCParam Y Positioning')
```
