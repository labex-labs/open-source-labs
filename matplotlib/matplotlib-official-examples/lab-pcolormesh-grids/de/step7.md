# Gouraud-Shading

`Gouraud-Shading` kann ebenfalls angegeben werden, wobei die Farbe in den Vierecken zwischen den Gitterpunkten linear interpoliert wird. Die Formen von `X`, `Y`, `Z` müssen gleich sein. Wir können das Gitter mit dem folgenden Codeblock visualisieren:

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='gouraud', cmap='viridis')
ax.set_title('Gouraud Shading')
plt.show()
```
