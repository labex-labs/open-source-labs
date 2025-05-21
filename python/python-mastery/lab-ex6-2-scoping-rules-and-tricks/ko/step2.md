# locals() 를 사용하여 함수 인수 접근하기

Python 에서 변수 스코프를 이해하는 것은 매우 중요합니다. 변수의 스코프는 코드 내에서 해당 변수에 접근할 수 있는 위치를 결정합니다. Python 은 스코핑을 이해하는 데 매우 유용한 `locals()`라는 내장 함수를 제공합니다. `locals()` 함수는 현재 스코프의 모든 지역 변수를 포함하는 딕셔너리를 반환합니다. 이는 함수 인수를 검사하려는 경우, 코드의 특정 부분 내에서 어떤 변수를 사용할 수 있는지 명확하게 보여주므로 매우 유용할 수 있습니다.

이것이 어떻게 작동하는지 확인하기 위해 Python 인터프리터에서 간단한 실험을 해보겠습니다. 먼저, 프로젝트 디렉토리로 이동하여 Python 인터프리터를 시작해야 합니다. 터미널에서 다음 명령을 실행하여 이 작업을 수행할 수 있습니다.

```bash
cd ~/project
python3
```

Python 대화형 셸에 들어가면 `Stock` 클래스를 정의합니다. Python 에서 클래스는 객체를 생성하기 위한 청사진과 같습니다. 이 클래스에서는 특수 `__init__` 메서드를 사용합니다. `__init__` 메서드는 Python 의 생성자이며, 클래스의 객체가 생성될 때 자동으로 호출됩니다. 이 `__init__` 메서드 내에서 `locals()` 함수를 사용하여 모든 지역 변수를 출력합니다.

```python
class Stock:
    def __init__(self, name, shares, price):
        print(locals())
```

이제 이 `Stock` 클래스의 인스턴스를 생성해 보겠습니다. 인스턴스는 클래스 청사진에서 생성된 실제 객체입니다. `name`, `shares`, `price` 매개변수에 대한 값을 전달합니다.

```python
s = Stock('GOOG', 100, 490.1)
```

이 코드를 실행하면 다음과 유사한 출력이 표시됩니다.

```
{'self': <__main__.Stock object at 0x...>, 'name': 'GOOG', 'shares': 100, 'price': 490.1}
```

이 출력은 `locals()`가 `__init__` 메서드의 모든 지역 변수를 포함하는 딕셔너리를 제공한다는 것을 보여줍니다. `self` 참조는 클래스 자체의 인스턴스를 참조하는 Python 클래스의 특수 변수입니다. 다른 변수는 `Stock` 객체를 생성할 때 전달한 매개변수 값입니다.

이 `locals()` 기능을 사용하여 객체 속성을 자동으로 초기화할 수 있습니다. 속성은 객체와 관련된 변수입니다. 헬퍼 함수를 정의하고 `Stock` 클래스를 수정해 보겠습니다.

```python
def _init(locs):
    self = locs.pop('self')
    for name, val in locs.items():
        setattr(self, name, val)

class Stock:
    def __init__(self, name, shares, price):
        _init(locals())
```

`_init` 함수는 `locals()`에서 얻은 지역 변수의 딕셔너리를 사용합니다. 먼저 `pop` 메서드를 사용하여 딕셔너리에서 `self` 참조를 제거합니다. 그런 다음 딕셔너리의 나머지 키 - 값 쌍을 반복하고 `setattr` 함수를 사용하여 각 변수를 객체의 속성으로 설정합니다.

이제 위치 인수와 키워드 인수를 모두 사용하여 이 구현을 테스트해 보겠습니다. 위치 인수는 함수 시그니처에 정의된 순서대로 전달되는 반면, 키워드 인수는 매개변수 이름과 함께 전달됩니다.

```python
# Test with positional arguments
s1 = Stock('GOOG', 100, 490.1)
print(s1.name, s1.shares, s1.price)

# Test with keyword arguments
s2 = Stock(name='AAPL', shares=50, price=125.3)
print(s2.name, s2.shares, s2.price)
```

이제 두 가지 방법 모두 작동해야 합니다! `_init` 함수를 사용하면 위치 인수와 키워드 인수를 원활하게 처리할 수 있습니다. 또한 함수 시그니처에서 매개변수 이름을 유지하므로 `help()` 출력의 유용성이 향상됩니다. Python 의 `help()` 함수는 함수, 클래스 및 모듈에 대한 정보를 제공하며, 매개변수 이름을 그대로 유지하면 이 정보가 더 의미 있게 됩니다.

실험을 마쳤으면 다음 명령을 실행하여 Python 인터프리터를 종료할 수 있습니다.

```python
exit()
```
