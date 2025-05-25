# 이진 분류 데이터셋 생성

다음으로, scikit-learn 에서 제공하는 `make_classification` 함수를 사용하여 이진 분류 데이터셋을 생성합니다. 이 함수를 통해 샘플 수, 특징 수, 클래스당 클러스터 수, 정보 특징 수를 지정할 수 있습니다. 재현성을 보장하기 위해 고정된 랜덤 상태 값을 사용합니다.

```python
X, y = make_classification(
    n_samples=500,
    n_features=25,
    n_clusters_per_class=1,
    n_informative=15,
    random_state=RANDOM_STATE,
)
```
