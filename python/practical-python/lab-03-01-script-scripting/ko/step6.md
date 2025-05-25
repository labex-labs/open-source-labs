# 함수 정의

함수는 어떤 순서로든 *정의 (define)*될 수 있습니다.

```python
def foo(x):
    bar(x)

def bar(x):
    statements

# OR
def bar(x):
    statements

def foo(x):
    bar(x)
```

함수는 프로그램 실행 중에 실제로 _사용 (use)_ (또는 호출 (call)) 되기 전에 정의되어야 합니다.

```python
foo(3)        # foo must be defined already
```

스타일적으로, 함수가 _하향식 (bottom-up)_ 방식으로 정의되는 것을 더 흔하게 볼 수 있습니다.
