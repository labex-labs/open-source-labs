# 몇 가지 주의사항

다중 상속은 강력한 도구입니다. 힘에는 책임이 따른다는 것을 기억하십시오. 프레임워크/라이브러리는 구성 요소의 조합과 관련된 고급 기능을 위해 때때로 이를 사용합니다. 이제 그것을 봤다는 것을 잊으십시오.

4 절에서 주식 보유를 나타내는 `Stock` 클래스를 정의했습니다. 이 연습에서는 해당 클래스를 사용합니다. 인터프리터를 다시 시작하고 몇 가지 인스턴스를 만듭니다.

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> goog = Stock('GOOG',100,490.10)
>>> ibm  = Stock('IBM',50, 91.23)
>>>
```
