# Affinity Propagation 계산

`sklearn.cluster` 모듈의 `AffinityPropagation` 클래스를 사용하여 데이터셋에 대한 클러스터링을 수행합니다. `preference` 매개변수를 -50 으로 설정하여 생성될 클러스터의 수를 제어합니다. `preference` 값이 낮을수록 더 많은 클러스터가 생성됩니다. 그런 다음 클러스터링의 품질을 평가하기 위해 몇 가지 지표를 출력합니다.

```python
af = AffinityPropagation(preference=-50, random_state=0).fit(X)
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_

n_clusters_ = len(cluster_centers_indices)

print("Estimated number of clusters: %d" % n_clusters_)
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
print("Adjusted Rand Index: %0.3f" % metrics.adjusted_rand_score(labels_true, labels))
print(
    "Adjusted Mutual Information: %0.3f"
    % metrics.adjusted_mutual_info_score(labels_true, labels)
)
print(
    "Silhouette Coefficient: %0.3f"
    % metrics.silhouette_score(X, labels, metric="sqeuclidean")
)
```
