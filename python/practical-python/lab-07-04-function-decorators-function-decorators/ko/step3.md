# 로깅을 만드는 코드

아마도 로깅이 추가된 함수를 만드는 함수를 만들 수 있을 것입니다. 래퍼 (wrapper) 입니다.

```python
def logged(func):
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

이제 사용해 봅시다.

```python
def add(x, y):
    return x + y

logged_add = logged(add)
```

`logged`에 의해 반환된 함수를 호출하면 어떻게 될까요?

```python
logged_add(3, 4)      # You see the logging message appear
```

이 예제는 소위 *래퍼 함수*를 생성하는 과정을 보여줍니다.

래퍼는 다른 함수를 감싸서 추가적인 처리를 수행하지만, 그렇지 않으면 원래 함수와 정확히 동일한 방식으로 작동하는 함수입니다.

```python
>>> logged_add(3, 4)
Calling add   # Extra output. Added by the wrapper
7
>>>
```

_참고: `logged()` 함수는 래퍼를 생성하고 결과를 반환합니다._
