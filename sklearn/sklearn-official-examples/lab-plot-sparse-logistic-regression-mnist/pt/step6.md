# Visualizar o Modelo

Visualizaremos o modelo plotando os vetores de classificação para cada classe.

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
plt.suptitle("Vetor de classificação para...")

run_time = time.time() - t0
print("Exemplo de execução em %.3f s" % run_time)
plt.show()
```
