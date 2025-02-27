# Générez quelques données d'échantillonnage

Ensuite, nous allons générer quelques données d'échantillonnage pour effectuer une estimation de la densité. Dans le cadre de ce laboratoire, générons un ensemble de données en une dimension avec 100 points. Nous utiliserons une distribution normale pour générer les données.

```python
np.random.seed(0)
X = np.random.normal(0, 1, 100).reshape(-1, 1)
```
