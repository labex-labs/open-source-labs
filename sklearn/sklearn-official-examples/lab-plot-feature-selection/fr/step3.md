# Tracer le score univarié des caractéristiques

Nous pouvons tracer les scores univariés de chaque caractéristique pour voir lesquelles sont significatives.

```python
import matplotlib.pyplot as plt

X_indices = np.arange(X.shape[-1])
plt.figure(1)
plt.clf()
plt.bar(X_indices - 0.05, scores, width=0.2)
plt.title("Score univarié des caractéristiques")
plt.xlabel("Numéro de la caractéristique")
plt.ylabel(r"Score univarié ($-Log(p_{valeur})$)")
plt.show()
```
