# 해설 (Commentary)

인터프리터를 가지고 실험을 시작할 때, 다양한 객체에서 지원되는 연산에 대해 더 알고 싶어지는 경우가 많습니다. 예를 들어, 문자열에서 사용할 수 있는 연산은 어떻게 찾을 수 있을까요?

Python 환경에 따라 탭 자동 완성 (tab-completion) 을 통해 사용 가능한 메서드 목록을 볼 수 있습니다. 예를 들어, 다음을 입력해 보십시오.

```python
>>> s = 'hello world'
>>> s.<tab key>
>>>
```

탭 키를 눌러도 아무런 반응이 없다면, 내장 함수인 `dir()` 함수를 사용할 수 있습니다. 예를 들어:

```python
>>> s = 'hello'
>>> dir(s)
['__add__', '__class__', '__contains__', ..., 'find', 'format',
'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace',
'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition',
'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
'title', 'translate', 'upper', 'zfill']
>>>
```

`dir()`은 `(.)` 다음에 나타날 수 있는 모든 연산 목록을 생성합니다. 특정 연산에 대한 자세한 정보를 얻으려면 `help()` 명령을 사용하십시오.

```python
>>> help(s.upper)
Help on built-in function upper:

upper(...)
    S.upper() -> string

    Return a copy of the string S converted to uppercase.
>>>
```
