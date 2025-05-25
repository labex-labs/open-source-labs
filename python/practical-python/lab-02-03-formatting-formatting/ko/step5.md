# C 스타일 서식 지정 (C-Style Formatting)

서식 지정 연산자 `%`를 사용할 수도 있습니다.

```python
>>> 'The value is %d' % 3
'The value is 3'
>>> '%5d %-5d %10d' % (3,4,5)
'    3 4              5'
>>> '%0.2f' % (3.1415926,)
'3.14'
```

이 방식은 오른쪽에 단일 항목 또는 튜플을 필요로 합니다. 서식 코드 또한 C 의 `printf()`를 모델로 합니다.

_참고: 바이트 문자열에서 사용 가능한 유일한 서식 지정 방식입니다._

```python
>>> b'%s has %d messages' % (b'Dave', 37)
b'Dave has 37 messages'
>>> b'%b has %d messages' % (b'Dave', 37)  # %b may be used instead of %s
b'Dave has 37 messages'
>>>
```
