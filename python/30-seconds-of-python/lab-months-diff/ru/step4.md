# Создание практического приложения: калькулятор подписок

Теперь, когда у нас есть надежная функция для вычисления разницы в месяцах, давайте применим ее к реальному сценарию. Мы создадим калькулятор подписок, который определяет стоимость подписки на услугу между двумя датами.

Создайте новый файл с именем `subscription_calculator.py` в директории `/home/labex/project`:

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

Сохраните файл и запустите его:

```bash
python3 ~/project/subscription_calculator.py
```

Вы должны увидеть вывод, похожий на следующий (даты испытательного периода будут соответствовать текущей дате):

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

Это приложение демонстрирует, как наша функция `months_diff` может быть использована в практическом сценарии:

1. Мы вычисляем общую стоимость подписки на основе количества месяцев между двумя датами.
2. Мы сравниваем эту стоимость с годовой подпиской, чтобы помочь пользователю решить, какую подписку выбрать.
3. Мы вычисляем стоимость короткого испытательного периода.

Обратите внимание, что даже 7-дневный испытательный период в нашей модели оплачивается как полный месяц. Это потому, что наша функция округляет любую частичную часть месяца до целого месяца, что распространено в биллинге подписок.

Такой тип расчетов часто используется в:

- Подписочных услугах (стримминг, программное обеспечение, членства)
- Расчетах по кредитам и ипотекам
- Арендных договорах
- Проектной отчетности
