# Criar Gráfico 3D

Criamos um gráfico 3D usando `matplotlib`. Adicionamos uma linha vazia para cada passeio aleatório ao gráfico. Definimos os limites para os eixos x, y e z para que fiquem entre 0 e 1.

```python
# Attaching 3D axis to the figure
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# Create lines initially without data
lines = [ax.plot([], [], [])[0] for _ in walks]

# Setting the axes properties
ax.set(xlim3d=(0, 1), xlabel='X')
ax.set(ylim3d=(0, 1), ylabel='Y')
ax.set(zlim3d=(0, 1), zlabel='Z')
```
