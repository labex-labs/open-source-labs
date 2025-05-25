# 데이터에 노이즈 추가

그런 다음 numpy 를 사용하여 데이터 포인트 간의 쌍대 거리에 노이즈를 추가합니다.

```python
similarities = euclidean_distances(X_true)

# 유사성에 노이즈 추가
noise = np.random.rand(n_samples, n_samples)
noise = noise + noise.T
noise[np.arange(noise.shape[0]), np.arange(noise.shape[0])] = 0
similarities += noise
```
