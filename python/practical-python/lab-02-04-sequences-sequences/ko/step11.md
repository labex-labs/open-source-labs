# zip() 함수

`zip` 함수는 여러 시퀀스를 받아 결합하는 이터레이터 (iterator) 를 만듭니다.

```python
columns = ['name', 'shares', 'price']
values = ['GOOG', 100, 490.1 ]
pairs = zip(columns, values)
# ('name','GOOG'), ('shares',100), ('price',490.1)
```

결과를 얻으려면 반복해야 합니다. 앞서 보여드린 것처럼 여러 변수를 사용하여 튜플을 언팩 (unpack) 할 수 있습니다.

```python
for column, value in pairs:
    ...
```

`zip`의 일반적인 사용법은 딕셔너리를 구성하기 위한 키/값 쌍을 만드는 것입니다.

```python
d = dict(zip(columns, values))
```
