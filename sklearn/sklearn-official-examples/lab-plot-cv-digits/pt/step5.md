# Plotar os resultados

Finalmente, plotamos as pontuações médias em função de C, e também incluímos barras de erro para visualizar o desvio padrão.

```python
import matplotlib.pyplot as plt

plt.figure()
plt.semilogx(C_s, scores)
plt.semilogx(C_s, np.array(scores) + np.array(scores_std), "b--")
plt.semilogx(C_s, np.array(scores) - np.array(scores_std), "b--")
locs, labels = plt.yticks()
plt.yticks(locs, list(map(lambda x: "%g" % x, locs)))
plt.ylabel("Pontuação CV")
plt.xlabel("Parâmetro C")
plt.ylim(0, 1.1)
plt.show()
```
