# 평가 지표

결과 클러스터의 품질을 정량화하기 위해 평가 지표를 사용할 수 있습니다. 동질성 (homogeneity), 완전성 (completeness), V-측도 (V-measure), 조정된 랜드 지수 (adjusted Rand index), 조정된 상호 정보 (adjusted mutual information), 실루엣 계수 (silhouette coefficient) 지표를 사용합니다. 이러한 지표는 sklearn.metrics 모듈에서 제공됩니다. 참값 레이블 (ground truth labels) 이 알려지지 않은 경우, 모델 결과 자체를 사용하여 평가를 수행할 수 있습니다. 이 경우 실루엣 계수가 유용합니다.

```python
print(f"Homogeneity: {metrics.homogeneity_score(labels_true, labels):.3f}")
print(f"Completeness: {metrics.completeness_score(labels_true, labels):.3f}")
print(f"V-measure: {metrics.v_measure_score(labels_true, labels):.3f}")
print(f"Adjusted Rand Index: {metrics.adjusted_rand_score(labels_true, labels):.3f}")
print(f"Adjusted Mutual Information: {metrics.adjusted_mutual_info_score(labels_true, labels):.3f}")
print(f"Silhouette Coefficient: {metrics.silhouette_score(X, labels):.3f}")
```
