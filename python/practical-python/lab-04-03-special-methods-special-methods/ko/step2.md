# 문자열 변환을 위한 특수 메서드

객체는 두 가지 문자열 표현을 갖습니다.

```python
>>> from datetime import date
>>> d = date(2012, 12, 21)
>>> print(d)
2012-12-21
>>> d
datetime.date(2012, 12, 21)
>>>
```

`str()` 함수는 보기 좋은 출력물을 생성하는 데 사용됩니다.

```python
>>> str(d)
'2012-12-21'
>>>
```

`repr()` 함수는 프로그래머를 위해 더 자세한 표현을 생성하는 데 사용됩니다.

```python
>>> repr(d)
'datetime.date(2012, 12, 21)'
>>>
```

이러한 함수 `str()`과 `repr()`은 클래스 내에서 표시될 문자열을 생성하기 위해 한 쌍의 특수 메서드를 사용합니다.

```python
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Used with `str()`
    def __str__(self):
        return f'{self.year}-{self.month}-{self.day}'

    # Used with `repr()`
    def __repr__(self):
        return f'Date({self.year},{self.month},{self.day})'
```

_참고: `__repr__()`의 관례는 `eval()`에 제공될 때 기본 객체를 다시 생성하는 문자열을 반환하는 것입니다. 이것이 불가능한 경우, 쉽게 읽을 수 있는 종류의 표현이 대신 사용됩니다._
