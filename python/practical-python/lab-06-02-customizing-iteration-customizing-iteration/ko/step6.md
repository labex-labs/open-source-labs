# 연습 문제 6.7: 포트폴리오 감시

`follow.py` 프로그램을 수정하여 주식 데이터 스트림을 감시하고 포트폴리오에 있는 주식에 대한 정보만 표시하는 티커를 인쇄하도록 하십시오. 예를 들어:

```python
if __name__ == '__main__':
    import report

    portfolio = report.read_portfolio('portfolio.csv')

    for line in follow('stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```

참고: 이것이 작동하려면 `Portfolio` 클래스가 `in` 연산자를 지원해야 합니다. 연습 문제 6.3 을 참조하고 `__contains__()` 연산자를 구현했는지 확인하십시오.
