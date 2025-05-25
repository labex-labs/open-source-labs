# 결과 저장을 위한 배열 정의

```python
scores = np.empty((x_values.shape[0], n_splits))
amount_labeled = np.empty((x_values.shape[0], n_splits))
amount_iterations = np.empty((x_values.shape[0], n_splits))
```

실험 결과를 저장하기 위한 배열을 정의합니다.
