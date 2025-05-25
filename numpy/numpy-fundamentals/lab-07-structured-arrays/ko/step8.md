# 구조화된 배열을 레코드 배열로 변환

`view` 메서드를 사용하고 `np.recarray` 타입을 지정하여 구조화된 배열을 레코드 배열로 변환할 수 있습니다.

```python
# Convert a structured array to a record array
recordarr = x.view(np.recarray)
```
