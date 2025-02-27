# Ergebnisse der Hauptkomponentenanalyse (PCA) visualisieren

Wir können die Ergebnisse unserer PCA visualisieren, indem wir die Hauptkomponenten darstellen. Wir erstellen einen 3D-Streuplot unserer Daten und färben jeden Punkt basierend auf seiner Dichte. Anschließend zeichnen wir die ersten beiden Hauptkomponenten als Ebene. Wir wiederholen diesen Prozess für zwei verschiedene Ansichten der Daten.

```python
fig = plt.figure(figsize=(10, 5))

# Erste Ansicht
ax = fig.add_subplot(121, projection="3d", elev=-40, azim=-80)
ax.set_title("Ansicht 1")

# Zeichnen der Daten
density = np.exp(-(x ** 2 + y ** 2))
ax.scatter(x, y, z, c=density, cmap="plasma", marker="+", alpha=0.4)

# Zeichnen der Hauptkomponenten
v1 = components[:, 0]
v2 = components[:, 1]
x_pca_plane = np.array([v1[0], -v1[0], -v1[0], v1[0]])
y_pca_plane = np.array([v1[1], -v1[1], -v1[1], v1[1]])
z_pca_plane = np.array([v1[2], -v1[2], v1[2], v1[2]])
ax.plot_surface(x_pca_plane, y_pca_plane, z_pca_plane, alpha=0.2)

# Zweite Ansicht
ax = fig.add_subplot(122, projection="3d", elev=30, azim=20)
ax.set_title("Ansicht 2")

# Zeichnen der Daten
density = np.exp(-(x ** 2 + y ** 2))
ax.scatter(x, y, z, c=density, cmap="plasma", marker="+", alpha=0.4)

# Zeichnen der Hauptkomponenten
v1 = components[:, 0]
v2 = components[:, 1]
x_pca_plane = np.array([v1[0], -v1[0], -v1[0], v1[0]])
y_pca_plane = np.array([v1[1], -v1[1], -v1[1], v1[1]])
z_pca_plane = np.array([v1[2], -v1[2], v1[2], v1[2]])
ax.plot_surface(x_pca_plane, y_pca_plane, z_pca_plane, alpha=0.2)

plt.show()
```
