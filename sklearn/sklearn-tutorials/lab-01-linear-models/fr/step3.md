# Lasso

Le Lasso est une méthode de régression linéaire qui ajoute un terme de pénalité à la fonction objectif des moindres carrés ordinaires. Le terme de pénalité a pour effet de fixer certains coefficients à exactement zéro, effectuant ainsi une sélection de caractéristiques. Le Lasso peut être utilisé pour l'estimation de modèles creux.

Ajustons un modèle Lasso.

```python
reg = linear_model.Lasso(alpha=0.1)
reg.fit([[0, 0], [1, 1]], [0, 1])

print(reg.coef_)
```

- Nous créons une instance de `Lasso` avec le paramètre de régularisation `alpha` défini sur 0,1.
- Nous utilisons la méthode `fit` pour ajuster le modèle aux données d'entraînement.
- Nous affichons les coefficients du modèle Lasso.
