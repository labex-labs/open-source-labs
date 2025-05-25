# Plotar a Triangulação de Delaunay

Vamos plotar a triangulação usando a função `triplot`.

```python
fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
ax1.triplot(triang, 'bo-', lw=1)
ax1.set_title('Triplot da Triangulação de Delaunay')
```
