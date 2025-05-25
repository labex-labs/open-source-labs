# Visualizar os Resultados

Visualizamos os resultados da validação cruzada não aninhada e aninhada usando um gráfico de barras.

```python
from matplotlib import pyplot as plt

# Plotar gráfico de barras da diferença.
plt.bar(["Não Aninhada", "Aninhada"], [non_nested_score, nested_scores.mean()])
plt.ylim([0.9, 1.0])
plt.ylabel("Pontuação")
plt.title("Pontuações de Validação Cruzada Não Aninhada e Aninhada")
plt.show()
```
