# 지연된 함수 실행

함수 `delay(fn, ms, *args)`를 작성하세요. 이 함수는 함수 `fn`, 밀리초 단위의 시간 `ms`, 그리고 임의의 개수의 인자 `args`를 받습니다. 이 함수는 `fn`의 실행을 `ms` 밀리초 동안 지연시킨 다음, 제공된 인자를 사용하여 호출해야 합니다. 이 함수는 `fn`을 호출한 결과를 반환해야 합니다.

`fn`의 실행을 지연시키기 위해 `time.sleep()` 함수를 사용하세요. 이 함수는 초 단위의 숫자를 인자로 받으므로, `time.sleep()`에 전달하기 전에 `ms`를 초 단위로 변환해야 합니다.

```python
from time import sleep

def delay(fn, ms, *args):
  sleep(ms / 1000)
  return fn(*args)
```

```python
delay(lambda x: print(x), 1000, 'later') # prints 'later' after one second
```
