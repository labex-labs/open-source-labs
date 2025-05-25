# 연습 문제 3.9: 예외 잡기

작성한 `parse_csv()` 함수는 파일의 전체 내용을 처리하는 데 사용됩니다. 그러나 실제 환경에서는 입력 파일에 손상된, 누락된 또는 잘못된 데이터가 있을 수 있습니다. 다음 실험을 시도해 보십시오.

```python
>>> portfolio = parse_csv('missing.csv', types=[str, int, float])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 36, in parse_csv
    row = [func(val) for func, val in zip(types, row)]
ValueError: invalid literal for int() with base 10: ''
>>>
```

`parse_csv()` 함수를 수정하여 레코드 생성 중에 생성된 모든 `ValueError` 예외를 잡고 변환할 수 없는 행에 대한 경고 메시지를 인쇄하십시오.

메시지에는 행 번호와 실패한 이유에 대한 정보가 포함되어야 합니다. 함수를 테스트하려면 위의 `missing.csv` 파일을 읽어보십시오. 예를 들어:

```python
>>> portfolio = parse_csv('missing.csv', types=[str, int, float])
Row 4: Couldn't convert ['MSFT', '', '51.23']
Row 4: Reason invalid literal for int() with base 10: ''
Row 7: Couldn't convert ['IBM', '', '70.44']
Row 7: Reason invalid literal for int() with base 10: ''
>>>
>>> portfolio
[{'name': 'AA', 'shares': 100, 'price': 32.2}, {'name': 'IBM', 'shares': 50, 'price': 91.1}, {'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'GE', 'shares': 95, 'price': 40.37}, {'name': 'MSFT', 'shares': 50, 'price': 65.1}]
>>>
```
