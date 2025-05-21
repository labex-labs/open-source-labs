# 속성 이름 제한하기

현재 `Structure` 클래스는 인스턴스에 모든 속성을 설정할 수 있습니다. 초보자에게는 처음에는 편리해 보일 수 있지만, 실제로 많은 문제를 야기할 수 있습니다. 클래스를 사용할 때는 특정 속성이 존재하고 특정 방식으로 사용될 것으로 예상합니다. 사용자가 속성 이름을 잘못 입력하거나 원래 설계에 포함되지 않은 속성을 설정하려고 하면 찾기 어려운 오류가 발생할 수 있습니다.

## 속성 제한의 필요성

속성 이름을 제한해야 하는 이유를 이해하기 위해 간단한 시나리오를 살펴보겠습니다. 다음 코드를 고려하십시오.

```python
s = Stock('GOOG', 100, 490.1)
s.shares = 50      # 올바른 속성 이름
s.share = 60       # 속성 이름의 오타 - 업데이트 대신 새 속성 생성
```

두 번째 줄에 오타가 있습니다. `shares` 대신 `share`를 작성했습니다. Python 에서는 오류를 발생시키는 대신 `share`라는 새 속성을 생성합니다. 이는 `shares` 속성을 업데이트하고 있다고 생각하지만 실제로 새 속성을 생성하고 있을 수 있으므로 미묘한 버그로 이어질 수 있습니다. 이로 인해 코드가 예기치 않게 동작하고 디버깅하기가 매우 어려울 수 있습니다.

## 속성 제한 구현하기

이 문제를 해결하기 위해 `__setattr__` 메서드를 재정의할 수 있습니다. 이 메서드는 객체에 속성을 설정하려고 할 때마다 호출됩니다. 이를 재정의하여 어떤 속성을 설정할 수 있고 어떤 속성을 설정할 수 없는지 제어할 수 있습니다.

`structure.py`의 `Structure` 클래스를 다음 코드로 업데이트하십시오.

```python
def __setattr__(self, name, value):
    """
    속성 설정을 _fields 에 정의된 속성 또는 밑줄로 시작하는 속성 (private 속성) 으로 제한합니다.
    """
    if name.startswith('_'):
        # private 속성 설정 허용 (_로 시작)
        super().__setattr__(name, value)
    elif name in self._fields:
        # _fields 에 정의된 속성 설정 허용
        super().__setattr__(name, value)
    else:
        # 다른 속성에 대해 오류 발생
        raise AttributeError(f'No attribute {name}')
```

이 메서드의 작동 방식은 다음과 같습니다.

1.  속성 이름이 밑줄 (`_`) 로 시작하는 경우, 이는 private 속성으로 간주됩니다. Private 속성은 종종 클래스 내부적인 목적으로 사용됩니다. 이러한 속성은 클래스의 내부 구현의 일부이므로 설정하도록 허용합니다.
2.  속성 이름이 `_fields` 목록에 있는 경우, 이는 클래스 설계에 정의된 속성 중 하나임을 의미합니다. 이러한 속성은 클래스의 예상된 동작의 일부이므로 설정하도록 허용합니다.
3.  속성 이름이 이러한 조건 중 어느 것도 충족하지 않는 경우, `AttributeError`를 발생시킵니다. 이는 사용자에게 클래스에 존재하지 않는 속성을 설정하려고 한다는 것을 알려줍니다.

## 속성 제한 테스트하기

이제 속성 제한을 구현했으므로 예상대로 작동하는지 테스트해 보겠습니다. 다음 코드로 `test_attributes.py`라는 파일을 만듭니다.

```python
# test_attributes.py
from structure import Stock

s = Stock('GOOG', 100, 490.1)

# 이것은 작동해야 합니다 - 유효한 속성
print("Setting shares to 50")
s.shares = 50
print(f"Shares is now: {s.shares}")

# 이것은 작동해야 합니다 - private 속성
print("\nSetting _internal_data")
s._internal_data = "Some data"
print(f"_internal_data is: {s._internal_data}")

# 이것은 실패해야 합니다 - 유효하지 않은 속성
print("\nTrying to set an invalid attribute:")
try:
    s.share = 60  # 속성 이름의 오타
    print("This should not print")
except AttributeError as e:
    print(f"Error correctly caught: {e}")
```

테스트를 실행하려면 터미널을 열고 다음 명령을 입력합니다.

```bash
python3 test_attributes.py
```

다음 출력이 표시되어야 합니다.

```
Setting shares to 50
Shares is now: 50

Setting _internal_data
_internal_data is: Some data

Trying to set an invalid attribute:
Error correctly caught: No attribute share
```

이 출력은 이제 클래스가 우발적인 속성 오류를 방지함을 보여줍니다. 유효한 속성과 private 속성을 설정할 수 있지만, 유효하지 않은 속성을 설정하려고 하면 오류가 발생합니다.

## 속성 제한의 가치

속성 이름 제한은 견고하고 유지 관리 가능한 코드를 작성하는 데 매우 중요합니다. 그 이유는 다음과 같습니다.

1.  속성 이름의 오타를 잡는 데 도움이 됩니다. 속성 이름을 입력할 때 실수를 하면 새 속성을 생성하는 대신 코드가 오류를 발생시킵니다. 이렇게 하면 개발 프로세스 초기에 오류를 찾고 수정하기가 더 쉬워집니다.
2.  클래스 설계에 존재하지 않는 속성을 설정하려는 시도를 방지합니다. 이렇게 하면 클래스가 의도한 대로 사용되고 코드가 예측 가능하게 동작하도록 보장합니다.
3.  새로운 속성의 우발적인 생성을 방지합니다. 새로운 속성을 생성하면 예기치 않은 동작이 발생하고 코드를 이해하고 유지 관리하기가 더 어려워질 수 있습니다.

속성 이름을 제한함으로써 코드를 더 신뢰할 수 있고 사용하기 쉽게 만듭니다.
