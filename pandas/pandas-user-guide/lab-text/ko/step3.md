# 부분 문자열 추출

정규 표현식 (regular expression) 을 사용하여 부분 문자열을 추출할 수 있습니다. `extract` 메서드는 하나 이상의 캡처 그룹 (capture group) 이 있는 정규 표현식을 허용합니다.

```python
# extract the first digit from each string
s = pd.Series(["a1", "b2", "c3"], dtype="string")
s.str.extract(r"(\d)", expand=False)
```
