# Doc Strings (독스트링)

독스트링 (doc-string) 형태로 문서를 포함하는 것은 좋은 습관입니다. 독스트링은 함수 이름 바로 뒤에 작성되는 문자열입니다. 이는 `help()` 함수, IDE 및 기타 도구에 정보를 제공합니다.

```python
def read_prices(filename):
    '''
    Read prices from a CSV file of name,price data
    '''
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

독스트링에 대한 좋은 습관은 함수가 수행하는 작업에 대한 짧은 한 문장 요약을 작성하는 것입니다. 더 많은 정보가 필요한 경우, 인수에 대한 자세한 설명과 함께 사용법에 대한 간단한 예시를 포함합니다.
