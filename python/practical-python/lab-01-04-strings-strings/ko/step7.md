# 문자열 불변성 (String Mutability)

문자열은 "불변 (immutable)" 또는 읽기 전용입니다. 생성된 후에는 값을 변경할 수 없습니다.

```python
>>> s = 'Hello World'
>>> s[1] = 'a'
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
```

**문자열 데이터를 조작하는 모든 연산과 메서드는 항상 새로운 문자열을 생성합니다.**
