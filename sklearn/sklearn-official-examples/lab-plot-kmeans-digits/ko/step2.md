# 평가 벤치마크 정의

K-Means 의 서로 다른 초기화 방법을 비교하기 위한 벤치마크를 정의합니다. 이 벤치마크는 다음을 수행합니다.

- `StandardScaler`를 사용하여 데이터를 스케일링하는 파이프라인 생성
- 파이프라인 적합 (fitting) 시간 측정
- 서로 다른 지표를 통해 얻은 군집화 성능 측정

```python
from time import time
from sklearn import metrics
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def bench_k_means(kmeans, name, data, labels):
    """KMeans 초기화 방법을 평가하기 위한 벤치마크.

    매개변수
    ----------
    kmeans : KMeans 인스턴스
        이미 초기화된 `KMeans` 인스턴스.
    name : str
        전략에 주어진 이름. 결과 표시에 사용됩니다.
    data : ndarray 형태 (n_samples, n_features)
        군집화할 데이터.
    labels : ndarray 형태 (n_samples,)
        일부 감독이 필요한 군집화 지표를 계산하는 데 사용되는 레이블.
    """
    t0 = time()
    estimator = make_pipeline(StandardScaler(), kmeans).fit(data)
    fit_time = time() - t0
    results = [name, fit_time, estimator[-1].inertia_]

    # 오직 실제 레이블과 추정기 레이블만 필요한 지표 정의
    clustering_metrics = [
        metrics.homogeneity_score,
        metrics.completeness_score,
        metrics.v_measure_score,
        metrics.adjusted_rand_score,
        metrics.adjusted_mutual_info_score,
    ]
    results += [m(labels, estimator[-1].labels_) for m in clustering_metrics]

    # 실루엣 점수는 전체 데이터셋이 필요합니다.
    results += [
        metrics.silhouette_score(
            data,
            estimator[-1].labels_,
            metric="euclidean",
            sample_size=300,
        )
    ]

    # 결과 표시
    formatter_result = (
        "{:9s}\t{:.3f}s\t{:.0f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}"
    )
    print(formatter_result.format(*results))
```
