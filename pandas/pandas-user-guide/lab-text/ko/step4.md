# 문자열 검사

`contains` 및 `match` 메서드를 사용하여 요소가 패턴을 포함하는지 또는 일치하는지 확인할 수 있습니다.

```python
# check if each string contains the pattern "a"
s.str.contains("a", na=False)

# check if each string matches the pattern "a"
s.str.match("a", na=False)
```
