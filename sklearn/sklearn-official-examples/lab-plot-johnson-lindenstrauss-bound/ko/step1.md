# 이론적 한계

첫 번째 단계는 존슨 - 린덴슈트라우스 보조정리의 이론적 한계를 탐색하는 것입니다. 샘플 수 `n_samples`가 증가함에 따라 `eps`-임베딩을 보장하기 위해 필요한 최소 차원을 플롯할 것입니다. 무작위 투영 `p`에 의해 도입되는 왜곡은 다음과 같은 사실에 의해 주장됩니다. `p`는 다음과 같이 정의된 좋은 확률로 `eps`-임베딩을 정의합니다.

`(1 - eps) \|u - v\|^2 < \|p(u) - p(v)\|^2 < (1 + eps) \|u - v\|^2`

여기서 `u`와 `v`는 `(n_samples, n_features)` 모양의 데이터셋에서 가져온 임의의 행이고, `p`는 `(n_components, n_features)` 모양의 무작위 가우시안 `N(0, 1)` 행렬 (또는 희소 아클리오타스 행렬) 에 의한 투영입니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.random_projection import johnson_lindenstrauss_min_dim

# 허용 가능한 왜곡의 범위
eps_range = np.linspace(0.1, 0.99, 5)
colors = plt.cm.Blues(np.linspace(0.3, 1.0, len(eps_range)))

# 임베딩할 샘플 수 (관측치) 의 범위
n_samples_range = np.logspace(1, 9, 9)

plt.figure()
for eps, color in zip(eps_range, colors):
    min_n_components = johnson_lindenstrauss_min_dim(n_samples_range, eps=eps)
    plt.loglog(n_samples_range, min_n_components, color=color)

plt.legend([f"eps = {eps:0.1f}" for eps in eps_range], loc="lower right")
plt.xlabel("eps-임베딩할 관측치의 수")
plt.ylabel("최소 차원 수")
plt.title("존슨 - 린덴슈트라우스 한계:\nn_samples 대 n_components")
plt.show()
```
