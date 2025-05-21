# 스택 프레임 검사 탐구

우리가 사용해 온 `_init(locals())` 접근 방식은 기능적이지만 단점이 있습니다. `__init__` 메서드를 정의할 때마다 `locals()`를 명시적으로 호출해야 합니다. 이는 특히 여러 클래스를 처리할 때 다소 번거로워질 수 있습니다. 다행히 스택 프레임 검사를 사용하여 코드를 더 깔끔하고 효율적으로 만들 수 있습니다. 이 기술을 사용하면 `locals()`를 명시적으로 호출하지 않고도 호출자의 지역 변수에 자동으로 접근할 수 있습니다.

Python 인터프리터에서 이 기술을 탐구해 보겠습니다. 먼저 터미널을 열고 프로젝트 디렉토리로 이동합니다. 그런 다음 Python 인터프리터를 시작합니다. 다음 명령을 실행하여 이 작업을 수행할 수 있습니다.

```bash
cd ~/project
python3
```

이제 Python 인터프리터에 들어왔으므로 `sys` 모듈을 가져와야 합니다. `sys` 모듈은 Python 인터프리터에서 사용하거나 유지 관리하는 일부 변수에 대한 접근을 제공합니다. 스택 프레임 정보를 접근하는 데 사용합니다.

```python
import sys
```

다음으로, 개선된 버전의 `_init()` 함수를 정의합니다. 이 새 버전은 호출자의 프레임에 직접 접근하여 `locals()`를 명시적으로 전달할 필요가 없도록 합니다.

```python
def _init():
    # Get the caller's frame (1 level up in the call stack)
    frame = sys._getframe(1)

    # Get the local variables from that frame
    locs = frame.f_locals

    # Extract self and set other variables as attributes
    self = locs.pop('self')
    for name, val in locs.items():
        setattr(self, name, val)
```

이 코드에서 `sys._getframe(1)`은 호출 함수에 해당하는 프레임 객체를 검색합니다. 인수로 `1`은 호출 스택에서 한 단계 위를 의미합니다. 프레임 객체가 있으면 `frame.f_locals`를 사용하여 해당 지역 변수에 접근할 수 있습니다. 이렇게 하면 호출자의 스코프에 있는 모든 지역 변수의 딕셔너리가 제공됩니다. 그런 다음 `self` 변수를 추출하고 나머지 변수를 `self` 객체의 속성으로 설정합니다.

이제 이 새로운 `_init()` 함수를 새로운 버전의 `Stock` 클래스로 테스트해 보겠습니다.

```python
class Stock:
    def __init__(self, name, shares, price):
        _init()  # No need to pass locals() anymore!

# Test it
s = Stock('GOOG', 100, 490.1)
print(s.name, s.shares, s.price)

# Also works with keyword arguments
s = Stock(name='AAPL', shares=50, price=125.3)
print(s.name, s.shares, s.price)
```

보시다시피, `__init__` 메서드는 더 이상 `locals()`를 명시적으로 전달할 필요가 없습니다. 이렇게 하면 호출자의 관점에서 코드가 더 깔끔하고 읽기 쉬워집니다.

### 스택 프레임 검사 작동 방식

`sys._getframe(1)`을 호출하면 Python 은 호출자의 실행 프레임을 나타내는 프레임 객체를 반환합니다. 인수 `1`은 "현재 프레임에서 한 단계 위"(호출 함수) 를 의미합니다.

프레임 객체에는 실행 컨텍스트에 대한 중요한 정보가 포함되어 있습니다. 여기에는 현재 실행 중인 함수, 해당 함수의 지역 변수 및 현재 실행 중인 줄 번호가 포함됩니다.

`frame.f_locals`에 접근하면 호출자의 스코프에 있는 모든 지역 변수의 딕셔너리를 얻습니다. 이는 해당 스코프에서 직접 호출된 경우 `locals()`가 반환하는 것과 유사합니다.

이 기술은 매우 강력하지만 주의해서 사용해야 합니다. 일반적으로 고급 Python 기능으로 간주되며 Python 의 일반적인 스코프 경계를 벗어나기 때문에 다소 "마법적"으로 보일 수 있습니다.

스택 프레임 검사를 실험한 후 다음 명령을 실행하여 Python 인터프리터를 종료할 수 있습니다.

```python
exit()
```
