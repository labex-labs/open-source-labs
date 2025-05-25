# 반복 (Looping)

`while` 문은 루프를 실행합니다.

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
```

`while` 뒤의 표현식이 `true`인 동안 `while` 아래에 들여쓰기된 문장이 실행됩니다.
