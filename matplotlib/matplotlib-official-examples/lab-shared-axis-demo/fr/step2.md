# Créer des données pour les graphiques

Nous devons créer des données pour les graphiques afin de les visualiser. Dans cet exemple, nous allons créer trois ensembles de données différents à l'aide de NumPy.

```python
t = np.arange(0.01, 5.0, 0.01)
s1 = np.sin(2 * np.pi * t)
s2 = np.exp(-t)
s3 = np.sin(4 * np.pi * t)
```
