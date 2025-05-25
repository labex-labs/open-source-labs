# 레코드 배열을 구조화된 배열로 변환

레코드 배열을 다시 구조화된 배열로 변환하려면 `view` 메서드를 사용하고 구조화된 배열의 원래 dtype 을 지정할 수 있습니다.

```python
# Convert a record array to a structured array
x = recordarr.view(dtype=[('name', 'U10'), ('age', int)])
```
