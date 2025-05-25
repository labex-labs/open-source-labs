# 배열의 데이터 유형 검색

배열의 데이터 유형을 확인하려면 `dtype` 속성에 접근할 수 있습니다. 예를 들어:

```python
z.dtype
# returns the dtype of array z, which is uint8
```

`dtype` 객체는 비트 너비 및 바이트 순서와 같은 유형에 대한 정보도 포함합니다. `dtype` 객체를 사용하여 정수인지 여부와 같은 유형의 속성을 쿼리할 수 있습니다. 예를 들어:

```python
d = np.dtype(int)
# creates a dtype object for int

np.issubdtype(d, np.integer)
# returns True, indicating that d is a subdtype of np.integer

np.issubdtype(d, np.floating)
# returns False, indicating that d is not a subdtype of np.floating
```
