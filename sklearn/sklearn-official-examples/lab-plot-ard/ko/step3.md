# 실제 계수와 추정 계수 시각화

각 모델의 계수를 실제 생성 모델의 가중치와 비교합니다.

```python
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import SymLogNorm

plt.figure(figsize=(10, 6))
ax = sns.heatmap(
    df.T,
    norm=SymLogNorm(linthresh=10e-4, vmin=-80, vmax=80),
    cbar_kws={"label": "계수 값"},
    cmap="seismic_r",
)
plt.ylabel("선형 모델")
plt.xlabel("계수")
plt.tight_layout(rect=(0, 0, 1, 0.95))
_ = plt.title("모델 계수")
```
