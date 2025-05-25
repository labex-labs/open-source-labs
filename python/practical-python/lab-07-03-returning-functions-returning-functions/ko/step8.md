# 연습 문제 7.8: 함수 호출 간소화하기

위의 예에서, 사용자는 `typedproperty('shares', int)`와 같은 호출을 입력하는 것이 다소 장황하다고 느낄 수 있습니다. 특히 반복적으로 사용되는 경우 더욱 그렇습니다. `typedproperty.py` 파일에 다음 정의를 추가하세요:

```python
String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)
```

이제, 이러한 함수를 대신 사용하여 `Stock` 클래스를 다시 작성하세요:

```python
class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

아, 훨씬 낫네요. 여기서 핵심은 클로저와 `lambda`를 사용하여 코드를 간소화하고 성가신 반복을 제거할 수 있다는 것입니다. 이는 종종 좋은 일입니다.
