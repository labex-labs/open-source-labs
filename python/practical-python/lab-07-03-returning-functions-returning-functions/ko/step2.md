# 지역 변수 (Local Variables)

내부 함수가 외부 함수에 의해 정의된 변수를 어떻게 참조하는지 살펴보십시오.

```python
def add(x, y):
    def do_add():
        # `x` 와 `y` 는 `add(x, y)` 위에 정의되어 있습니다.
        print('Adding', x, y)
        return x + y
    return do_add
```

또한, `add()`가 종료된 후에도 해당 변수가 어떻게든 유지되는지 관찰하십시오.

```python
>>> a = add(3,4)
>>> a
<function do_add at 0x6a670>
>>> a()
Adding 3 4      # 이 값들은 어디에서 오는 걸까요?
7
```
