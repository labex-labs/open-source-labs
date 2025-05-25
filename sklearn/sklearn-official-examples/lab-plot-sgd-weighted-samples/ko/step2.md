# 가중치가 부여된 데이터셋 생성

NumPy 라이브러리를 사용하여 가중치가 부여된 데이터셋을 생성합니다. 랜덤 값을 가진 20 개의 점을 생성하고 마지막 10 개의 샘플에 더 큰 가중치를 할당합니다.

```python
np.random.seed(0)
X = np.r_[np.random.randn(10, 2) + [1, 1], np.random.randn(10, 2)]
y = [1] * 10 + [-1] * 10
sample_weight = 100 * np.abs(np.random.randn(20))
sample_weight[:10] *= 10
```
