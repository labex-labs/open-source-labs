# 연습 문제 3.10: 오류 무시하기

`parse_csv()` 함수를 수정하여 사용자가 명시적으로 원하는 경우 구문 분석 오류 메시지를 무시할 수 있도록 합니다. 예를 들어:

```python
>>> portfolio = parse_csv('missing.csv', types=[str,int,float], silence_errors=True)
>>> portfolio
[{'name': 'AA', 'shares': 100, 'price': 32.2}, {'name': 'IBM', 'shares': 50, 'price': 91.1}, {'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'GE', 'shares': 95, 'price': 40.37}, {'name': 'MSFT', 'shares': 50, 'price': 65.1}]
>>>
```

오류 처리는 대부분의 프로그램에서 제대로 처리하기 가장 어려운 것 중 하나입니다. 일반적으로 오류를 조용히 무시해서는 안 됩니다. 대신 문제를 보고 사용자가 원하는 경우 오류 메시지를 무시할 수 있는 옵션을 제공하는 것이 좋습니다.
