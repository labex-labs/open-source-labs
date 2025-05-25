# 결과 플롯 및 분석

이 단계에서는 히트맵을 사용하여 각 선형 모델의 실제 및 추정 계수의 희소성을 시각화합니다.

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
    cbar_kws={"label": "계수 값"},
    cmap="seismic_r",
)
plt.ylabel("선형 모델")
plt.xlabel("계수")
plt.title(
    f"모델 계수\nLasso $R^2$: {r2_score_lasso:.3f}, "
    f"ARD $R^2$: {r2_score_ard:.3f}, "
    f"ElasticNet $R^2$: {r2_score_enet:.3f}"
)
plt.tight_layout()
```
