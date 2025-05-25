# 데이터 생성 및 간단한 히스토그램 그리기

1D 히스토그램을 생성하려면 숫자 벡터 하나만 있으면 됩니다. 2D 히스토그램의 경우 두 번째 벡터가 필요합니다. 아래에서 두 벡터를 모두 생성하고 각 벡터에 대한 히스토그램을 표시합니다.

```python
import matplotlib.pyplot as plt
import numpy as np

# 재현성을 위해 고정된 시드로 난수 생성기를 생성합니다.
rng = np.random.default_rng(19680801)

N_points = 100000
n_bins = 20

# 두 개의 정규 분포를 생성합니다.
dist1 = rng.standard_normal(N_points)
dist2 = 0.4 * rng.standard_normal(N_points) + 5

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# *bins* 키워드 인수를 사용하여 bin 의 수를 설정할 수 있습니다.
axs[0].hist(dist1, bins=n_bins)
axs[1].hist(dist2, bins=n_bins)

plt.show()
```
