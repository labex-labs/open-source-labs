# 인자 전달 (Argument Passing)

함수를 호출할 때, 인자 변수는 전달된 값을 참조하는 이름입니다. 이러한 값은 복사본이 아닙니다. 가변 데이터 타입 (예: 리스트, 딕셔너리) 이 전달되면, _제자리에서_ 수정될 수 있습니다.

```python
def foo(items):
    items.append(42)    # Modifies the input object

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]
```

**핵심 사항: 함수는 입력 인자의 복사본을 받지 않습니다.**
