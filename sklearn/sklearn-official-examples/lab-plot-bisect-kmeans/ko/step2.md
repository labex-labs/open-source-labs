# 샘플 데이터 생성

이 단계에서는 scikit-learn 의 `make_blobs()` 함수를 사용하여 샘플 데이터를 생성합니다. 2 개의 중심점을 가진 10,000 개의 샘플을 생성합니다.

```python
n_samples = 10000
random_state = 0
X, _ = make_blobs(n_samples=n_samples, centers=2, random_state=random_state)
```
