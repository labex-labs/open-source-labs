# Funções para Plotar Resultados

Vamos plotar as funções de resultados utilizando a biblioteca `matplotlib`. Usaremos a função `plt.subplot()` para criar dois subplots. No primeiro subplot, plotaremos os erros de treino e teste em função do parâmetro de regularização. Também plotaremos uma linha vertical no parâmetro de regularização ótimo. No segundo subplot, plotaremos os coeficientes verdadeiros e os coeficientes estimados.

```python
import matplotlib.pyplot as plt

plt.subplot(2, 1, 1)
plt.semilogx(alphas, train_errors, label="Treino")
plt.semilogx(alphas, test_errors, label="Teste")
plt.vlines(
    alpha_optim,
    plt.ylim()[0],
    np.max(test_errors),
    color="k",
    linewidth=3,
    label="Ótimo em teste",
)
plt.legend(loc="lower right")
plt.ylim([0, 1.2])
plt.xlabel("Parâmetro de regularização")
plt.ylabel("Desempenho")

# Mostrar coef_ estimado vs coef verdadeiro
plt.subplot(2, 1, 2)
plt.plot(coef, label="Coef verdadeiro")
plt.plot(coef_, label="Coef estimado")
plt.legend()
plt.subplots_adjust(0.09, 0.04, 0.94, 0.94, 0.26, 0.26)
plt.show()
```
