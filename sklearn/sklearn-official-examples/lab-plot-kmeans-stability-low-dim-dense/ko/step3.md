# 초기화 방법의 정량적 평가

k-평균 초기화 전략이 알고리즘 수렴을 얼마나 강건하게 만드는지 평가할 것입니다. 클러스터링의 관성 (가장 가까운 클러스터 중심점까지의 제곱 거리의 합) 의 상대 표준 편차를 측정할 것입니다. 첫 번째 그림은 모델 (`KMeans` 또는 `MiniBatchKMeans`) 과 초기화 방법 (`init="random"` 또는 `init="k-means++"`) 의 각 조합에 대해 `n_init` 매개변수 (초기화 횟수를 제어) 값이 증가함에 따라 도달한 최상의 관성을 보여줍니다.

```python
n_runs = 5
n_init_range = np.array([1, 5, 10, 15, 20])

plt.figure()
plots = []
legends = []

cases = [
    (KMeans, "k-means++", {}, "^-"),
    (KMeans, "random", {}, "o-"),
    (MiniBatchKMeans, "k-means++", {"max_no_improvement": 3}, "x-"),
    (MiniBatchKMeans, "random", {"max_no_improvement": 3, "init_size": 500}, "d-"),
]

for factory, init, params, format in cases:
    print("Evaluation of %s with %s init" % (factory.__name__, init))
    inertia = np.empty((len(n_init_range), n_runs))

    for run_id in range(n_runs):
        X, y = make_data(run_id, n_samples_per_center, grid_size, scale)
        for i, n_init in enumerate(n_init_range):
            km = factory(
                n_clusters=n_clusters,
                init=init,
                random_state=run_id,
                n_init=n_init,
                **params,
            ).fit(X)
            inertia[i, run_id] = km.inertia_
    p = plt.errorbar(
        n_init_range, inertia.mean(axis=1), inertia.std(axis=1), fmt=format
    )
    plots.append(p[0])
    legends.append("%s with %s init" % (factory.__name__, init))

plt.xlabel("n_init")
plt.ylabel("inertia")
plt.legend(plots, legends)
plt.title("Mean inertia for various k-means init across %d runs" % n_runs)
```
