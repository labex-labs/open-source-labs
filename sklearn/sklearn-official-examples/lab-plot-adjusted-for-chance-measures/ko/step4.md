# 실험 2 - 클래스 수와 클러스터 수 변화

이 섹션에서는 여러 지표를 사용하여 2 개의 균일 분포 랜덤 레이블링을 평가하는 유사한 함수를 정의합니다. 이 경우 각 가능한 값에 대해 클래스 수와 할당된 클러스터 수가 `n_clusters_range` 내에서 일치합니다.

```python
def uniform_labelings_scores(score_func, n_samples, n_clusters_range, n_runs=5):
    scores = np.zeros((len(n_clusters_range), n_runs))

    for i, n_clusters in enumerate(n_clusters_range):
        for j in range(n_runs):
            labels_a = random_labels(n_samples=n_samples, n_classes=n_clusters)
            labels_b = random_labels(n_samples=n_samples, n_classes=n_clusters)
            scores[i, j] = score_func(labels_a, labels_b)
    return scores
```
