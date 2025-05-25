# 섞인 데이터셋 재정렬

NumPy 의 `argsort()` 함수를 사용하여 섞인 데이터셋을 재정렬하여 바이클러스터가 연속적으로 배치되도록 합니다.

```python
fit_data = data[np.argsort(model.row_labels_)]
fit_data = fit_data[:, np.argsort(model.column_labels_)]
```
