# Graficar los coeficientes reales y estimados

Comparamos los coeficientes de cada modelo con los pesos del modelo generativo real.

```python
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import SymLogNorm

plt.figure(figsize=(10, 6))
ax = sns.heatmap(
    df.T,
    norm=SymLogNorm(linthresh=10e-4, vmin=-80, vmax=80),
    cbar_kws={"label": "valores de los coeficientes"},
    cmap="seismic_r",
)
plt.ylabel("modelo lineal")
plt.xlabel("coeficientes")
plt.tight_layout(rect=(0, 0, 1, 0.95))
_ = plt.title("Coeficientes de los modelos")
```
