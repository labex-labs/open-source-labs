# Nuage de points

Nous pouvons également créer un nuage de points pour montrer la relation entre deux variables catégorielles. Dans ce cas, nous utiliserons les mêmes données sur les fruits et ajouterons du bruit aléatoire aux comptes pour créer une deuxième variable.

```python
noise = np.random.rand(len(values)) * 5
plt.scatter(names, values + noise)
plt.title('Fruit Counts with Noise')
plt.xlabel('Fruit')
plt.ylabel('Count')
plt.show()
```
