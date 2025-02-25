# Créer des données d'échantillonnage

Ensuite, nous allons créer des données d'échantillonnage pour notre graphique à l'aide de NumPy. Nous allons générer 100 points de données entre 0 et 2π et calculer leurs valeurs sinus correspondantes.

```python
x = np.linspace(0, 2 * np.pi, 100)
y = 2 * np.sin(x)
```
