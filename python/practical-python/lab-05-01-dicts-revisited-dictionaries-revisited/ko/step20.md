# 연습 문제 5.3: 클래스의 역할

클래스 정의를 구성하는 정의는 해당 클래스의 모든 인스턴스에서 공유됩니다. 모든 인스턴스가 관련 클래스로 다시 연결되어 있음을 확인하십시오.

```python
>>> goog.__class__
... look at output ...
>>> ibm.__class__
... look at output ...
>>>
```

인스턴스에서 메서드를 호출해 보십시오.

```python
>>> goog.cost()
49010.0
>>> ibm.cost()
4561.5
>>>
```

`goog.__dict__` 또는 `ibm.__dict__`에 'cost'라는 이름이 정의되어 있지 않음을 확인하십시오. 대신, 클래스 딕셔너리에서 제공됩니다. 다음을 시도해 보십시오.

```python
>>> Stock.__dict__['cost']
... look at output ...
>>>
```

딕셔너리를 통해 `cost()` 메서드를 직접 호출해 보십시오.

```python
>>> Stock.__dict__['cost'](goog)
49010.0
>>> Stock.__dict__['cost'](ibm)
4561.5
>>>
```

클래스 정의에서 정의된 함수를 어떻게 호출하고 `self` 인수가 인스턴스를 얻는지 확인하십시오.

`Stock` 클래스에 새 속성을 추가해 보십시오.

```python
>>> Stock.foo = 42
>>>
```

이 새 속성이 이제 모든 인스턴스에 표시되는 방식을 확인하십시오.

```python
>>> goog.foo
42
>>> ibm.foo
42
>>>
```

그러나 인스턴스 딕셔너리의 일부가 아님을 확인하십시오.

```python
>>> goog.__dict__
... look at output and notice there is no 'foo' attribute ...
>>>
```

인스턴스 자체에서 찾을 수 없는 경우 Python 이 항상 클래스 딕셔너리를 확인하기 때문에 인스턴스에서 `foo` 속성에 액세스할 수 있습니다.

참고: 이 연습 부분은 클래스 변수라고 하는 것을 보여줍니다. 예를 들어, 다음과 같은 클래스가 있다고 가정해 보십시오.

```python
class Foo(object):
     a = 13                  # Class variable
     def __init__(self,b):
         self.b = b          # Instance variable
```

이 클래스에서 클래스 자체의 본문에서 할당된 변수 `a`는 "클래스 변수"입니다. 생성되는 모든 인스턴스에서 공유됩니다. 예를 들어:

```python
>>> f = Foo(10)
>>> g = Foo(20)
>>> f.a          # Inspect the class variable (same for both instances)
13
>>> g.a
13
>>> f.b          # Inspect the instance variable (differs)
10
>>> g.b
20
>>> Foo.a = 42   # Change the value of the class variable
>>> f.a
42
>>> g.a
42
>>>
```
