# 문자열 표현 개선

Python 에서 `MutInt` 객체를 인쇄하면 `<__main__.MutInt object at 0x...>`와 같은 출력을 보게 됩니다. 이 출력은 `MutInt` 객체의 실제 값을 알려주지 않으므로 그다지 유용하지 않습니다. 객체가 나타내는 것을 더 쉽게 이해하기 위해 문자열 표현을 위한 특수 메서드를 구현할 것입니다.

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
```

`MutInt` 클래스에 세 가지 중요한 메서드를 추가했습니다.

- `__str__()`: 이 메서드는 객체에 `str()` 함수를 사용하거나 객체를 직접 인쇄할 때 호출됩니다. 사람이 읽을 수 있는 문자열을 반환해야 합니다.
- `__repr__()`: 이 메서드는 객체의 "공식적인" 문자열 표현을 제공합니다. 주로 디버깅에 사용되며, 이상적으로는 `eval()` 함수에 전달하면 객체를 다시 생성하는 문자열을 반환해야 합니다.
- `__format__()`: 이 메서드를 사용하면 `MutInt` 객체와 함께 Python 의 문자열 형식 시스템을 사용할 수 있습니다. 패딩 및 숫자 형식 지정과 같은 형식 사양을 사용할 수 있습니다.

2. 이러한 새 메서드를 테스트하기 위해 `test_string_repr.py`라는 새 테스트 파일을 생성합니다.

```python
# test_string_repr.py

from mutint import MutInt

# MutInt 객체 생성
a = MutInt(3)

# 문자열 표현 테스트
print(f"str(a): {str(a)}")
print(f"repr(a): {repr(a)}")

# 직접 인쇄 테스트
print(f"Print a: {a}")

# 문자열 형식 지정 테스트
print(f"Formatted with padding: '{a:*^10}'")
print(f"Formatted as decimal: '{a:d}'")

# 가변성 테스트
a.value = 42
print(f"After changing value, repr(a): {repr(a)}")
```

이 테스트 파일에서는 먼저 `MutInt` 클래스를 가져옵니다. 그런 다음 값 `3`으로 `MutInt` 객체를 생성합니다. `str()` 및 `repr()` 함수를 사용하여 `__str__()` 및 `__repr__()` 메서드를 테스트합니다. 또한 직접 인쇄, 문자열 형식 지정 및 `MutInt` 객체의 가변성을 테스트합니다.

3. 테스트 스크립트를 실행합니다.

```bash
python3 /home/labex/project/test_string_repr.py
```

이 명령을 실행하면 Python 은 `test_string_repr.py` 스크립트를 실행합니다. 다음과 유사한 출력을 볼 수 있습니다.

```
str(a): 3
repr(a): MutInt(3)
Print a: 3
Formatted with padding: '****3*****'
Formatted as decimal: '3'
After changing value, repr(a): MutInt(42)
```

이제 `MutInt` 객체가 보기 좋게 표시됩니다. 문자열 표현은 기본 값을 보여주며, 일반 정수와 마찬가지로 문자열 형식을 사용할 수 있습니다.

`__str__()`과 `__repr__()`의 차이점은 `__str__()`은 사람이 이해하기 쉬운 출력을 생성하기 위한 것이고, `__repr__()`은 이상적으로 `eval()`에 전달하면 객체를 다시 생성하는 문자열을 생성해야 한다는 것입니다. 이것이 `__repr__()` 메서드에 클래스 이름을 포함시킨 이유입니다.

`__format__()` 메서드를 사용하면 객체가 Python 의 형식 시스템과 함께 작동하므로 패딩 및 숫자 형식 지정과 같은 형식 사양을 사용할 수 있습니다.
