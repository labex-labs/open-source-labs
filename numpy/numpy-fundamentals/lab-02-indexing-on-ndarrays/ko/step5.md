# 필드 접근 (Field Access)

ndarray 객체가 구조화된 배열인 경우, 배열의 필드는 문자열을 사용하여 배열을 인덱싱하여 딕셔너리처럼 접근할 수 있습니다.

```python
x = np.array([(1, 2), (3, 4), (5, 6)], dtype=[('a', np.int32), ('b', np.int32)])
print(x['a'])  # Output: [1, 3, 5]
```
