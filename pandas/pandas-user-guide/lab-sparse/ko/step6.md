# 희소 데이터와 밀집 데이터 간 변환

희소 데이터에서 밀집 데이터로, 그리고 그 반대로 데이터를 쉽게 변환할 수 있습니다.

```python
# 희소 데이터에서 밀집 데이터로 변환
print(sdf.sparse.to_dense())

# 밀집 데이터에서 희소 데이터로 변환
dense = pd.DataFrame({"A": [1, 0, 0, 1]})
dtype = pd.SparseDtype(int, fill_value=0)
print(dense.astype(dtype))
```
