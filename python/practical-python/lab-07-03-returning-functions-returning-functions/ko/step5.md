# 지연 평가 (Delayed Evaluation)

다음과 같은 함수를 생각해 봅시다:

```python
def after(seconds, func):
    import time
    time.sleep(seconds)
    func()
```

사용 예시:

```python
def greeting():
    print('Hello Guido')

after(30, greeting)
```

`after` 함수는 제공된 함수를 나중에 실행합니다.

클로저는 추가 정보를 함께 전달합니다.

```python
def add(x, y):
    def do_add():
        print(f'Adding {x} + {y} -> {x+y}')
    return do_add

def after(seconds, func):
    import time
    time.sleep(seconds)
    func()

after(30, add(2, 3))
# `do_add` 는 x -> 2 및 y -> 3 의 참조를 가지고 있습니다.
```
