# Построение и анализ результатов

В этом шаге мы используем тепловую карту для визуализации разреженности истинных и оцененных коэффициентов соответствующих линейных моделей.

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.colors import SymLogNorm

df = pd.DataFrame(
    {
        "True coefficients": true_coef,
        "Lasso": lasso.coef_,
        "ARDRegression": ard.coef_,
        "ElasticNet": enet.coef_,
    }
)

plt.figure(figsize=(10, 6))
ax = sns.heatmap(
    df.T,
    norm=SymLogNorm(linthresh=10e-4, vmin=-1, vmax=1),
    cbar_kws={"label": "значения коэффициентов"},
    cmap="seismic_r",
)
plt.ylabel("линейная модель")
plt.xlabel("коэффициенты")
plt.title(
    f"Коэффициенты моделей\nLasso $R^2$: {r2_score_lasso:.3f}, "
    f"ARD $R^2$: {r2_score_ard:.3f}, "
    f"ElasticNet $R^2$: {r2_score_enet:.3f}"
)
plt.tight_layout()
```
