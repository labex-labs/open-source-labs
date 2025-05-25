# 연습 문제 1.7: Dave 의 모기지 (mortgage)

Dave 는 Guido's Mortgage, Stock Investment, and Bitcoin trading corporation 에서 30 년 고정 금리 모기지 \$500,000 을 받기로 결정했습니다. 이자율은 5% 이고 월별 납입금은 \$2684.11 입니다.

다음은 Dave 가 모기지 기간 동안 지불해야 하는 총액을 계산하는 프로그램입니다:

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

이 프로그램을 입력하고 실행하십시오. `966279.5999999957`의 답을 얻어야 합니다.
