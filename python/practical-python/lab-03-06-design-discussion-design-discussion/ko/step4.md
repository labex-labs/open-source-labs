# 연습 문제 3.17: 파일 이름에서 파일 유사 객체로

이제 `parse_csv()` 함수를 포함하는 파일 `fileparse.py`를 만들었습니다. 이 함수는 다음과 같이 작동했습니다.

```python
>>> import fileparse
>>> portfolio = fileparse.parse_csv('portfolio.csv', types=[str,int,float])
>>>
```

현재, 이 함수는 파일 이름을 전달받도록 되어 있습니다. 하지만 코드를 더 유연하게 만들 수 있습니다. 파일 유사/이터러블 (iterable) 객체와 함께 작동하도록 함수를 수정하십시오. 예를 들어:

```python
>>> import fileparse
>>> import gzip
>>> with gzip.open('portfolio.csv.gz', 'rt') as file:
...      port = fileparse.parse_csv(file, types=[str,int,float])
...
>>> lines = ['name,shares,price', 'AA,100,34.23', 'IBM,50,91.1', 'HPE,75,45.1']
>>> port = fileparse.parse_csv(lines, types=[str,int,float])
>>>
```

이 새로운 코드에서, 이전처럼 파일 이름을 전달하면 어떻게 될까요?

```python
>>> port = fileparse.parse_csv('portfolio.csv', types=[str,int,float])
>>> port
... 출력 결과를 확인하세요 (엉망일 것입니다) ...
>>>
```

네, 주의해야 합니다. 이를 방지하기 위해 안전 점검을 추가할 수 있을까요?
