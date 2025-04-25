# 実用的なアプリケーションの作成：サブスクリプション料金計算機

月数の差を計算する信頼性の高い関数ができたので、これを実際のシナリオに適用しましょう。2 つの日付間のサービスサブスクリプションの料金を算出するサブスクリプション料金計算機を作成します。

`/home/labex/project` ディレクトリに `subscription_calculator.py` という名前の新しいファイルを作成します。

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

ファイルを保存して実行します。

```bash
python3 ~/project/subscription_calculator.py
```

以下のような出力が表示されるはずです（トライアル期間の日付は現在の日付になります）。

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

このアプリケーションは、`months_diff` 関数が実用的なシナリオでどのように使えるかを示しています。

1. 2 つの日付間の月数に基づいてサブスクリプションの総料金を計算します。
2. この料金を年間プランと比較して、ユーザーがどのプランがより経済的かを判断できるようにします。
3. 短期のトライアル期間の料金を計算します。

このモデルでは、7 日間のトライアル期間でも 1 か月分の料金が請求されることに注意してください。これは、関数が部分的な月をすべて 1 か月に切り上げるためで、サブスクリプションの請求では一般的な方法です。

この種の計算は、以下のような場面で頻繁に使われます。

- サブスクリプションサービス（ストリーミング、ソフトウェア、会員制サービス）
- ローンや住宅ローンの計算
- レンタル契約
- プロジェクトの請求
