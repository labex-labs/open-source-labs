# 创建实用应用程序：订阅费用计算器

既然我们已经有了一个可靠的计算月数差的函数，那么让我们将其应用到一个实际场景中。我们将创建一个订阅费用计算器，用于确定两个日期之间某项服务订阅的费用。

在 `/home/labex/project` 目录下创建一个名为 `subscription_calculator.py` 的新文件：

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

保存文件并运行：

```bash
python3 ~/project/subscription_calculator.py
```

你应该会看到类似以下的输出（试用日期将显示你当前的日期）：

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

这个应用程序展示了我们的 `months_diff` 函数如何在实际场景中使用：

1. 我们根据两个日期之间的月数计算订阅的总费用。
2. 我们将这个费用与年度计划进行比较，以帮助用户决定哪种计划更经济。
3. 我们计算短期试用期间的费用。

注意在我们的模型中，即使是 7 天的试用也会按一个整月收费。这是因为我们的函数会将任何不足一个月的部分向上舍入为一个整月，这在订阅计费中很常见。

这种计算方式经常用于以下场景：

- 订阅服务（流媒体、软件、会员服务）
- 贷款和抵押贷款计算
- 租赁协议
- 项目计费
