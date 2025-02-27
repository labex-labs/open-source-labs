# Visualiser les résultats de la PCA

Nous pouvons visualiser les résultats de notre PCA en traçant les composantes principales. Nous créons un nuage de points 3D de nos données et colorons chaque point en fonction de sa densité. Nous traçons ensuite les deux premières composantes principales sous forme de plan. Nous répétons ce processus pour deux vues différentes des données.

```python
fig = plt.figure(figsize=(10, 5))

# Première vue
ax = fig.add_subplot(121, projection="3d", elev=-40, azim=-80)
ax.set_title("Vue 1")

# Tracer les données
density = np.exp(-(x ** 2 + y ** 2))
ax.scatter(x, y, z, c=density, cmap="plasma", marker="+", alpha=0.4)

# Tracer les composantes principales
v1 = components[:, 0]
v2 = components[:, 1]
x_pca_plane = np.array([v1[0], -v1[0], -v1[0], v1[0]])
y_pca_plane = np.array([v1[1], -v1[1], -v1[1], v1[1]])
z_pca_plane = np.array([v1[2], -v1[2], v1[2], v1[2]])
ax.plot_surface(x_pca_plane, y_pca_plane, z_pca_plane, alpha=0.2)

# Deuxième vue
ax = fig.add_subplot(122, projection="3d", elev=30, azim=20)
ax.set_title("Vue 2")

# Tracer les données
density = np.exp(-(x ** 2 + y ** 2))
ax.scatter(x, y, z, c=density, cmap="plasma", marker="+", alpha=0.4)

# Tracer les composantes principales
v1 = components[:, 0]
v2 = components[:, 1]
x_pca_plane = np.array([v1[0], -v1[0], -v1[0], v1[0]])
y_pca_plane = np.array([v1[1], -v1[1], -v1[1], v1[1]])
z_pca_plane = np.array([v1[2], -v1[2], v1[2], v1[2]])
ax.plot_surface(x_pca_plane, y_pca_plane, z_pca_plane, alpha=0.2)

plt.show()
```
