# 데코레이터 (Decorators)

함수 주위에 래퍼를 사용하는 것은 Python 에서 매우 흔합니다. 너무 흔해서, 이를 위한 특별한 구문이 있습니다.

```python
def add(x, y):
    return x + y
add = logged(add)

# Special syntax
@logged
def add(x, y):
    return x + y
```

특별한 구문은 위에서 보여준 것과 정확히 동일한 단계를 수행합니다. 데코레이터는 단지 새로운 구문일 뿐입니다. 함수를 *데코레이트 (decorate)*한다고 말합니다.
