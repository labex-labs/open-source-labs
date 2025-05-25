# 실험 1 - 고정된 기준 레이블과 증가하는 클러스터 수

균일 분포 랜덤 레이블링을 생성하고 `random_labels` 함수를 사용하여 `n_classes`에 분포된 고정된 기준 레이블 집합 (`labels_a`) 을 만듭니다. 그리고 여러 개의 랜덤하게 "예측된" 레이블 집합 (`labels_b`) 을 평가하여 주어진 `n_clusters`에서 특정 지표의 변동성을 평가합니다.

```python
rng = np.random.RandomState(0)

def random_labels(n_samples, n_classes):
    return rng.randint(low=0, high=n_classes, size=n_samples)

def fixed_classes_uniform_labelings_scores(
    score_func, n_samples, n_clusters_range, n_classes, n_runs=5
):
    scores = np.zeros((len(n_clusters_range), n_runs))
    labels_a = random_labels(n_samples=n_samples, n_classes=n_classes)

    for i, n_clusters in enumerate(n_clusters_range):
        for j in range(n_runs):
            labels_b = random_labels(n_samples=n_samples, n_classes=n_clusters)
            scores[i, j] = score_func(labels_a, labels_b)
    return scores
```
