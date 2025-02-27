# Visualiser les résultats

Dans cette étape, nous allons visualiser les résultats des chemins de régression岭.

```python
ax = plt.gca()

ax.plot(alphas, coefs)
ax.set_xscale("log")
ax.set_xlim(ax.get_xlim()[::-1])  # inverse l'axe
plt.xlabel("alpha")
plt.ylabel("poids")
plt.title("Coefficients de régression岭 en fonction de la régularisation")
plt.axis("tight")
plt.show()
```
