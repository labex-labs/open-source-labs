# Tracer les résultats

Nous allons maintenant tracer la dépendance de la cible par rapport à chaque caractéristique ainsi que les scores du test F et de l'information mutuelle pour chaque caractéristique.

```python
plt.figure(figsize=(15, 5))
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.scatter(X[:, i], y, edgecolor="black", s=20)
    plt.xlabel("$x_{}$".format(i + 1), fontsize=14)
    if i == 0:
        plt.ylabel("$y$", fontsize=14)
    plt.title("F-test={:.2f}, MI={:.2f}".format(f_test[i], mi[i]), fontsize=16)
plt.show()
```
