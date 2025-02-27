# Визуализируем результаты анализа главных компонент (PCA)

Мы можем визуализировать результаты нашего анализа главных компонент, построив главные компоненты. Создадим трехмерный точечный график наших данных и покрасим каждую точку в зависимости от ее плотности. Затем построим первые две главные компоненты в виде плоскости. Повторим этот процесс для двух различных представлений данных.

```python
fig = plt.figure(figsize=(10, 5))

# Первое представление
ax = fig.add_subplot(121, projection="3d", elev=-40, azim=-80)
ax.set_title("Представление 1")

# Строим данные
density = np.exp(-(x ** 2 + y ** 2))
ax.scatter(x, y, z, c=density, cmap="plasma", marker="+", alpha=0.4)

# Строим главные компоненты
v1 = components[:, 0]
v2 = components[:, 1]
x_pca_plane = np.array([v1[0], -v1[0], -v1[0], v1[0]])
y_pca_plane = np.array([v1[1], -v1[1], -v1[1], v1[1]])
z_pca_plane = np.array([v1[2], -v1[2], v1[2], v1[2]])
ax.plot_surface(x_pca_plane, y_pca_plane, z_pca_plane, alpha=0.2)

# Второе представление
ax = fig.add_subplot(122, projection="3d", elev=30, azim=20)
ax.set_title("Представление 2")

# Строим данные
density = np.exp(-(x ** 2 + y ** 2))
ax.scatter(x, y, z, c=density, cmap="plasma", marker="+", alpha=0.4)

# Строим главные компоненты
v1 = components[:, 0]
v2 = components[:, 1]
x_pca_plane = np.array([v1[0], -v1[0], -v1[0], v1[0]])
y_pca_plane = np.array([v1[1], -v1[1], -v1[1], v1[1]])
z_pca_plane = np.array([v1[2], -v1[2], v1[2], v1[2]])
ax.plot_surface(x_pca_plane, y_pca_plane, z_pca_plane, alpha=0.2)

plt.show()
```
