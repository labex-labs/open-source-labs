# 다양한 날짜 시나리오로 테스트하기

`months_diff` 함수가 다양한 날짜 시나리오에서 어떻게 작동하는지 더 잘 이해하기 위해 별도의 테스트 파일을 만들어 보겠습니다. 이 접근 방식은 코드가 예상대로 작동하는지 확인하기 위해 소프트웨어 개발에서 일반적입니다.

`/home/labex/project` 디렉토리에 `month_diff_test.py`라는 새 파일을 생성합니다.

```python
from datetime import date
from month_difference import months_diff

# Test scenario 1: Dates in the same month
date1 = date(2023, 5, 5)
date2 = date(2023, 5, 25)
print(f"Same month: {months_diff(date1, date2)} month(s)")

# Test scenario 2: Consecutive months
date3 = date(2023, 6, 28)
date4 = date(2023, 7, 15)
print(f"Consecutive months: {months_diff(date3, date4)} month(s)")

# Test scenario 3: Dates crossing year boundary
date5 = date(2023, 12, 20)
date6 = date(2024, 1, 10)
print(f"Across years: {months_diff(date5, date6)} month(s)")

# Test scenario 4: Several months apart
date7 = date(2023, 3, 10)
date8 = date(2023, 9, 20)
print(f"Several months: {months_diff(date7, date8)} month(s)")

# Test scenario 5: Dates in reverse order (negative result)
print(f"Reverse order: {months_diff(date8, date7)} month(s)")

# Test scenario 6: Exact multiples of 30 days
date9 = date(2023, 1, 1)
date10 = date(2023, 1, 31)  # 30 days
date11 = date(2023, 3, 2)   # 60 days
print(f"30 days exactly: {months_diff(date9, date10)} month(s)")
print(f"60 days exactly: {months_diff(date9, date11)} month(s)")
```

이 파일을 저장하고 실행합니다.

```bash
python3 ~/project/month_diff_test.py
```

다음과 유사한 출력을 볼 수 있습니다.

```
Same month: 1 month(s)
Consecutive months: 1 month(s)
Across years: 1 month(s)
Several months: 7 month(s)
Reverse order: -7 month(s)
30 days exactly: 1 month(s)
60 days exactly: 2 month(s)
```

이 결과를 분석해 보겠습니다.

1. **Same month (같은 달)**: 같은 달 내에서도 함수는 1 개월을 반환합니다. 이는 부분적인 달조차도 전체 달로 계산되기 때문입니다.

2. **Consecutive months (연속된 달)**: 연속된 달의 날짜에 대해 함수는 1 개월을 반환합니다.

3. **Across years (연도 경계 넘기)**: 연도 경계를 넘는 날짜에 대해서도 함수는 올바르게 계산합니다.

4. **Several months (여러 달)**: 여러 달 차이가 나는 날짜에 대해 함수는 적절한 개월 수를 계산합니다.

5. **Reverse order (역순)**: 종료 날짜가 시작 날짜보다 앞선 경우 음수 결과가 나타나며, 이는 남은 시간을 계산하는 시나리오에 적합합니다.

6. **Exact multiples (정확한 배수)**: 정확히 30 일인 경우 1 개월을 얻습니다. 60 일인 경우 2 개월을 얻습니다. 이는 함수가 월 정의의 정확한 배수로 예상대로 작동함을 확인합니다.

`months_diff` 함수는 한 달을 30 일로 정의하는 방식에 따라 이러한 모든 테스트 케이스를 올바르게 처리합니다.
