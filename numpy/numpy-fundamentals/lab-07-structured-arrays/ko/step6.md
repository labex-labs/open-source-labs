# 레코드 배열 생성

레코드 배열은 인덱스 대신 속성으로 필드에 접근할 수 있도록 하는 ndarray 의 서브클래스입니다. `np.rec.array` 함수를 사용하여 레코드 배열을 생성할 수 있습니다.

```python
# Create a record array
recordarr = np.rec.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
```
