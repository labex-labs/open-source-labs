# Plotar os Resultados

Plotamos um histograma das pontuações de permutação (a distribuição nula) para o conjunto de dados iris original e os dados aleatorizados. Também indicamos a pontuação obtida pelo classificador nos dados originais usando uma linha vermelha. O valor p é exibido em cada gráfico.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# Dados originais
ax.hist(perm_scores_iris, bins=20, density=True)
ax.axvline(score_iris, ls="--", color="r")
score_label = f"Pontuação nos dados\noriginais: {score_iris:.2f}\n(valor-p: {pvalue_iris:.3f})"
ax.text(0.7, 10, score_label, fontsize=12)
ax.set_xlabel("Pontuação de precisão")
_ = ax.set_ylabel("Densidade de probabilidade")

plt.show()

fig, ax = plt.subplots()

# Dados aleatórios
ax.hist(perm_scores_rand, bins=20, density=True)
ax.set_xlim(0.13)
ax.axvline(score_rand, ls="--", color="r")
score_label = f"Pontuação nos dados\noriginais: {score_rand:.2f}\n(valor-p: {pvalue_rand:.3f})"
ax.text(0.14, 7.5, score_label, fontsize=12)
ax.set_xlabel("Pontuação de precisão")
ax.set_ylabel("Densidade de probabilidade")

plt.show()
```
