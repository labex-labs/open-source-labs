# Plotar Posteriores

Plotaremos os posteriors do modelo GPC usando hiperparâmetros fixos e otimizados. Plotaremos os dados de treino, os dados de teste e a probabilidade prevista da classe 1. Também rotularemos os gráficos.

```python
# Plotar posteriors
plt.figure()
plt.scatter(X[:train_size, 0], y[:train_size], c="k", label="Dados de treino", edgecolors=(0, 0, 0))
plt.scatter(X[train_size:, 0], y[train_size:], c="g", label="Dados de teste", edgecolors=(0, 0, 0))
X_ = np.linspace(0, 5, 100)
plt.plot(X_, gp_fix.predict_proba(X_[:, np.newaxis])[:, 1], "r", label="Kernel inicial: %s" % gp_fix.kernel_)
plt.plot(X_, gp_opt.predict_proba(X_[:, np.newaxis])[:, 1], "b", label="Kernel otimizado: %s" % gp_opt.kernel_)
plt.xlabel("Característica")
plt.ylabel("Probabilidade da classe 1")
plt.xlim(0, 5)
plt.ylim(-0.25, 1.5)
plt.legend(loc="best")
```
