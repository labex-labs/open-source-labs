# 데이터셋 로드

`sklearn.datasets`의 `make_gaussian_quantiles` 함수를 사용하여 데이터셋을 생성합니다. 이 함수는 등방성 가우시안 분포를 생성하고 클래스 간의 분리를 추가하여 문제를 더 어렵게 만듭니다.

```python
X, y = make_gaussian_quantiles(
    n_samples=13000, n_features=10, n_classes=3, random_state=1
)
```
