# 들여쓰기 (Indentation)

들여쓰기는 함께 묶이는 문장 그룹을 나타내는 데 사용됩니다. 이전 예제를 살펴보겠습니다.

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
```

들여쓰기는 다음 문장들을 반복되는 연산으로 함께 묶습니다.

```python
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2
```

마지막 `print()` 문은 들여쓰기되지 않았으므로 루프에 속하지 않습니다. 빈 줄은 가독성을 위한 것입니다. 실행에는 영향을 미치지 않습니다.
