# Créez les données

Dans cette étape, nous créons les données que nous utiliserons pour créer notre graphique à barre d'erreur.

```python
x = np.arange(10)
y = 2.5 * np.sin(x / 20 * np.pi)
yerr = np.linspace(0.05, 0.2, 10)
```
