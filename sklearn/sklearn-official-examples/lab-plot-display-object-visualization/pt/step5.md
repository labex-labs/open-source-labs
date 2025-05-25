# Combinar Objetos de Exibição em um Único Gráfico

Os objetos de exibição armazenam os valores calculados que foram passados como argumentos. Isso permite que as visualizações sejam facilmente combinadas usando a API do Matplotlib. No exemplo a seguir, os gráficos são colocados lado a lado em uma linha.

```python
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))

roc_display.plot(ax=ax1)
pr_display.plot(ax=ax2)
plt.show()
```
