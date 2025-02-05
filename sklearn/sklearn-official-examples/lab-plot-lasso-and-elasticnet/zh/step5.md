# 结果的绘制与分析

在这一步中，我们使用热图来可视化各个线性模型的真实系数和估计系数的稀疏性。

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.colors import SymLogNorm

df = pd.DataFrame(
    {
        "真实系数": true_coef,
        "套索（Lasso）": lasso.coef_,
        "自动相关性确定（ARD）回归": ard.coef_,
        "弹性网络（ElasticNet）": enet.coef_,
    }
)

plt.figure(figsize=(10, 6))
ax = sns.heatmap(
    df.T,
    norm=SymLogNorm(linthresh=10e-4, vmin=-1, vmax=1),
    cbar_kws={"label": "系数值"},
    cmap="seismic_r"
)
plt.ylabel("线性模型")
plt.xlabel("系数")
plt.title(
    f"模型的系数\n套索（Lasso） $R^2$: {r2_score_lasso:.3f}, "
    f"自动相关性确定（ARD） $R^2$: {r2_score_ard:.3f}, "
    f"弹性网络（ElasticNet） $R^2$: {r2_score_enet:.3f}"
)
plt.tight_layout()
```
