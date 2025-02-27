# Tracer les coefficients réels et estimés

Nous comparons les coefficients de chaque modèle avec les poids du modèle générateur réel.

```python
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import SymLogNorm

plt.figure(figsize=(10, 6))
ax = sns.heatmap(
    df.T,
    norm=SymLogNorm(linthresh=10e-4, vmin=-80, vmax=80),
    cbar_kws={"label": "valeurs des coefficients"},
    cmap="seismic_r",
)
plt.ylabel("modèle linéaire")
plt.xlabel("coefficients")
plt.tight_layout(rect=(0, 0, 1, 0.95))
_ = plt.title("Coefficients des modèles")
```
