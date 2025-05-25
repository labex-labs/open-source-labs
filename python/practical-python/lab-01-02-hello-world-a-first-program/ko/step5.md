# 샘플 프로그램

다음 문제를 풀어보겠습니다.

> 어느 날 아침, 시카고의 시어스 타워 옆 보도에 1 달러 지폐 한 장을 놓습니다. 그 후 매일 지폐 수를 두 배로 늘립니다. 지폐 더미가 타워 높이를 초과하는 데 얼마나 걸릴까요?

다음은 `/home/labex/project` 디렉토리에 `sears.py` 파일을 생성하는 솔루션입니다.

```python
# sears.py
bill_thickness = 0.11 * 0.001 # Meters (0.11 mm)
sears_height = 442 # Height (meters)
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)
```

실행하면 다음과 같은 출력을 얻습니다.

```bash
$ python3 sears.py
1 1 0.00011
2 2 0.00022
3 4 0.00044
4 8 0.00088
5 16 0.00176
6 32 0.00352
...
21 1048576 115.34336
22 2097152 230.68672
Number of days 23
Number of bills 4194304
Final height 461.37344
```

이 프로그램을 가이드로 사용하여 Python 에 대한 여러 가지 중요한 핵심 개념을 배울 수 있습니다.
