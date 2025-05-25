# 예외 포착 및 처리 (Catching and Handling Exceptions)

예외는 포착하고 처리할 수 있습니다.

포착하려면 `try - except` 문을 사용하십시오.

```python
for line in file:
    fields = line.split(',')
    try:
        shares = int(fields[1])
    except ValueError:
        print("Couldn't parse", line)
    ...
```

`ValueError`의 이름은 포착하려는 오류의 종류와 일치해야 합니다.

수행되는 작업에 따라 어떤 종류의 오류가 발생할 수 있는지 미리 정확히 아는 것은 종종 어렵습니다. 좋든 싫든, 예외 처리는 종종 프로그램이 예기치 않게 충돌한 *후*에 추가됩니다 (예: "아, 그 오류를 포착하는 것을 잊었네. 그걸 처리해야 해!").
