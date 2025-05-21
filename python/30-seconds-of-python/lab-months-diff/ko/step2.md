# 월 차이 함수 생성하기

이제 날짜 객체로 작업하고 일 차이를 계산하는 방법을 이해했으므로, 월 차이를 계산하는 함수를 만들어 보겠습니다.

많은 애플리케이션에서 한 달은 30 일로 근사됩니다. 이것이 항상 정확하지는 않지만 (달은 28 일에서 31 일까지 가질 수 있음), 많은 비즈니스 계산에 잘 맞는 일반적인 단순화입니다.

`month_difference.py` 파일을 열고 기존 코드 아래에 이 함수를 추가합니다.

```python
def months_diff(start, end):
    """
    Calculate the difference in months between two dates.

    Args:
        start (date): The start date
        end (date): The end date

    Returns:
        int: The number of months between the dates (rounded up)
    """
    # Calculate the difference in days
    days_difference = (end - start).days

    # Convert days to months (assuming 30 days per month) and round up
    months = ceil(days_difference / 30)

    return months
```

이 함수가 무엇을 하는지 이해해 봅시다.

1. `start`와 `end`의 두 매개변수를 사용하며, 이는 날짜 객체입니다.
2. 이 날짜 간의 일 차이를 계산합니다.
3. 일 수를 월 수로 변환하기 위해 30 으로 나눕니다.
4. 가장 가까운 정수로 올림하기 위해 `ceil()`을 사용합니다.
5. 결과를 정수로 반환합니다.

`ceil()` 함수는 많은 비즈니스 시나리오에서 부분적인 달조차도 청구 목적으로 전체 달로 계산되기 때문에 사용됩니다.

함수를 테스트하려면 파일 끝에 다음 코드를 추가합니다.

```python
# Test the months_diff function with our example dates
print(f"Months between {date1} and {date2}: {months_diff(date1, date2)}")

# Test with some other date pairs
print(f"Months between 2020-10-28 and 2020-11-25: {months_diff(date(2020, 10, 28), date(2020, 11, 25))}")
print(f"Months between 2020-12-15 and 2021-01-10: {months_diff(date(2020, 12, 15), date(2021, 01, 10))}")
```

파일을 저장하고 다시 실행합니다.

```bash
python3 ~/project/month_difference.py
```

다음과 같은 출력을 볼 수 있습니다.

```
Date 1: 2023-01-15
Date 2: 2023-03-20
Difference in days: 64
Months between 2023-01-15 and 2023-03-20: 3
Months between 2020-10-28 and 2020-11-25: 1
Months between 2020-12-15 and 2021-01-10: 1
```

다음 사항에 유의하십시오.

- 2023-01-15 와 2023-03-20 사이의 64 일은 3 개월로 계산됩니다 (64/30 = 2.13, 올림하여 3).
- 10 월 28 일과 11 월 25 일 사이의 차이는 1 개월로 계산됩니다.
- 12 월 15 일과 1 월 10 일 사이의 차이 (연도 경계를 넘는 경우) 도 1 개월로 계산됩니다.
