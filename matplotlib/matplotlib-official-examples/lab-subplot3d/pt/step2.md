# Criar a Figura e os Subplots

Criaremos uma figura com dois subplots. O primeiro subplot será um gráfico de superfície 3D, e o segundo subplot será um gráfico wireframe 3D.

```python
# Criar uma figura com dois subplots
fig = plt.figure(figsize=plt.figaspect(0.5))

# Adicionar o primeiro subplot com projeção 3D
ax1 = fig.add_subplot(1, 2, 1, projection='3d')

# Adicionar o segundo subplot com projeção 3D
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
```
