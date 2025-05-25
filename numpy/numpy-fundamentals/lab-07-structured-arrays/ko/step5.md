# 구조화 배열 비교

두 구조화 배열의 데이터 유형 (dtype) 이 같으면, 등가 연산자 (`==`) 를 사용하여 비교할 수 있습니다. 이는 모든 필드에 대해 동일한 값을 가진 요소를 나타내는 부울 배열을 반환합니다.

```python
# Compare two structured arrays
y = np.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
comparison = x == y
```
