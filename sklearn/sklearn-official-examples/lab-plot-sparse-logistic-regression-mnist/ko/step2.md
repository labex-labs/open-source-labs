# MNIST 데이터셋 로드

scikit-learn 의 `fetch_openml` 함수를 사용하여 MNIST 데이터셋을 로드합니다. `train_samples` 값을 5000 으로 설정하여 데이터의 일부를 선택합니다.

```python
# 더 빠른 수렴을 위해 줄임
t0 = time.time()
train_samples = 5000

# https://www.openml.org/d/554에서 데이터 로드
X, y = fetch_openml(
    "mnist_784", version=1, return_X_y=True, as_frame=False, parser="pandas"
)
```
