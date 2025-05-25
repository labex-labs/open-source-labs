# Gráfico de Dispersão dos Dados Originais e Reduzidos

Neste passo, criaremos um gráfico de dispersão dos dados originais e reduzidos.

```python
fig = plt.figure(figsize=(9, 8))

ax = plt.subplot(221)
ax.scatter(X[:, 0], X[:, 1], c=y, s=50, edgecolor="k")
ax.set_title("Dados Originais (2d)")
ax.set_xticks(())
ax.set_yticks(())

ax = plt.subplot(222)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, s=50, edgecolor="k")
ax.set_title(
    "Redução por SVD truncada (2d) dos dados transformados (%dd)" % X_transformed.shape[1]
)
ax.set_xticks(())
ax.set_yticks(())
```
