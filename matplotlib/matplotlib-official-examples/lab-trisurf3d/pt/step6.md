# Criar a Superfície 3D

Criaremos a superfície 3D usando a função `plot_trisurf`:

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)

plt.show()
```
