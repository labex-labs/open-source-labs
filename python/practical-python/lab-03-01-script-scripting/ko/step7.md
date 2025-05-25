# 하향식 스타일

함수는 구성 요소 (building block) 로 취급됩니다. 더 작고/단순한 블록이 먼저 옵니다.

```python
# myprogram.py
def foo(x):
    ...

def bar(x):
    ...
    foo(x)          # Defined above
    ...

def spam(x):
    ...
    bar(x)          # Defined above
    ...

spam(42)            # Code that uses the functions appears at the end
```

나중에 정의된 함수는 이전에 정의된 함수를 기반으로 합니다. 다시 말하지만, 이것은 단지 스타일의 문제입니다. 위의 프로그램에서 중요한 유일한 것은 `spam(42)`에 대한 호출이 마지막에 나타나는 것입니다.
