# 클로저 (Closures)

내부 함수가 결과로 반환될 때, 해당 내부 함수를 _클로저 (closure)_ 라고 합니다.

```python
def add(x, y):
    # `do_add` 는 클로저입니다.
    def do_add():
        print('Adding', x, y)
        return x + y
    return do_add
```

_핵심 기능: 클로저는 나중에 함수가 제대로 실행되는 데 필요한 모든 변수의 값을 유지합니다._ 클로저를 함수와, 함수가 의존하는 변수의 값을 담고 있는 추가적인 환경으로 생각할 수 있습니다.
