# Visualize PCA Results

We can visualize the results of our PCA by plotting the principal components. We create a 3D scatter plot of our data and color each point based on its density. We then plot the first two principal components as a plane. We repeat this process for two different views of the data.

```python
fig = plt.figure(figsize=(10, 5))

# First view
ax = fig.add_subplot(121, projection="3d", elev=-40, azim=-80)
ax.set_title("View 1")

# Plot the data
density = np.exp(-(x ** 2 + y ** 2))
ax.scatter(x, y, z, c=density, cmap="plasma", marker="+", alpha=0.4)

# Plot the principal components
v1 = components[:, 0]
v2 = components[:, 1]
x_pca_plane = np.array([v1[0], -v1[0], -v1[0], v1[0]])
y_pca_plane = np.array([v1[1], -v1[1], -v1[1], v1[1]])
z_pca_plane = np.array([v1[2], -v1[2], v1[2], v1[2]])
ax.plot_surface(x_pca_plane, y_pca_plane, z_pca_plane, alpha=0.2)

# Second view
ax = fig.add_subplot(122, projection="3d", elev=30, azim=20)
ax.set_title("View 2")

# Plot the data
density = np.exp(-(x ** 2 + y ** 2))
ax.scatter(x, y, z, c=density, cmap="plasma", marker="+", alpha=0.4)

# Plot the principal components
v1 = components[:, 0]
v2 = components[:, 1]
x_pca_plane = np.array([v1[0], -v1[0], -v1[0], v1[0]])
y_pca_plane = np.array([v1[1], -v1[1], -v1[1], v1[1]])
z_pca_plane = np.array([v1[2], -v1[2], v1[2], v1[2]])
ax.plot_surface(x_pca_plane, y_pca_plane, z_pca_plane, alpha=0.2)

plt.show()
```
