# exec() 기본 이해

Python 에서 `exec()` 함수는 런타임에 동적으로 생성된 코드를 실행할 수 있게 해주는 강력한 도구입니다. 이는 특정 입력 또는 구성에 따라 코드를 즉석에서 생성할 수 있음을 의미하며, 이는 많은 프로그래밍 시나리오에서 매우 유용합니다.

`exec()` 함수의 기본적인 사용법을 살펴보겠습니다. 이를 위해 Python 셸을 열어보겠습니다. 터미널을 열고 `python3`를 입력합니다. 이 명령은 Python 인터프리터를 시작하여 Python 코드를 직접 실행할 수 있게 해줍니다.

```bash
python3
```

이제 Python 코드를 문자열로 정의한 다음 `exec()` 함수를 사용하여 실행해 보겠습니다. 작동 방식은 다음과 같습니다.

```python
>>> code = '''
for i in range(n):
    print(i, end=' ')
'''
>>> n = 10
>>> exec(code)
0 1 2 3 4 5 6 7 8 9
```

이 예제에서:

1. 먼저, `code`라는 문자열을 정의했습니다. 이 문자열에는 Python for-loop 가 포함되어 있습니다. 이 루프는 `n`번 반복하고 각 반복 숫자를 인쇄하도록 설계되었습니다.
2. 그런 다음, 변수 `n`을 정의하고 값 10 을 할당했습니다. 이 변수는 루프에서 `range()` 함수의 상한으로 사용됩니다.
3. 그 후, `code` 문자열을 인수로 사용하여 `exec()` 함수를 호출했습니다. `exec()` 함수는 문자열을 가져와 Python 코드로 실행합니다.
4. 마지막으로, 루프가 실행되어 0 부터 9 까지의 숫자를 인쇄했습니다.

`exec()` 함수의 진정한 힘은 함수나 메서드와 같은 더 복잡한 코드 구조를 생성하는 데 사용할 때 더욱 분명해집니다. `__init__()` 메서드를 동적으로 생성하는 더 고급 예제를 시도해 보겠습니다.

```python
>>> class Stock:
...     _fields = ('name', 'shares', 'price')
...
>>> argstr = ','.join(Stock._fields)
>>> code = f'def __init__(self, {argstr}):\n'
>>> for name in Stock._fields:
...     code += f'    self.{name} = {name}\n'
...
>>> print(code)
def __init__(self, name,shares,price):
    self.name = name
    self.shares = shares
    self.price = price

>>> locs = { }
>>> exec(code, locs)
>>> Stock.__init__ = locs['__init__']

>>> # Now try the class
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
```

이 더 복잡한 예제에서:

1. 먼저, `_fields` 속성을 가진 `Stock` 클래스를 정의했습니다. 이 속성은 클래스의 속성 이름을 포함하는 튜플입니다.
2. 그런 다음, `__init__` 메서드에 대한 Python 코드를 나타내는 문자열을 생성했습니다. 이 메서드는 객체의 속성을 초기화하는 데 사용됩니다.
3. 다음으로, `exec()` 함수를 사용하여 코드 문자열을 실행했습니다. 또한 빈 딕셔너리 `locs`를 `exec()`에 전달했습니다. 실행 결과로 생성된 함수는 이 딕셔너리에 저장됩니다.
4. 그 후, 딕셔너리에 저장된 함수를 `Stock` 클래스의 `__init__` 메서드로 할당했습니다.
5. 마지막으로, `Stock` 클래스의 인스턴스를 생성하고 객체의 속성에 액세스하여 `__init__` 메서드가 올바르게 작동하는지 확인했습니다.

이 예제는 `exec()` 함수를 사용하여 런타임에 사용 가능한 데이터를 기반으로 메서드를 동적으로 생성하는 방법을 보여줍니다.
