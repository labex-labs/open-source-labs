# 아이리스 데이터셋 로드 및 특징의 공분산 플롯

아이리스 데이터셋을 로드하고 특징들의 공분산을 플롯하여 특징 간의 상관관계를 살펴보겠습니다.

```python
import matplotlib.pyplot as plt
import numpy as np

from sklearn.decomposition import FactorAnalysis, PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

# 아이리스 데이터 로드
data = load_iris()
X = StandardScaler().fit_transform(data["data"])
feature_names = data["feature_names"]

# 아이리스 특징의 공분산 플롯
ax = plt.axes()

im = ax.imshow(np.corrcoef(X.T), cmap="RdBu_r", vmin=-1, vmax=1)

ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(list(feature_names), rotation=90)
ax.set_yticks([0, 1, 2, 3])
ax.set_yticklabels(list(feature_names))

plt.colorbar(im).ax.set_ylabel("$r$", rotation=0)
ax.set_title("아이리스 특징 상관 행렬")
plt.tight_layout()
```
