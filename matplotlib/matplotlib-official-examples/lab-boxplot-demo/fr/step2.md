# Générez les données

Ensuite, nous allons générer quelques données d'échantillonnage pour les utiliser dans nos diagrammes en boîte. Pour ce tutoriel, nous utiliserons les données suivantes :

```python
spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low))
```
