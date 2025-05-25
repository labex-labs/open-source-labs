# 데이터 로드

다음으로, Scikit-learn 의 `fetch_openml` 함수를 사용하여 MNIST 데이터셋을 로드합니다.

```python
X, y = fetch_openml(
    "mnist_784", version=1, return_X_y=True, as_frame=False, parser="pandas"
)
```
