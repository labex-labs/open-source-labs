# Die wahren und geschätzten Koeffizienten plotten

Wir vergleichen die Koeffizienten jedes Modells mit den Gewichten des wahren generativen Modells.

```python
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import SymLogNorm

plt.figure(figsize=(10, 6))
ax = sns.heatmap(
    df.T,
    norm=SymLogNorm(linthresh=10e-4, vmin=-80, vmax=80),
    cbar_kws={"label": "Koeffizientenwerte"},
    cmap="seismic_r",
)
plt.ylabel("lineares Modell")
plt.xlabel("Koeffizienten")
plt.tight_layout(rect=(0, 0, 1, 0.95))
_ = plt.title("Koeffizienten der Modelle")
```
