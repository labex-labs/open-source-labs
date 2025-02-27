# Visualiser le modèle

Nous allons visualiser le modèle en traçant les vecteurs de classification pour chaque classe.

```python
coef = clf.coef_.copy()
plt.figure(figsize=(10, 5))
scale = np.abs(coef).max()
for i in range(10):
    l1_plot = plt.subplot(2, 5, i + 1)
    l1_plot.imshow(
        coef[i].reshape(28, 28),
        interpolation="nearest",
        cmap=plt.cm.RdBu,
        vmin=-scale,
        vmax=scale,
    )
    l1_plot.set_xticks(())
    l1_plot.set_yticks(())
    l1_plot.set_xlabel("Classe %i" % i)
plt.suptitle("Vecteur de classification pour...")

run_time = time.time() - t0
print("Exécution de l'exemple en %.3f s" % run_time)
plt.show()
```
