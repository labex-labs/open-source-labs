# Построение графиков истинных и оцененных коэффициентов

Мы сравниваем коэффициенты каждой модели с весами истинной генеративной модели.

```python
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import SymLogNorm

plt.figure(figsize=(10, 6))
ax = sns.heatmap(
    df.T,
    norm=SymLogNorm(linthresh=10e-4, vmin=-80, vmax=80),
    cbar_kws={"label": "значения коэффициентов"},
    cmap="seismic_r",
)
plt.ylabel("линейная модель")
plt.xlabel("коэффициенты")
plt.tight_layout(rect=(0, 0, 1, 0.95))
_ = plt.title("коэффициенты моделей")
```
