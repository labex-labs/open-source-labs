# 더미 변수 생성

`get_dummies` 메서드를 사용하여 문자열 데이터로부터 더미 변수 (dummy variables) 를 생성할 수 있습니다.

```python
# create dummy variables
s = pd.Series(["a", "a|b", np.nan, "a|c"], dtype="string")
s.str.get_dummies(sep="|")
```
