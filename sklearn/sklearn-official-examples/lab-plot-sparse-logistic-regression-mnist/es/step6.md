# Visualizar el modelo

Visualizaremos el modelo trazando los vectores de clasificación para cada clase.

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
    l1_plot.set_xlabel("Clase %i" % i)
plt.suptitle("Vector de clasificación para...")

run_time = time.time() - t0
print("Ejemplo ejecutado en %.3f s" % run_time)
plt.show()
```
