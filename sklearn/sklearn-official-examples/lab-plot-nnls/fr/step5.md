# Comparer les coefficients de régression

Nous allons maintenant comparer les coefficients de régression entre la régression linéaire non négative et la régression linéaire classique. Nous allons tracer les coefficients l'un contre l'autre et observer qu'ils sont fortement corrélés. Cependant, la contrainte non négative réduit certains coefficients à 0. Cela est dû au fait que la régression linéaire non négative produit intrinsèquement des résultats parcimonieux.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(reg_ols.coef_, reg_nnls.coef_, linewidth=0, marker=".")

low_x, high_x = ax.get_xlim()
low_y, high_y = ax.get_ylim()
low = max(low_x, low_y)
high = min(high_x, high_y)
ax.plot([low, high], [low, high], ls="--", c=".3", alpha=0.5)
ax.set_xlabel("OLS regression coefficients", fontweight="bold")
ax.set_ylabel("NNLS regression coefficients", fontweight="bold")
```
