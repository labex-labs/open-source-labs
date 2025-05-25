# 문자열 소문자 변환

문자열 `s`를 인수로 받아 첫 글자를 소문자로 변환한 새 문자열을 반환하는 함수 `decapitalize(s, upper_rest = False)`를 작성하십시오. 이 함수는 선택적 매개변수 `upper_rest`도 가져야 하며, 이 매개변수를 `True`로 설정하면 나머지 문자열을 대문자로 변환합니다.

```python
def decapitalize(s, upper_rest = False):
  return ''.join([s[:1].lower(), (s[1:].upper() if upper_rest else s[1:])])
```

```python
decapitalize('FooBar') # 'fooBar'
decapitalize('FooBar', True) # 'fOOBAR'
```
