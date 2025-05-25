# 생산자 - 소비자 문제

제너레이터는 다양한 형태의 _생산자 - 소비자_(producer-consumer) 문제와 밀접하게 관련되어 있습니다.

```python
# Producer
def follow(f):
    ...
    while True:
        ...
        yield line        # Produces value in `line` below
        ...

# Consumer
for line in follow(f):    # Consumes value from `yield` above
    ...
```

`yield`는 `for`가 소비하는 값을 생성합니다.
