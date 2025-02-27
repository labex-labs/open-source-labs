# Visualizar los resultados del PCA

Podemos visualizar los resultados de nuestro PCA mediante la representación de los componentes principales. Creamos un diagrama de dispersión tridimensional de nuestros datos y coloreamos cada punto según su densidad. Luego representamos los primeros dos componentes principales como un plano. Repetimos este proceso para dos vistas diferentes de los datos.

```python
fig = plt.figure(figsize=(10, 5))

# Primera vista
ax = fig.add_subplot(121, projection="3d", elev=-40, azim=-80)
ax.set_title("Vista 1")

# Representar los datos
density = np.exp(-(x ** 2 + y ** 2))
ax.scatter(x, y, z, c=density, cmap="plasma", marker="+", alpha=0.4)

# Representar los componentes principales
v1 = components[:, 0]
v2 = components[:, 1]
x_pca_plane = np.array([v1[0], -v1[0], -v1[0], v1[0]])
y_pca_plane = np.array([v1[1], -v1[1], -v1[1], v1[1]])
z_pca_plane = np.array([v1[2], -v1[2], v1[2], v1[2]])
ax.plot_surface(x_pca_plane, y_pca_plane, z_pca_plane, alpha=0.2)

# Segunda vista
ax = fig.add_subplot(122, projection="3d", elev=30, azim=20)
ax.set_title("Vista 2")

# Representar los datos
density = np.exp(-(x ** 2 + y ** 2))
ax.scatter(x, y, z, c=density, cmap="plasma", marker="+", alpha=0.4)

# Representar los componentes principales
v1 = components[:, 0]
v2 = components[:, 1]
x_pca_plane = np.array([v1[0], -v1[0], -v1[0], v1[0]])
y_pca_plane = np.array([v1[1], -v1[1], -v1[1], v1[1]])
z_pca_plane = np.array([v1[2], -v1[2], v1[2], v1[2]])
ax.plot_surface(x_pca_plane, y_pca_plane, z_pca_plane, alpha=0.2)

plt.show()
```
