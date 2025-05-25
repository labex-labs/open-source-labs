# 데이터셋 로드

`sklearn.datasets` 모듈의 `make_classification` 함수를 사용하여 분류 데이터셋을 생성합니다. 이 데이터셋은 400 개의 샘플과 12 개의 특징을 포함합니다. 데이터셋을 로드하는 코드는 다음과 같습니다.

```python
rng = np.random.RandomState(0)
X, y = datasets.make_classification(n_samples=400, n_features=12, random_state=rng)
```
