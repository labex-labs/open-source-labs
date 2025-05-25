# Visualizar Resultados

Finalmente, visualizaremos os resultados usando matplotlib. Plotaremos a posição verdadeira dos pontos de dados, a posição dos pontos de dados usando MDS e a posição dos pontos de dados usando MDS não-métrico. Também plotaremos as distâncias em pares entre os pontos de dados usando LineCollection do matplotlib.

```python
fig = plt.figure(1)
ax = plt.axes([0.0, 0.0, 1.0, 1.0])

s = 100
plt.scatter(X_true[:, 0], X_true[:, 1], color="navy", s=s, lw=0, label="Posição Verdadeira")
plt.scatter(pos[:, 0], pos[:, 1], color="turquoise", s=s, lw=0, label="MDS")
plt.scatter(npos[:, 0], npos[:, 1], color="darkorange", s=s, lw=0, label="NMDS")
plt.legend(scatterpoints=1, loc="best", shadow=False)

similarities = similarities.max() / (similarities + EPSILON) * 100
np.fill_diagonal(similarities, 0)
# Plotar as arestas
start_idx, end_idx = np.where(pos)
# uma sequência de (*linha0*, *linha1*, *linha2*), onde::
#            linen = (x0, y0), (x1, y1), ... (xm, ym)
segments = [
    [X_true[i, :], X_true[j, :]] for i in range(len(pos)) for j in range(len(pos))
]
values = np.abs(similarities)
lc = LineCollection(
    segments, zorder=0, cmap=plt.cm.Blues, norm=plt.Normalize(0, values.max())
)
lc.set_array(similarities.flatten())
lc.set_linewidths(np.full(len(segments), 0.5))
ax.add_collection(lc)

plt.show()
```
