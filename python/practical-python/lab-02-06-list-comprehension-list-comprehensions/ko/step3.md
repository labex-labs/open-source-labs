# 사용 사례

리스트 컴프리헨션은 매우 유용합니다. 예를 들어, 특정 딕셔너리 필드의 값을 수집할 수 있습니다.

```python
stocknames = [s['name'] for s in stocks]
```

시퀀스에 대해 데이터베이스와 유사한 쿼리를 수행할 수 있습니다.

```python
a = [s for s in stocks if s['price'] > 100 and s['shares'] > 50 ]
```

또한 리스트 컴프리헨션과 시퀀스 축약을 결합할 수 있습니다.

```python
cost = sum([s['shares']*s['price'] for s in stocks])
```
