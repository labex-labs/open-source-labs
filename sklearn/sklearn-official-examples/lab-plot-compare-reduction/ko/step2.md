# 파이프라인 생성 및 매개변수 그리드 정의

차원 축소를 수행한 후 서포트 벡터 분류기를 사용하여 예측하는 파이프라인을 생성합니다. 비지도 학습 PCA 및 NMF 차원 축소와 함께, 단변량 특징 선택을 그리드 검색 중에 사용할 것입니다.

```python
pipe = Pipeline(
    [
        ("scaling", MinMaxScaler()),
        # reduce_dim 단계는 param_grid 에 의해 채워집니다.
        ("reduce_dim", "passthrough"),
        ("classify", LinearSVC(dual=False, max_iter=10000)),
    ]
)

N_FEATURES_OPTIONS = [2, 4, 8]
C_OPTIONS = [1, 10, 100, 1000]
param_grid = [
    {
        "reduce_dim": [PCA(iterated_power=7), NMF(max_iter=1_000)],
        "reduce_dim__n_components": N_FEATURES_OPTIONS,
        "classify__C": C_OPTIONS,
    },
    {
        "reduce_dim": [SelectKBest(mutual_info_classif)],
        "reduce_dim__k": N_FEATURES_OPTIONS,
        "classify__C": C_OPTIONS,
    },
]
reducer_labels = ["PCA", "NMF", "KBest(mutual_info_classif)"]
```
