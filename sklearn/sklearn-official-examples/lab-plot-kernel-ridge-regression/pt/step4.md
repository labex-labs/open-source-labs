# Analisar os Resultados

Vamos visualizar o modelo aprendido do KRR e do SVR quando a complexidade/regularização e a largura de banda do kernel RBF são otimizadas usando a busca em grade.

```python
import matplotlib.pyplot as plt

sv_ind = svr.best_estimator_.support_
plt.scatter(
    X[sv_ind],
    y[sv_ind],
    c="r",
    s=50,
    label="Vetores de suporte SVR",
    zorder=2,
    edgecolors=(0, 0, 0),
)
plt.scatter(X[:100], y[:100], c="k", label="dados", zorder=1, edgecolors=(0, 0, 0))
plt.plot(
    X_plot,
    y_svr,
    c="r",
    label="SVR (ajuste: %.3fs, previsão: %.3fs)" % (svr_fit, svr_predict),
)
plt.plot(
    X_plot, y_kr, c="g", label="KRR (ajuste: %.3fs, previsão: %.3fs)" % (kr_fit, kr_predict)
)
plt.xlabel("dados")
plt.ylabel("alvo")
plt.title("SVR versus Ridge Kernel")
_ = plt.legend()
```
