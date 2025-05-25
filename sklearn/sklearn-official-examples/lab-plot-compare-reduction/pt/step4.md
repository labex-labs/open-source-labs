# Plotar resultados

Plotaremos os resultados do `GridSearchCV` usando um gráfico de barras. Isso nos permitirá comparar a precisão de diferentes técnicas de redução de recursos.

```python
import pandas as pd

mean_scores = np.array(grid.cv_results_["mean_test_score"])
# as pontuações estão na ordem da iteração do param_grid, que é alfabética
mean_scores = mean_scores.reshape(len(C_OPTIONS), -1, len(N_FEATURES_OPTIONS))
# seleciona a pontuação para o melhor C
mean_scores = mean_scores.max(axis=0)
# cria um DataFrame para facilitar o plot
mean_scores = pd.DataFrame(
    mean_scores.T, index=N_FEATURES_OPTIONS, columns=reducer_labels
)

ax = mean_scores.plot.bar()
ax.set_title("Comparando técnicas de redução de recursos")
ax.set_xlabel("Número reduzido de recursos")
ax.set_ylabel("Precisão de classificação de dígitos")
ax.set_ylim((0, 1))
ax.legend(loc="upper left")

plt.show()
```
