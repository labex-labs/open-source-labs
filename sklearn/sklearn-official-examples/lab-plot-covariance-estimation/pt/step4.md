# Plotar Resultados

Plotamos a probabilidade de dados não vistos para diferentes valores do parâmetro de encolhimento e mostramos as escolhas feitas pela validação cruzada, as estimativas LedoitWolf e OAS.

```python
import matplotlib.pyplot as plt

fig = plt.figure()
plt.title("Covariância regularizada: probabilidade e coeficiente de encolhimento")
plt.xlabel("Parâmetro de regularização: coeficiente de encolhimento")
plt.ylabel("Erro: probabilidade logarítmica negativa nos dados de teste")

plt.loglog(shrinkages, negative_logliks, label="Probabilidade logarítmica negativa")

plt.plot(plt.xlim(), 2 * [loglik_real], "--r", label="Probabilidade da covariância real")

lik_max = np.amax(negative_logliks)
lik_min = np.amin(negative_logliks)
ymin = lik_min - 6.0 * np.log((plt.ylim()[1] - plt.ylim()[0]))
ymax = lik_max + 10.0 * np.log(lik_max - lik_min)
xmin = shrinkages[0]
xmax = shrinkages[-1]

plt.vlines(
    lw.shrinkage_,
    ymin,
    -loglik_lw,
    color="magenta",
    linewidth=3,
    label="Estimativa Ledoit-Wolf",
)

plt.vlines(
    oa.shrinkage_, ymin, -loglik_oa, color="purple", linewidth=3, label="Estimativa OAS"
)

plt.vlines(
    cv.best_estimator_.shrinkage,
    ymin,
    -cv.best_estimator_.score(X_test),
    color="cyan",
    linewidth=3,
    label="Melhor estimativa da validação cruzada",
)

plt.ylim(ymin, ymax)
plt.xlim(xmin, xmax)
plt.legend()

plt.show()
```
