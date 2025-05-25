# Visualizar Resultados da PCA

Podemos visualizar os resultados da nossa PCA plotando os componentes principais. Criamos um gráfico de dispersão 3D dos nossos dados e colorimos cada ponto com base na sua densidade. Em seguida, plotamos os dois primeiros componentes principais como um plano. Repetimos este processo para duas vistas diferentes dos dados.

```python
fig = plt.figure(figsize=(10, 5))

# Primeira vista
ax = fig.add_subplot(121, projection="3d", elev=-40, azim=-80)
ax.set_title("Vista 1")

# Plotar os dados
density = np.exp(-(x ** 2 + y ** 2))
ax.scatter(x, y, z, c=density, cmap="plasma", marker="+", alpha=0.4)

# Plotar os componentes principais
v1 = components[:, 0]
v2 = components[:, 1]
x_pca_plane = np.array([v1[0], -v1[0], -v1[0], v1[0]])
y_pca_plane = np.array([v1[1], -v1[1], -v1[1], v1[1]])
z_pca_plane = np.array([v1[2], -v1[2], v1[2], v1[2]])
ax.plot_surface(x_pca_plane, y_pca_plane, z_pca_plane, alpha=0.2)

# Segunda vista
ax = fig.add_subplot(122, projection="3d", elev=30, azim=20)
ax.set_title("Vista 2")

# Plotar os dados
density = np.exp(-(x ** 2 + y ** 2))
ax.scatter(x, y, z, c=density, cmap="plasma", marker="+", alpha=0.4)

# Plotar os componentes principais
v1 = components[:, 0]
v2 = components[:, 1]
x_pca_plane = np.array([v1[0], -v1[0], -v1[0], v1[0]])
y_pca_plane = np.array([v1[1], -v1[1], -v1[1], v1[1]])
z_pca_plane = np.array([v1[2], -v1[2], v1[2], v1[2]])
ax.plot_surface(x_pca_plane, y_pca_plane, z_pca_plane, alpha=0.2)

plt.show()
```
