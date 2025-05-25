# Predizer Distribuição de Espécies

Neste passo, preveremos a distribuição da espécie usando o modelo OneClassSVM. Predizeremos a distribuição da espécie usando os dados de treino e plotaremos os resultados.

```python
# Predizer a distribuição da espécie usando os dados de treino
Z = np.ones((data.Ny, data.Nx), dtype=np.float64)

# Iremos prever apenas para os pontos terrestres.
idx = np.where(data.coverages[6] > -9999)
coverages_land = data.coverages[:, idx[0], idx[1]].T

pred = clf.decision_function((coverages_land - mean) / std)
Z *= pred.min()
Z[idx[0], idx[1]] = pred

levels = np.linspace(Z.min(), Z.max(), 25)
Z[data.coverages[6] == -9999] = -9999

# plotar contornos da previsão
plt.contourf(X, Y, Z, levels=levels, cmap=plt.cm.Reds)
plt.colorbar(format="%.2f")

# dispersão de pontos de treino/teste
plt.scatter(
    BV_bunch.pts_train["dd long"],
    BV_bunch.pts_train["dd lat"],
    s=2**2,
    c="black",
    marker="^",
    label="treino",
)
plt.scatter(
    BV_bunch.pts_test["dd long"],
    BV_bunch.pts_test["dd lat"],
    s=2**2,
    c="black",
    marker="x",
    label="teste",
)
plt.legend()
plt.title(BV_bunch.name)
plt.axis("equal")
```
