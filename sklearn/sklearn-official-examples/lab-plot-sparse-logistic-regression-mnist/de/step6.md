# Modell visualisieren

Wir werden das Modell visualisieren, indem wir die Klassifikationsvektoren für jede Klasse darstellen.

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
    l1_plot.set_xlabel("Klasse %i" % i)
plt.suptitle("Klassifikationsvektor für...")

laufzeit = time.time() - t0
print("Beispiellauf in %.3f s" % laufzeit)
plt.show()
```
