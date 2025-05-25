# 희소 계산 수행

NumPy ufunc 을 SparseArray 에 적용하여 결과로 SparseArray 를 얻을 수 있습니다.

```python
# SparseArray 생성
arr = pd.arrays.SparseArray([1., np.nan, np.nan, -2., np.nan])

# NumPy ufunc 적용
print(np.abs(arr))
```
