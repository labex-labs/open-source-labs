# 演習 1.7：デイブの住宅ローン

デイブは、ギドの住宅ローン、株式投資、ビットコイン取引会社との間で、50 万ドルの 30 年固定金利住宅ローンを組むことにしました。金利は 5% で、月額返済額は 2,684.11 ドルです。

以下は、デイブが住宅ローン期間中に支払う合計金額を計算するプログラムです。

```python
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)
```

このプログラムを入力して実行してください。`966279.5999999957` という答えが得られるはずです。
