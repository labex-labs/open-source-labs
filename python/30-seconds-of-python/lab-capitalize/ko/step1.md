# 문자열 대문자화 (Capitalize String)

`capitalize_string(s, lower_rest=False)`라는 Python 함수를 작성하세요. 이 함수는 문자열을 인수로 받아 첫 글자가 대문자로 된 새로운 문자열을 반환합니다. 이 함수는 선택적 매개변수 `lower_rest`를 가져야 하며, 이 매개변수가 `True`로 설정되면 나머지 문자열을 소문자로 변환합니다.

```python
def capitalize(s, lower_rest = False):
  return ''.join([s[:1].upper(), (s[1:].lower() if lower_rest else s[1:])])
```

```python
capitalize('fooBar') # 'FooBar'
capitalize('fooBar', True) # 'Foobar'
```
