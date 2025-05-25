# Plotando os resultados

Finalmente, plotamos o quão bem nossos dois regressores, o regressor de árvore de decisão única e o regressor AdaBoost, conseguiram ajustar os dados. Usamos a função `scatter()` do Matplotlib para plotar as amostras de treinamento e os valores previstos de ambos os regressores. Usamos a função `plot()` do Matplotlib para plotar os valores previstos contra os dados para ambos os regressores. Adicionamos uma legenda ao gráfico para distinguir entre os dois regressores.

```python
import matplotlib.pyplot as plt
import seaborn as sns

colors = sns.color_palette("colorblind")

plt.figure()
plt.scatter(X, y, color=colors[0], label="training samples")
plt.plot(X, y_1, color=colors[1], label="n_estimators=1", linewidth=2)
plt.plot(X, y_2, color=colors[2], label="n_estimators=300", linewidth=2)
plt.xlabel("dados")
plt.ylabel("alvo")
plt.title("Regressão de Árvore de Decisão Boostada")
plt.legend()
plt.show()
```
