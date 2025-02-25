# Ajouter l'étiquette de l'intégrale

Ajoutez l'étiquette de l'intégrale au graphique à l'aide de `text`. L'étiquette devrait être centrée au point milieu entre a et b et devrait être formatée à l'aide de mathtext.

```python
ax.text(0.5 * (a + b), 30, r"$\int_a^b f(x)\mathrm{d}x$",
        horizontalalignment='center', fontsize=20)
```
