# Criar o Gráfico (Plot)

Precisamos criar o gráfico e adicionar o polígono a ele.

```python
fig, ax = plt.subplots()
ax.add_patch(poly)
p = PolygonInteractor(ax, poly)

ax.set_title('Clique e arraste um ponto para movê-lo')
ax.set_xlim((-2, 2))
ax.set_ylim((-2, 2))
plt.show()
```
