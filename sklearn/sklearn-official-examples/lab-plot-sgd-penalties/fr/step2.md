# Génération de données

Nous allons générer quelques données d'échantillonnage pour appliquer nos pénalités dessus. Pour cet exemple, nous allons générer deux classes de données avec 100 échantillons chacune.

```python
np.random.seed(42)

# Générer deux classes de données
X = np.random.randn(200, 2)
y = np.repeat([1, -1], 100)
```
