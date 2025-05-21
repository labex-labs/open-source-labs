# 수학 연산 추가

현재 `MutInt` 클래스는 덧셈과 같은 수학 연산을 지원하지 않습니다. Python 에서 사용자 정의 클래스에 대해 이러한 연산을 활성화하려면 특수 메서드를 구현해야 합니다. 이러한 특수 메서드는 이중 밑줄로 둘러싸여 있기 때문에 "매직 메서드" 또는 "던더 메서드 (dunder methods)"라고도 합니다. 산술 연산에 대한 관련 특수 메서드를 구현하여 덧셈 기능을 추가해 보겠습니다.

1. WebIDE 에서 `mutint.py`를 열고 다음 코드로 업데이트합니다.

```python
# mutint.py

class MutInt:
    """
    생성 후 값을 수정할 수 있는 가변 정수 클래스입니다.
    """
    __slots__ = ['value']

    def __init__(self, value):
        """정수 값으로 초기화합니다."""
        self.value = value

    def __str__(self):
        """인쇄를 위한 문자열 표현을 반환합니다."""
        return str(self.value)

    def __repr__(self):
        """개발자 친화적인 문자열 표현을 반환합니다."""
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        """형식 사양을 사용하여 문자열 형식을 지원합니다."""
        return format(self.value, fmt)

    def __add__(self, other):
        """덧셈 처리: self + other."""
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        """역순 덧셈 처리: other + self."""
        # +와 같은 교환 연산의 경우 __add__를 재사용할 수 있습니다.
        return self.__add__(other)

    def __iadd__(self, other):
        """제자리 덧셈 처리: self += other."""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented
```

`MutInt` 클래스에 세 가지 새로운 메서드를 추가했습니다.

- `__add__()`: 이 메서드는 `+` 연산자가 `MutInt` 객체의 왼쪽에 사용될 때 호출됩니다. 이 메서드 내부에서 먼저 `other` 피연산자가 `MutInt` 또는 `int`의 인스턴스인지 확인합니다. 그렇다면 덧셈을 수행하고 결과로 새 `MutInt` 객체를 반환합니다. `other` 피연산자가 다른 것이면 `NotImplemented`를 반환합니다. 이렇게 하면 Python 이 다른 메서드를 시도하거나 `TypeError`를 발생시킵니다.
- `__radd__()`: 이 메서드는 `+` 연산자가 `MutInt` 객체의 오른쪽에 사용될 때 호출됩니다. 덧셈은 교환 연산 (즉, `a + b`는 `b + a`와 동일) 이므로 `__add__` 메서드를 간단히 재사용할 수 있습니다.
- `__iadd__()`: 이 메서드는 `+=` 연산자가 `MutInt` 객체에 사용될 때 호출됩니다. 새 객체를 생성하는 대신 기존 `MutInt` 객체를 수정하고 반환합니다.

2. 이러한 새 메서드를 테스트하기 위해 `test_math_ops.py`라는 새 테스트 파일을 생성합니다.

```python
# test_math_ops.py

from mutint import MutInt

# MutInt 객체 생성
a = MutInt(3)
b = MutInt(5)

# 일반 덧셈 테스트
c = a + b
print(f"a + b = {c}")

# int 를 사용한 덧셈 테스트
d = a + 10
print(f"a + 10 = {d}")

# 역순 덧셈 테스트
e = 7 + a
print(f"7 + a = {e}")

# 제자리 덧셈 테스트
print(f"Before a += 5: a = {a}")
a += 5
print(f"After a += 5: a = {a}")

# 참조 공유를 사용한 제자리 덧셈 테스트
f = a  # f 와 a 는 동일한 객체를 가리킵니다.
print(f"Before a += 10: a = {a}, f = {f}")
a += 10
print(f"After a += 10: a = {a}, f = {f}")

# 지원되지 않는 연산 테스트
try:
    result = a + 3.5  # float 를 더하는 것은 지원되지 않습니다.
    print(f"a + 3.5 = {result}")
except TypeError as e:
    print(f"Error when adding float: {e}")
```

이 테스트 파일에서는 먼저 `MutInt` 클래스를 가져옵니다. 그런 다음 몇 개의 `MutInt` 객체를 생성하고 다양한 유형의 덧셈 연산을 수행합니다. 또한 제자리 덧셈과 지원되지 않는 연산 (float 추가) 을 시도하는 경우를 테스트합니다.

3. 테스트 스크립트를 실행합니다.

```bash
python3 /home/labex/project/test_math_ops.py
```

다음과 유사한 출력을 볼 수 있습니다.

```
a + b = MutInt(8)
a + 10 = MutInt(13)
7 + a = MutInt(10)
Before a += 5: a = MutInt(3)
After a += 5: a = MutInt(8)
Before a += 10: a = MutInt(8), f = MutInt(8)
After a += 10: a = MutInt(18), f = MutInt(18)
Error when adding float: unsupported operand type(s) for +: 'MutInt' and 'float'
```

이제 `MutInt` 클래스는 기본 덧셈 연산을 지원합니다. `+=`를 사용했을 때 `a`와 `f`가 모두 업데이트되었음을 확인하십시오. 이는 `a += 10`이 새 객체를 생성하는 대신 기존 객체를 수정했음을 보여줍니다.

가변 객체 (mutable objects) 를 사용한 이 동작은 Python 의 내장 가변 유형 (mutable types) 인 리스트와 유사합니다. 예를 들어:

```python
a = [1, 2, 3]
b = a
a += [4, 5]  # a 와 b 가 모두 업데이트됩니다.
```

반대로, 튜플과 같은 불변 유형 (immutable types) 의 경우 `+=`는 새 객체를 생성합니다.

```python
c = (1, 2, 3)
d = c
c += (4, 5)  # c 는 새 객체이고, d 는 여전히 이전 객체를 가리킵니다.
```
