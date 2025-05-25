# Plotar os resultados

Finalmente, plotamos os erros de treino e teste dos nossos modelos base e dos classificadores AdaBoost discretos e reais.

```python
import matplotlib.pyplot as plt
import seaborn as sns

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot([1, n_estimators], [dt_stump_err] * 2, "k-", label="Erro do Stump de Decisão")
ax.plot([1, n_estimators], [dt_err] * 2, "k--", label="Erro da Árvore de Decisão")

colors = sns.color_palette("colorblind")

ax.plot(
    np.arange(n_estimators) + 1,
    ada_discrete_err,
    label="Erro de Teste do AdaBoost Discreto",
    color=colors[0],
)
ax.plot(
    np.arange(n_estimators) + 1,
    ada_discrete_err_train,
    label="Erro de Treino do AdaBoost Discreto",
    color=colors[1],
)
ax.plot(
    np.arange(n_estimators) + 1,
    ada_real_err,
    label="Erro de Teste do AdaBoost Real",
    color=colors[2],
)
ax.plot(
    np.arange(n_estimators) + 1,
    ada_real_err_train,
    label="Erro de Treino do AdaBoost Real",
    color=colors[4],
)

ax.set_ylim((0.0, 0.5))
ax.set_xlabel("Número de aprendizes fracos")
ax.set_ylabel("Taxa de erro")

leg = ax.legend(loc="upper right", fancybox=True)
leg.get_frame().set_alpha(0.7)

plt.show()
```
