# 문자열 메서드 사용

Pandas 는 문자열 데이터를 쉽게 조작할 수 있도록 다양한 문자열 처리 메서드를 제공합니다. 이러한 메서드는 누락된/NA 값을 자동으로 제외합니다.

```python
s = pd.Series(
    ["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"], dtype="string"
)

# convert to lowercase
s.str.lower()

# convert to uppercase
s.str.upper()

# calculate the length of each string
s.str.len()
```
