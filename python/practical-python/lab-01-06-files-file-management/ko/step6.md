# 연습 1.28: 다른 종류의 "파일" (Other kinds of "files")

gzip 압축된 데이터 파일과 같은 텍스트가 아닌 파일을 읽고 싶다면 어떻게 해야 할까요? 내장 함수 `open()`은 여기에서 도움이 되지 않지만, Python 에는 gzip 압축 파일을 읽을 수 있는 `gzip` 라이브러리 모듈이 있습니다.

시도해 보세요:

```python
>>> import gzip
>>> with gzip.open('portfolio.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')

... 출력을 확인하세요 ...
>>>
```

참고: 파일 모드 `'rt'`를 포함하는 것은 여기에서 중요합니다. 이를 잊어버리면 일반 텍스트 문자열 대신 바이트 문자열을 얻게 됩니다.
