# 스펙트럴 클러스터링 적용

기본 eigen_solver='arpack'을 사용하여 스펙트럴 클러스터링을 적용합니다. eigen_solver='arpack', 'lobpcg', 또는 'amg' 중 어떤 구현된 솔버든 사용할 수 있습니다. eigen_solver='amg'를 선택하려면 'pyamg'라는 추가 패키지가 필요합니다. 분할의 품질과 계산 속도는 주로 솔버의 선택과 허용 오차 'eigen_tol'의 값에 따라 결정됩니다.

```python
# 기본 eigen_solver='arpack'을 사용하여 스펙트럴 클러스터링을 적용합니다.
# 구현된 솔버 중 eigen_solver='arpack', 'lobpcg', 또는 'amg'를 사용할 수 있습니다.
# eigen_solver='amg'를 선택하려면 'pyamg'라는 추가 패키지가 필요합니다.
# 분할의 품질과 계산 속도는 주로 솔버의 선택과 허용 오차 'eigen_tol'의 값에 따라 결정됩니다.
n_regions = 26
n_regions_plus = 3
for assign_labels in ("kmeans", "discretize", "cluster_qr"):
    t0 = time.time()
    labels = spectral_clustering(
        graph,
        n_clusters=(n_regions + n_regions_plus),
        eigen_tol=1e-7,
        assign_labels=assign_labels,
        random_state=42,
    )
    t1 = time.time()
    labels = labels.reshape(rescaled_coins.shape)
```
