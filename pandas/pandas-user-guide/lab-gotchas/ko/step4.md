# NA 값 처리

Pandas 는 결측값을 가질 수 있는 정수를 표현하기 위해 nullable-integer 확장 데이터 유형 (extension dtypes) 을 제공합니다.

```python
s_int = pd.Series([1, 2, 3, 4, 5], index=list("abcde"), dtype=pd.Int64Dtype())
s2_int = s_int.reindex(["a", "b", "c", "f", "u"])
```
