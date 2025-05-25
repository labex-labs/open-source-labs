# 데이터셋 섞기

NumPy 의 `permutation()` 함수를 사용하여 데이터셋을 섞습니다.

```python
rng = np.random.RandomState(0)
row_idx = rng.permutation(data.shape[0])
col_idx = rng.permutation(data.shape[1])
data = data[row_idx][:, col_idx]
```
