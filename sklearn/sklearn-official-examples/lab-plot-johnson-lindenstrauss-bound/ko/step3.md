# 실험적 검증

다음 단계는 20 뉴스그룹 텍스트 문서 데이터셋 또는 숫자 데이터셋에서 존슨 - 린덴슈트라우스 경계를 실험적으로 검증하는 것입니다. 20 뉴스그룹 데이터셋을 사용하고 총 100,000 개의 특징을 가진 300 개의 문서를 희소 무작위 행렬을 사용하여 목표 차원 수 `n_components`가 다양한 값을 갖는 더 작은 유클리드 공간으로 투영할 것입니다.

```python
import sys
from time import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_20newsgroups_vectorized
from sklearn.random_projection import SparseRandomProjection
from sklearn.metrics.pairwise import euclidean_distances

data = fetch_20newsgroups_vectorized().data[:300]

n_samples, n_features = data.shape
print(f"Embedding {n_samples} samples with dim {n_features} using various random projections")

n_components_range = np.array([300, 1_000, 10_000])
dists = euclidean_distances(data, squared=True).ravel()

# 동일한 샘플 쌍만 선택
nonzero = dists != 0
dists = dists[nonzero]

for n_components in n_components_range:
    t0 = time()
    rp = SparseRandomProjection(n_components=n_components)
    projected_data = rp.fit_transform(data)
    print(f"Projected {n_samples} samples from {n_features} to {n_components} in {time() - t0:0.3f}s")
    if hasattr(rp, "components_"):
        n_bytes = rp.components_.data.nbytes
        n_bytes += rp.components_.indices.nbytes
        print(f"Random matrix with size: {n_bytes / 1e6:0.3f} MB")

    projected_dists = euclidean_distances(projected_data, squared=True).ravel()[nonzero]

    plt.figure()
    min_dist = min(projected_dists.min(), dists.min())
    max_dist = max(projected_dists.max(), dists.max())
    plt.hexbin(
        dists,
        projected_dists,
        gridsize=100,
        cmap=plt.cm.PuBu,
        extent=[min_dist, max_dist, min_dist, max_dist],
    )
    plt.xlabel("원래 공간의 쌍별 제곱 거리")
    plt.ylabel("투영된 공간의 쌍별 제곱 거리")
    plt.title("n_components=%d에 대한 쌍별 거리 분포" % n_components)
    cb = plt.colorbar()
    cb.set_label("샘플 쌍 개수")

    rates = projected_dists / dists
    print(f"평균 거리 비율: {np.mean(rates):.2f} ({np.std(rates):.2f})")

    plt.figure()
    plt.hist(rates, bins=50, range=(0.0, 2.0), edgecolor="k", density=True)
    plt.xlabel("제곱 거리 비율: 투영된 / 원래")
    plt.ylabel("샘플 쌍의 분포")
    plt.title("n_components=%d에 대한 쌍별 거리 비율 히스토그램" % n_components)
```
