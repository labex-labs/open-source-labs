# 들여쓰기 (Indentation) 모범 사례

- 탭 대신 공백을 사용합니다.
- 레벨당 4 개의 공백을 사용합니다.
- Python 을 인식하는 편집기를 사용합니다.

Python 의 유일한 요구 사항은 동일한 블록 내의 들여쓰기가 일관되어야 한다는 것입니다. 예를 들어, 다음은 오류입니다.

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
        day = day + 1 # ERROR
    num_bills = num_bills * 2
```
