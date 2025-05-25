# 예외 다시 살펴보기

연습 문제에서 다음과 같은 `parse()` 함수를 작성했습니다.

```python
# fileparse.py
def parse(f, types=None, names=None, delimiter=None):
    records = []
    for line in f:
        line = line.strip()
        if not line: continue
        try:
            records.append(split(line,types,names,delimiter))
        except ValueError as e:
            print("Couldn't parse :", line)
            print("Reason :", e)
    return records
```

`try-except` 문에 집중해 봅시다. `except` 블록에서 무엇을 해야 할까요?

경고 메시지를 출력해야 할까요?

```python
try:
    records.append(split(line,types,names,delimiter))
except ValueError as e:
    print("Couldn't parse :", line)
    print("Reason :", e)
```

아니면 조용히 무시해야 할까요?

```python
try:
    records.append(split(line,types,names,delimiter))
except ValueError as e:
    pass
```

두 가지 해결책 모두 만족스럽지 않습니다. 왜냐하면 종종 _두 가지_ 동작 (사용자가 선택 가능) 을 모두 원하기 때문입니다.
