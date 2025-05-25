# Plotar os Coeficientes Verdadeiros e Estimados

Comparamos os coeficientes de cada modelo com os pesos do modelo gerador verdadeiro.

```python
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import SymLogNorm

plt.figure(figsize=(10, 6))
ax = sns.heatmap(
    df.T,
    norm=SymLogNorm(linthresh=10e-4, vmin=-80, vmax=80),
    cbar_kws={"label": "valores dos coeficientes"},
    cmap="seismic_r",
)
plt.ylabel("modelo linear")
plt.xlabel("coeficientes")
plt.tight_layout(rect=(0, 0, 1, 0.95))
_ = plt.title("Coeficientes dos Modelos")
```
