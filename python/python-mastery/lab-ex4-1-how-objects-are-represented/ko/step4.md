# 클래스와 인스턴스의 관계 이해

이제 Python 에서 클래스와 인스턴스가 어떻게 관련되어 있는지, 그리고 메서드 조회 (method lookup) 가 어떻게 작동하는지 살펴보겠습니다. 이는 Python 이 객체로 작업할 때 메서드와 속성을 어떻게 찾고 사용하는지 이해하는 데 도움이 되므로 중요한 개념입니다.

먼저, 인스턴스가 어떤 클래스에 속하는지 확인해 보겠습니다. 인스턴스의 클래스를 아는 것은 Python 이 해당 인스턴스와 관련된 메서드와 속성을 어디에서 찾을지 알려주므로 매우 중요합니다.

```python
>>> goog.__class__
<class '__main__.SimpleStock'>
>>> ibm.__class__
<class '__main__.SimpleStock'>
```

두 인스턴스 모두 `SimpleStock` 클래스를 참조합니다. 이 참조는 Python 이 메서드를 찾아야 할 때 사용하는 포인터와 같습니다. 인스턴스에서 메서드를 호출하면 Python 은 이 참조를 사용하여 적절한 메서드 정의를 찾습니다.

인스턴스에서 메서드를 호출하면 Python 은 다음 단계를 따릅니다.

1. 인스턴스의 `__dict__`에서 속성을 찾습니다. 인스턴스의 `__dict__`는 모든 인스턴스별 속성이 보관되는 저장 영역과 같습니다.
2. 찾을 수 없으면 클래스의 `__dict__`를 확인합니다. 클래스의 `__dict__`는 해당 클래스의 모든 인스턴스에 공통적인 모든 속성 및 메서드를 저장합니다.
3. 클래스에서 찾으면 해당 속성을 반환합니다.

이것을 실제로 살펴보겠습니다. 먼저, `cost` 메서드가 인스턴스 딕셔너리에 없는지 확인합니다. 이 단계는 `cost` 메서드가 각 인스턴스에 특정된 것이 아니라 클래스 수준에서 정의되었음을 이해하는 데 도움이 됩니다.

```python
>>> 'cost' in goog.__dict__
False
>>> 'cost' in ibm.__dict__
False
```

그렇다면 `cost` 메서드는 어디에서 오는 것일까요? 클래스를 확인해 보겠습니다. 클래스의 `__dict__`를 보면 `cost` 메서드가 어디에 정의되어 있는지 알 수 있습니다.

```python
>>> SimpleStock.__dict__['cost']
<function SimpleStock.cost at 0x7f...>
```

메서드는 인스턴스가 아닌 클래스에 정의되어 있습니다. `goog.cost()`를 호출하면 Python 은 `goog.__dict__`에서 `cost`를 찾지 못하므로 `SimpleStock.__dict__`를 찾아 거기에서 찾습니다.

실제로 클래스 딕셔너리에서 메서드를 직접 호출하여 인스턴스를 첫 번째 인수로 전달할 수 있습니다 (이것이 `self`가 됩니다). 이는 일반적인 instance.method() 구문을 사용할 때 Python 이 내부적으로 메서드를 호출하는 방식을 보여줍니다.

```python
>>> SimpleStock.__dict__['cost'](goog)
49010.0
>>> SimpleStock.__dict__['cost'](ibm)
4561.5
```

이것이 기본적으로 `goog.cost()`를 호출할 때 Python 이 내부적으로 수행하는 작업입니다.

이제 클래스 속성을 추가해 보겠습니다. 클래스 속성은 모든 인스턴스에서 공유됩니다. 즉, 클래스의 모든 인스턴스가 이 속성에 접근할 수 있으며 클래스 수준에서 한 번만 저장됩니다.

```python
>>> SimpleStock.exchange = 'NASDAQ'
>>> goog.exchange
'NASDAQ'
>>> ibm.exchange
'NASDAQ'
```

두 인스턴스 모두 `exchange` 속성에 접근할 수 있지만 개별 딕셔너리에는 저장되지 않습니다. 인스턴스 및 클래스 딕셔너리를 확인하여 이를 확인해 보겠습니다.

```python
>>> 'exchange' in goog.__dict__
False
>>> 'exchange' in SimpleStock.__dict__
True
>>> SimpleStock.__dict__['exchange']
'NASDAQ'
```

이는 다음을 보여줍니다.

1. 클래스 속성은 모든 인스턴스에서 공유됩니다. 모든 인스턴스는 자체 복사본 없이 동일한 클래스 속성에 접근할 수 있습니다.
2. Python 은 먼저 인스턴스 딕셔너리를 확인한 다음 클래스 딕셔너리를 확인합니다. 이는 인스턴스에서 속성에 접근하려고 할 때 Python 이 속성을 찾는 순서입니다.
3. 클래스는 공유 데이터 및 동작 (메서드) 의 저장소 역할을 합니다. 클래스는 모든 인스턴스에서 사용할 수 있는 모든 공통 속성 및 메서드를 저장합니다.

동일한 이름의 인스턴스 속성을 수정하면 클래스 속성이 가려집니다 (shadow). 즉, 해당 인스턴스에서 속성에 접근하면 Python 은 클래스 수준의 값 대신 인스턴스별 값을 사용합니다.

```python
>>> ibm.exchange = 'NYSE'
>>> ibm.exchange
'NYSE'
>>> goog.exchange  # Still using the class attribute
'NASDAQ'
>>> ibm.__dict__['exchange']
'NYSE'
```

이제 `ibm`은 클래스 속성을 가리는 자체 `exchange` 속성을 갖는 반면, `goog`는 여전히 클래스 속성을 사용합니다.
