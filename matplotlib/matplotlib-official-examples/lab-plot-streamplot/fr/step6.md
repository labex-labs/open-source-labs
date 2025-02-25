# Contrôle des points de départ

Dans cette étape, nous allons créer un graphique de champ de flux avec des points de départ contrôlés. Le paramètre `start_points` prend un tableau 2D qui représente les points de départ des lignes de courant.

```python
seed_points = np.array([[-2, -1, 0, 1, 2, -1], [-2, -1, 0, 1, 2, 2]])

strm = plt.streamplot(X, Y, U, V, color=U, linewidth=2,
                      cmap='autumn', start_points=seed_points.T)
plt.colorbar(strm.lines)
plt.title('Controlling Starting Points')
plt.plot(seed_points[0], seed_points[1], 'bo')
plt.xlim(-w, w)
plt.ylim(-w, w)
plt.show()
```
