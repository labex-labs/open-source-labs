# SparseDtype 이해

`SparseDtype`은 희소하지 않은 값의 dtype 과 스칼라 채움 값 (fill value) 을 저장합니다. dtype 만 전달하거나, 명시적인 채움 값을 함께 전달하여 생성할 수 있습니다.

```python
# SparseDtype 생성
print(pd.SparseDtype(np.dtype('datetime64[ns]')))

# 명시적인 채움 값을 사용하여 SparseDtype 생성
print(pd.SparseDtype(np.dtype('datetime64[ns]'), fill_value=pd.Timestamp('2017-01-01')))
```
