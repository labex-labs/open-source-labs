# Régression Ridge

La régression Ridge est une méthode de régression linéaire qui ajoute un terme de pénalité à la fonction objectif des moindres carrés ordinaires. Ce terme de pénalité aide à réduire le surapprentissage en réduisant les coefficients vers zéro. La complexité du modèle peut être contrôlée par le paramètre de régularisation.

Ajustons un modèle de régression Ridge.

```python
reg = linear_model.Ridge(alpha=0.5)
reg.fit([[0, 0], [0, 0], [1, 1]], [0, 0.1, 1])

print(reg.coef_)
```

- Nous créons une instance de `Ridge` avec le paramètre de régularisation `alpha` défini sur 0,5.
- Nous utilisons la méthode `fit` pour ajuster le modèle aux données d'entraînement.
- Nous affichons les coefficients du modèle de régression Ridge.
