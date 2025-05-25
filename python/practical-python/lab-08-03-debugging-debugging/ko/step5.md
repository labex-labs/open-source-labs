# Python 디버거

프로그램 내에서 수동으로 디버거를 실행할 수 있습니다.

```python
def some_function():
    ...
    breakpoint()      # Enter the debugger (Python 3.7+)
    ...
```

이것은 `breakpoint()` 호출에서 디버거를 시작합니다.

이전 Python 버전에서는 다음과 같이 했습니다. 다른 디버깅 가이드에서 이 내용을 언급하는 것을 볼 수 있습니다.

```python
import pdb
...
pdb.set_trace()       # Instead of `breakpoint()`
...
```
