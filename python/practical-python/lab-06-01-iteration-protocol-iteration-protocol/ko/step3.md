# 반복 지원 (Supporting Iteration)

반복에 대해 아는 것은 자신의 객체에 반복을 추가하려는 경우 유용합니다. 예를 들어, 사용자 정의 컨테이너를 만드는 경우입니다.

```python
class Portfolio:
    def __init__(self):
        self.holdings = []

    def __iter__(self):
        return self.holdings.__iter__()
    ...

port = Portfolio()
for s in port:
    ...
```
