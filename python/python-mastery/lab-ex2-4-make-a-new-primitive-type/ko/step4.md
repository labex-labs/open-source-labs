# 비교 연산 구현

현재 `MutInt` 객체는 서로 또는 일반 정수와 비교할 수 없습니다. Python 에서 `==`, `<`, `<=`, `>`, `>=`와 같은 비교 연산은 객체로 작업할 때 매우 유용합니다. 이를 통해 서로 다른 객체 간의 관계를 결정할 수 있으며, 이는 정렬, 필터링 및 조건문과 같은 많은 프로그래밍 시나리오에서 중요합니다. 따라서 비교 연산에 대한 특수 메서드를 구현하여 `MutInt` 클래스에 비교 기능을 추가해 보겠습니다.

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
```

몇 가지 주요 개선 사항을 추가했습니다.

1. `functools` 모듈에서 `@total_ordering` 데코레이터를 가져와 사용합니다. `@total_ordering` 데코레이터는 Python 에서 강력한 도구입니다. 클래스에 대한 비교 메서드를 구현할 때 많은 시간과 노력을 절약하는 데 도움이 됩니다. 여섯 개의 모든 비교 메서드 (`__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`) 를 수동으로 정의하는 대신 `__eq__`와 다른 비교 메서드 (이 경우 `__lt__`) 하나만 정의하면 됩니다. 그러면 데코레이터가 나머지 네 개의 비교 메서드를 자동으로 생성합니다.
2. 동등성 비교 (`==`) 를 처리하기 위해 `__eq__()` 메서드를 추가합니다. 이 메서드는 두 개의 `MutInt` 객체 또는 `MutInt` 객체와 정수가 동일한 값을 갖는지 확인하는 데 사용됩니다.
3. 작음 비교 (`<`) 를 처리하기 위해 `__lt__()` 메서드를 추가합니다. 이 메서드는 하나의 `MutInt` 객체 또는 정수와 비교된 `MutInt` 객체가 더 작은 값을 갖는지 확인하는 데 사용됩니다.

4. 이러한 새 메서드를 테스트하기 위해 `test_comparisons.py`라는 새 테스트 파일을 생성합니다.

```python
# test_comparisons.py

from mutint import MutInt

# MutInt 객체 생성
a = MutInt(3)
b = MutInt(3)
c = MutInt(5)

# 동등성 테스트
print(f"a == b: {a == b}")  # True 여야 함 (동일한 값)
print(f"a == c: {a == c}")  # False 여야 함 (다른 값)
print(f"a == 3: {a == 3}")  # True 여야 함 (int 와 비교)
print(f"a == 5: {a == 5}")  # False 여야 함 (다른 값)

# 작음 테스트
print(f"a < c: {a < c}")    # True 여야 함 (3 < 5)
print(f"c < a: {c < a}")    # False 여야 함 (5 는 < 3 이 아님)
print(f"a < 4: {a < 4}")    # True 여야 함 (3 < 4)

# 다른 비교 테스트 (@total_ordering 에서 제공)
print(f"a <= b: {a <= b}")  # True 여야 함 (3 <= 3)
print(f"a > c: {a > c}")    # False 여야 함 (3 은 > 5 가 아님)
print(f"c >= a: {c >= a}")  # True 여야 함 (5 >= 3)

# 다른 유형으로 테스트
print(f"a == '3': {a == '3'}")  # False 여야 함 (다른 유형)
```

이 테스트 파일에서는 여러 `MutInt` 객체를 생성하고 이에 대해 다양한 비교 연산을 수행합니다. 또한 `MutInt` 객체를 일반 정수 및 다른 유형 (이 경우 문자열) 과 비교합니다. 이러한 테스트를 실행하여 비교 메서드가 예상대로 작동하는지 확인할 수 있습니다.

3. 테스트 스크립트를 실행합니다.

```bash
python3 /home/labex/project/test_comparisons.py
```

다음과 유사한 출력을 볼 수 있습니다.

```
a == b: True
a == c: False
a == 3: True
a == 5: False
a < c: True
c < a: False
a < 4: True
a <= b: True
a > c: False
c >= a: True
a == '3': False
```

이제 `MutInt` 클래스는 모든 비교 연산을 지원합니다.

`@total_ordering` 데코레이터는 여섯 개의 모든 비교 메서드를 수동으로 구현할 필요가 없으므로 특히 유용합니다. `__eq__`와 `__lt__`만 제공하면 Python 이 나머지 네 개의 비교 메서드를 자동으로 파생할 수 있습니다.

사용자 정의 클래스를 구현할 때는 일반적으로 동일한 유형의 객체와 의미가 있는 내장 유형 모두에서 작동하도록 하는 것이 좋습니다. 이것이 비교 메서드가 `MutInt` 객체와 일반 정수를 모두 처리하는 이유입니다. 이렇게 하면 `MutInt` 클래스를 다양한 프로그래밍 시나리오에서 더 유연하게 사용할 수 있습니다.
