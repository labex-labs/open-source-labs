# 메타클래스 상속 탐구

메타클래스는 매력적인 특징을 가지고 있습니다. 바로 "고착성 (sticky)"입니다. 이는 클래스가 메타클래스를 사용하면 상속 계층 구조의 모든 하위 클래스도 동일한 메타클래스를 사용한다는 의미입니다. 즉, 메타클래스 속성은 상속 체인을 통해 전파됩니다.

이를 실제로 살펴보겠습니다.

1. 먼저 `mymeta.py` 파일을 엽니다. 이 파일의 끝에 새 클래스를 추가할 것입니다. `MyStock`이라는 이 클래스는 `Stock` 클래스에서 상속받습니다. `__init__` 메서드는 객체의 속성을 초기화하는 데 사용되며, 공통 속성을 초기화하기 위해 `super().__init__`을 사용하여 상위 클래스의 `__init__` 메서드를 호출합니다. `info` 메서드는 주식에 대한 정보가 포함된 형식이 지정된 문자열을 반환하는 데 사용됩니다. 다음 코드를 추가합니다.

```python
class MyStock(Stock):
    def __init__(self, name, shares, price, category):
        super().__init__(name, shares, price)
        self.category = category

    def info(self):
        return f"{self.name} ({self.category}): {self.shares} shares at ${self.price}"
```

2. 코드를 추가한 후 `mymeta.py` 파일을 저장합니다. 파일을 저장하면 변경 사항이 저장되어 나중에 사용할 수 있습니다.

3. 이제 메타클래스의 상속 동작을 테스트하기 위해 `test_inheritance.py`라는 새 파일을 만들 것입니다. 이 파일에서 `mymeta.py` 파일에서 `MyStock` 클래스를 가져옵니다. 그런 다음 `MyStock` 클래스의 인스턴스를 생성하고, 해당 메서드를 호출하고, 결과를 출력하여 메타클래스가 상속을 통해 어떻게 작동하는지 확인합니다. `test_inheritance.py`에 다음 코드를 추가합니다.

```python
# test_inheritance.py
from mymeta import MyStock

# Create a MyStock instance
tech_stock = MyStock("MSFT", 50, 305.75, "Technology")

# Test the methods
print(tech_stock.info())
print(f"Total cost: ${tech_stock.cost()}")

# Sell some shares
tech_stock.sell(5)
print(f"After selling: {tech_stock.shares} shares remaining")
print(f"Updated cost: ${tech_stock.cost()}")
```

4. 마지막으로 `test_inheritance.py` 파일을 실행하여 상속을 통해 메타클래스가 작동하는 것을 확인합니다. 터미널을 열고 `test_inheritance.py` 파일이 있는 디렉토리로 이동하여 다음 명령을 실행합니다.

```bash
python3 test_inheritance.py
```

다음과 유사한 출력을 볼 수 있습니다.

```
Creating class : myobject
Base classes   : ()
Attributes     : ['__module__', '__qualname__', '__doc__']
Creating class : Stock
Base classes   : (<class 'mymeta.myobject'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'cost', 'sell', '__doc__']
Creating class : MyStock
Base classes   : (<class 'mymeta.Stock'>,)
Attributes     : ['__module__', '__qualname__', '__init__', 'info', '__doc__']
MSFT (Technology): 50 shares at $305.75
Total cost: $15287.5
After selling: 45 shares remaining
Updated cost: $13758.75
```

`MyStock` 클래스에 대해 명시적으로 메타클래스를 지정하지 않았음에도 메타클래스가 여전히 적용되는 것을 확인하십시오. 이는 메타클래스가 상속을 통해 어떻게 전파되는지 명확하게 보여줍니다.

## 메타클래스의 실용적인 사용

이 예제에서 메타클래스는 단순히 클래스에 대한 정보를 출력합니다. 그러나 메타클래스는 실제 프로그래밍에서 많은 실용적인 응용 프로그램을 가지고 있습니다.

1. **유효성 검사 (Validation)**: 메타클래스를 사용하여 클래스에 필요한 메서드 또는 속성이 있는지 확인할 수 있습니다. 이를 통해 클래스가 사용되기 전에 특정 기준을 충족하는지 확인할 수 있습니다.
2. **등록 (Registration)**: 메타클래스는 클래스를 레지스트리에 자동으로 등록할 수 있습니다. 이는 특정 유형의 모든 클래스를 추적해야 할 때 유용합니다.
3. **인터페이스 강제 (Interface enforcement)**: 클래스가 필요한 인터페이스를 구현하도록 하는 데 사용할 수 있습니다. 이는 코드에서 일관된 구조를 유지하는 데 도움이 됩니다.
4. **관점 지향 프로그래밍 (Aspect-oriented programming)**: 메타클래스는 메서드에 동작을 추가할 수 있습니다. 예를 들어, 메서드 코드를 직접 수정하지 않고도 메서드에 로깅 또는 성능 모니터링을 추가할 수 있습니다.
5. **ORM 시스템 (ORM systems)**: Django 또는 SQLAlchemy 와 같은 객체 관계 매핑 (ORM) 시스템에서 메타클래스는 클래스를 데이터베이스 테이블에 매핑하는 데 사용됩니다. 이는 애플리케이션에서 데이터베이스 작업을 단순화합니다.

메타클래스는 매우 강력하지만 신중하게 사용해야 합니다. Tim Peters(Python 의 Zen 으로 유명함) 가 말했듯이, "메타클래스는 99% 의 사용자가 걱정해야 할 것보다 더 심오한 마법입니다."
