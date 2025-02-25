# Tracez les données

Dans cette étape, nous allons utiliser la fonction `plot` de Matplotlib pour tracer les trois jeux de données dans un seul appel. Nous utiliserons des tirets rouges pour le premier jeu de données, des carrés bleus pour le second jeu de données et des triangles verts pour le troisième jeu de données.

```python
plt.plot(t, t, 'r--', label='linear')
plt.plot(t, t**2, 'bs', label='quadratic')
plt.plot(t, t**3, 'g^', label='cubic')
plt.legend()
plt.show()
```
