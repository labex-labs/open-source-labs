# Créer le graphique en maillage 3D

Nous allons créer un graphique en maillage 3D pour le second sous-graphique. Nous utiliserons la fonction `get_test_data` de mpl_toolkits.mplot3d.axes3d pour créer les données du graphique.

```python
# Create data for the 3D wireframe plot
X, Y, Z = Axes3D.get_test_data(0.05)

# Plot the 3D wireframe plot
ax2.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
```
