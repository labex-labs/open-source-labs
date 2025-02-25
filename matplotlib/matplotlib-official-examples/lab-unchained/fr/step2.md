# Génération de données aléatoires

Dans cette étape, nous allons générer des données aléatoires que nous utiliserons pour créer notre graphique.

```python
# Generate random data
data = np.random.uniform(0, 1, (64, 75))
X = np.linspace(-1, 1, data.shape[-1])
G = 1.5 * np.exp(-4 * X ** 2)
```
