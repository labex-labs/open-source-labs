# Ajuster le régresseur Ridge

Nous allons maintenant ajuster le régresseur Ridge à l'ensemble de données et comparer ses performances à celles du HuberRegressor.

```python
# Ajuster un régresseur Ridge pour le comparer au régresseur Huber.
ridge = Ridge(alpha=0.0, random_state=0)
ridge.fit(X, y)
coef_ridge = ridge.coef_
coef_ = ridge.coef_ * x + ridge.intercept_
plt.plot(x, coef_, "g-", label="ridge regression")

# Ajouter une légende au tracé
plt.legend(loc=0)

# Afficher le tracé
plt.title("Comparaison de HuberRegressor et Ridge")
plt.xlabel("X")
plt.ylabel("y")
plt.show()
```
