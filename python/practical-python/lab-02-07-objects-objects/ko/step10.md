# 모든 것은 객체 (Everything is an object)

숫자, 문자열, 리스트, 함수, 예외, 클래스, 인스턴스 등은 모두 객체입니다. 이는 이름을 지정할 수 있는 모든 객체가 데이터로 전달되고, 컨테이너에 배치되는 등, 어떠한 제약 없이 사용될 수 있음을 의미합니다. _특별한_ 종류의 객체는 없습니다. 때로는 모든 객체가 "일급 객체 (first-class)"라고 말하기도 합니다.

간단한 예시:

```python
>>> import math
>>> items = [abs, math, ValueError ]
>>> items
[<built-in function abs>,
  <module 'math' (builtin)>,
  <type 'exceptions.ValueError'>]
>>> items[0](-45)
45
>>> items[1].sqrt(2)
1.4142135623730951
>>> try:
        x = int('not a number')
    except items[2]:
        print('Failed!')
Failed!
>>>
```

여기서 `items`는 함수, 모듈 및 예외를 포함하는 리스트입니다. 원래 이름 대신 리스트의 항목을 직접 사용할 수 있습니다.

```python
items[0](-45)       # abs
items[1].sqrt(2)    # math
except items[2]:    # ValueError
```

큰 힘에는 책임이 따릅니다. 그렇게 할 수 있다고 해서 반드시 해야 하는 것은 아닙니다.

이 일련의 연습에서는 일급 객체에서 비롯되는 몇 가지 강력한 기능에 대해 살펴봅니다.
