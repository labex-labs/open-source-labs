# 샘플 가중치 생성

두 가지 샘플 가중치 집합을 생성합니다. 첫 번째 집합은 모든 포인트에 대해 일정하고, 두 번째 집합은 일부 이상치에 대해 더 큰 가중치를 갖습니다.

```python
sample_weight_last_ten = abs(np.random.randn(len(X)))
sample_weight_constant = np.ones(len(X))
sample_weight_last_ten[15:] *= 5
sample_weight_last_ten[9] *= 15
```
