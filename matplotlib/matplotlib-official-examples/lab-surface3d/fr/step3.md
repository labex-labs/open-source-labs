# Création des données

```python
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```

Nous créons les données pour le tracé. Nous créons les valeurs de `X` et `Y` sous forme de tableaux avec des valeurs régulièrement espacées de -5 à 5 avec un pas de 0,25. Nous créons ensuite une grille de maillage des valeurs de `X` et `Y` à l'aide de `np.meshgrid()`. Nous utilisons la grille de maillage pour calculer les valeurs de `R`, qui est la distance à l'origine. Nous calculons ensuite les valeurs de `Z` en utilisant la fonction `sin()` de `R`.
