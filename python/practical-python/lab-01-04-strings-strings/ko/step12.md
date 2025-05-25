# 연습 1.13: 개별 문자 및 부분 문자열 추출

문자열은 문자의 배열입니다. 몇 개의 문자를 추출해 보십시오.

```python
>>> symbols[0]
?
>>> symbols[1]
?
>>> symbols[2]
?
>>> symbols[-1]        # 마지막 문자
?
>>> symbols[-2]        # 음수 인덱스는 문자열의 끝에서부터 시작합니다.
?
>>>
```

Python 에서 문자열은 읽기 전용입니다.

`symbols`의 첫 번째 문자를 소문자 'a'로 변경하려는 시도를 통해 이를 확인하십시오.

```python
>>> symbols[0] = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
```
