# continue 문 (continue statement)

하나의 요소를 건너뛰고 다음 요소로 이동하려면 `continue` 문을 사용하십시오.

```python
for line in lines:
    if line == '\n':    # Skip blank lines
        continue
    # More statements
    ...
```

이는 현재 항목이 관심 대상이 아니거나 처리 과정에서 무시해야 할 때 유용합니다.
