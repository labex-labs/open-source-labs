# 실용적인 애플리케이션 생성: 구독 계산기

이제 월 차이를 계산하는 신뢰할 수 있는 함수가 있으므로, 이를 실제 시나리오에 적용해 보겠습니다. 두 날짜 사이의 서비스 구독 비용을 결정하는 구독 계산기를 만들 것입니다.

`/home/labex/project` 디렉토리에 `subscription_calculator.py`라는 새 파일을 생성합니다.

```python
from datetime import date, timedelta
from month_difference import months_diff

def calculate_subscription_cost(start_date, end_date, monthly_fee):
    """
    Calculate the total cost of a subscription between two dates.

    Args:
        start_date (date): Subscription start date
        end_date (date): Subscription end date
        monthly_fee (float): Cost per month

    Returns:
        float: Total subscription cost
    """
    # Calculate number of months
    months = months_diff(start_date, end_date)

    # Calculate total cost
    total_cost = months * monthly_fee

    return total_cost

# Example: Calculate subscription cost for a streaming service
start = date(2023, 1, 15)  # Subscription starts January 15, 2023
end = date(2023, 8, 20)    # Ends August 20, 2023
monthly_cost = 9.99        # $9.99 per month

total = calculate_subscription_cost(start, end, monthly_cost)
print(f"Subscription period: {start} to {end}")
print(f"Monthly fee: ${monthly_cost:.2f}")
print(f"Total cost: ${total:.2f}")

# Compare with an annual plan
annual_cost = 99.99  # $99.99 per year
print(f"\nAnnual plan cost: ${annual_cost:.2f}")
print(f"Monthly plan for same period: ${total:.2f}")

if total > annual_cost:
    print(f"Savings with annual plan: ${total - annual_cost:.2f}")
else:
    print(f"Additional cost for annual plan: ${annual_cost - total:.2f}")

# Calculate cost for a trial period
today = date.today()
trial_end = today + timedelta(days=7)  # 7-day trial
trial_cost = calculate_subscription_cost(today, trial_end, monthly_cost)
print(f"\nOne-week trial period: {today} to {trial_end}")
print(f"Trial period cost: ${trial_cost:.2f}")
```

파일을 저장하고 실행합니다.

```bash
python3 ~/project/subscription_calculator.py
```

다음과 유사한 출력을 볼 수 있습니다 (체험 날짜는 현재 날짜를 표시합니다).

```
Subscription period: 2023-01-15 to 2023-08-20
Monthly fee: $9.99
Total cost: $79.92

Annual plan cost: $99.99
Monthly plan for same period: $79.92
Additional cost for annual plan: $20.07

One-week trial period: 2023-06-01 to 2023-06-08
Trial period cost: $9.99
```

이 애플리케이션은 `months_diff` 함수를 실제 시나리오에서 어떻게 사용할 수 있는지 보여줍니다.

1. 두 날짜 사이의 개월 수를 기준으로 구독의 총 비용을 계산합니다.
2. 사용자가 어떤 요금제가 더 경제적인지 결정하도록 돕기 위해 이 비용을 연간 요금제와 비교합니다.
3. 짧은 체험 기간의 비용을 계산합니다.

7 일 체험 기간조차도 모델에서 한 달 전체로 청구되는 것을 확인하십시오. 이는 함수가 부분적인 달을 전체 달로 올림하기 때문이며, 이는 구독 청구에서 일반적입니다.

이러한 유형의 계산은 다음에서 자주 사용됩니다.

- 구독 서비스 (스트리밍, 소프트웨어, 멤버십)
- 대출 및 모기지 계산
- 임대 계약
- 프로젝트 청구
