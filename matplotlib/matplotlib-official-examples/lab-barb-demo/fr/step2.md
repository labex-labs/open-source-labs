# Création des données

Ensuite, nous allons créer les données qui seront utilisées pour générer le graphique de flèches de vent. Nous allons créer une grille uniforme de 5x5 et un champ vectoriel à l'aide des fonctions meshgrid et multiplication.

```python
x = np.linspace(-5, 5, 5)
X, Y = np.meshgrid(x, x)
U, V = 12 * X, 12 * Y
```
