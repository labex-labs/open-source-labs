# Tracez les résultats

Nous allons tracer les résultats pour visualiser la façon dont les modèles s'ajustent aux données.

```python
plt.figure()
plt.scatter(X, y, s=20, edgecolor="black", c="darkorange", label="données")
plt.plot(X_test, y_1, color="cornflowerblue", label="profondeur maximale = 2", linewidth=2)
plt.plot(X_test, y_2, color="yellowgreen", label="profondeur maximale = 5", linewidth=2)
plt.xlabel("données")
plt.ylabel("cible")
plt.title("Régression par arbre de décision")
plt.legend()
plt.show()
```
