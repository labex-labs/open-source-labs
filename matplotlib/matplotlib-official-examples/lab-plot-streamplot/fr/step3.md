# Densité variable

Dans cette étape, nous allons créer un graphique de champ de flux avec une densité variable. Le paramètre `density` contrôle le nombre de lignes de courant à tracer. Des valeurs plus élevées résulteront en plus de lignes de courant.

```python
plt.streamplot(X, Y, U, V, density=[0.5, 1])
plt.title('Varying Density')
plt.show()
```
