# 타입 변환 추가

현재 `MutInt` 클래스는 덧셈 및 비교 연산을 지원합니다. 그러나 `int()` 및 `float()`와 같은 Python 의 내장 변환 함수와는 작동하지 않습니다. 이러한 변환 함수는 Python 에서 매우 유용합니다. 예를 들어, 다른 계산 또는 연산을 위해 값을 정수 또는 부동 소수점 숫자로 변환하려는 경우 이러한 함수에 의존합니다. 따라서 `MutInt` 클래스가 이러한 함수와 함께 작동할 수 있도록 기능을 추가해 보겠습니다.

1. WebIDE 에서 `mutint.py`를 열고 다음 코드로 업데이트합니다.

```python
# mutint.py

from functools import total_ordering

@total_ordering
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

    def __eq__(self, other):
        """동등성 비교 처리: self == other."""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """작음 비교 처리: self < other."""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """int 로 변환합니다."""
        return self.value

    def __float__(self):
        """float 로 변환합니다."""
        return float(self.value)

    __index__ = __int__  # 배열 인덱싱 및 인덱스가 필요한 기타 연산 지원

    def __lshift__(self, other):
        """왼쪽 시프트 처리: self << other."""
        if isinstance(other, MutInt):
            return MutInt(self.value << other.value)
        elif isinstance(other, int):
            return MutInt(self.value << other)
        else:
            return NotImplemented

    def __rlshift__(self, other):
        """역순 왼쪽 시프트 처리: other << self."""
        if isinstance(other, int):
            return MutInt(other << self.value)
        else:
            return NotImplemented
```

`MutInt` 클래스에 세 가지 새로운 메서드를 추가했습니다.

1. `__int__()`: 이 메서드는 `MutInt` 클래스의 객체에 대해 `int()` 함수를 사용할 때 호출됩니다. 예를 들어, `MutInt` 객체 `a`가 있고 `int(a)`를 작성하면 Python 은 `a` 객체의 `__int__()` 메서드를 호출합니다.
2. `__float__()`: 마찬가지로 이 메서드는 `MutInt` 객체에 대해 `float()` 함수를 사용할 때 호출됩니다.
3. `__index__()`: 이 메서드는 특히 정수 인덱스가 필요한 연산에 사용됩니다. 예를 들어, 인덱스를 사용하여 목록의 요소에 액세스하거나 비트 길이 연산을 수행하려는 경우 Python 은 정수 인덱스가 필요합니다.
4. `__lshift__()`: 이 메서드는 `MutInt` 객체가 `<<` 연산자의 왼쪽에 있을 때 왼쪽 시프트 연산을 처리합니다.
5. `__rlshift__()`: 이 메서드는 `MutInt` 객체가 `<<` 연산자의 오른쪽에 있을 때 왼쪽 시프트 연산을 처리합니다.

`__index__` 메서드는 목록 인덱싱, 슬라이싱 및 비트 길이 연산과 같이 정수 인덱스가 필요한 연산에 매우 중요합니다. 간단한 구현에서는 `__int__`와 동일하게 설정했습니다. 이는 `MutInt` 객체의 값을 정수 인덱스로 직접 사용할 수 있기 때문입니다.

`__lshift__` 및 `__rlshift__` 메서드는 비트 단위 왼쪽 시프트 연산을 지원하는 데 필수적입니다. 이를 통해 `MutInt` 객체가 비트 단위 연산에 참여할 수 있으며, 이는 정수와 유사한 유형에 대한 일반적인 요구 사항입니다.

2. 이러한 새 메서드를 테스트하기 위해 `test_conversions.py`라는 새 테스트 파일을 생성합니다.

```python
# test_conversions.py

from mutint import MutInt

# MutInt 객체 생성
a = MutInt(3)

# 변환 테스트
print(f"int(a): {int(a)}")
print(f"float(a): {float(a)}")

# 인덱스로 사용 테스트
names = ['Dave', 'Guido', 'Paula', 'Thomas', 'Lewis']
print(f"names[a]: {names[a]}")

# 비트 연산에서 사용 테스트 (__index__ 필요)
print(f"1 << a: {1 << a}")  # 3 만큼 왼쪽으로 시프트

# 16 진수/8 진수/2 진수 함수 테스트 (__index__ 필요)
print(f"hex(a): {hex(a)}")
print(f"oct(a): {oct(a)}")
print(f"bin(a): {bin(a)}")

# 수정하고 다시 테스트
a.value = 4
print(f"\n값을 4 로 변경한 후:")
print(f"int(a): {int(a)}")
print(f"names[a]: {names[a]}")
```

3. 테스트 스크립트를 실행합니다.

```bash
python3 /home/labex/project/test_conversions.py
```

다음과 유사한 출력을 볼 수 있습니다.

```
int(a): 3
float(a): 3.0
names[a]: Thomas
1 << a: 8
hex(a): 0x3
oct(a): 0o3
bin(a): 0b11

값을 4로 변경한 후:
int(a): 4
names[a]: Lewis
```

이제 `MutInt` 클래스는 표준 Python 유형으로 변환될 수 있으며 정수 인덱스가 필요한 연산에 사용할 수 있습니다.

`__index__` 메서드는 특히 중요합니다. 이 메서드는 목록 인덱싱, 비트 단위 연산 및 `hex()`, `oct()`, `bin()`과 같은 다양한 함수와 같이 정수 인덱스가 필요한 상황에서 객체를 사용할 수 있도록 Python 에 도입되었습니다.

이러한 추가 기능을 통해 `MutInt` 클래스는 이제 상당히 완전한 기본 유형입니다. 가변이라는 추가적인 이점과 함께 일반 정수가 사용되는 대부분의 컨텍스트에서 사용할 수 있습니다.

## 완전한 MutInt 구현

다음은 추가한 모든 기능이 포함된 완전한 `MutInt` 구현입니다.

```python
# mutint.py

from functools import total_ordering

@total_ordering
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

    def __eq__(self, other):
        """동등성 비교 처리: self == other."""
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        """작음 비교 처리: self < other."""
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __int__(self):
        """int 로 변환합니다."""
        return self.value

    def __float__(self):
        """float 로 변환합니다."""
        return float(self.value)

    __index__ = __int__  # 배열 인덱싱 및 인덱스가 필요한 기타 연산 지원

    def __lshift__(self, other):
        """왼쪽 시프트 처리: self << other."""
        if isinstance(other, MutInt):
            return MutInt(self.value << other.value)
        elif isinstance(other, int):
            return MutInt(self.value << other)
        else:
            return NotImplemented

    def __rlshift__(self, other):
        """역순 왼쪽 시프트 처리: other << self."""
        if isinstance(other, int):
            return MutInt(other << self.value)
        else:
            return NotImplemented
```

이 구현은 Python 에서 새로운 기본 유형을 만드는 주요 측면을 다룹니다. 이를 더욱 완전하게 만들려면 뺄셈, 곱셈, 나눗셈 등과 같은 다른 연산에 대한 추가 메서드를 구현할 수 있습니다.
