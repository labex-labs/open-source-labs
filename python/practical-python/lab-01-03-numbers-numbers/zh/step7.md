# 练习1.7：戴夫的房贷

戴夫决定向吉多的房贷、股票投资与比特币交易公司申请一笔50万美元的30年期固定利率房贷。年利率为5%，每月还款额为2684.11美元。

以下是一个计算戴夫在房贷存续期内总共需支付金额的程序：

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

输入此程序并运行它。你应该会得到一个答案 `966279.5999999957`。
