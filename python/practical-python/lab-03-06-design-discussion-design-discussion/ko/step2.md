# 심오한 아이디어: "덕 타이핑 (Duck Typing)"

[덕 타이핑 (Duck Typing)](https://en.wikipedia.org/wiki/Duck_typing)은 객체가 특정 목적에 사용될 수 있는지 여부를 결정하는 컴퓨터 프로그래밍 개념입니다. 이는 [덕 테스트 (duck test)](https://en.wikipedia.org/wiki/Duck_test)의 적용입니다.

> 만약 그것이 오리처럼 보이고, 오리처럼 헤엄치고, 오리처럼 꽥꽥거린다면, 아마도 그것은 오리일 것이다.

위의 `read_data()`의 두 번째 버전에서, 함수는 모든 이터러블 (iterable) 객체를 예상합니다. 파일의 줄뿐만 아니라.

```python
def read_data(lines):
    records = []
    for line in lines:
        ...
        records.append(r)
    return records
```

이는 다른 *lines*와 함께 사용할 수 있음을 의미합니다.

```python
# A CSV file
lines = open('data.csv')
data = read_data(lines)

# A zipped file
lines = gzip.open('data.csv.gz','rt')
data = read_data(lines)

# The Standard Input
lines = sys.stdin
data = read_data(lines)

# A list of strings
lines = ['ACME,50,91.1','IBM,75,123.45', ... ]
data = read_data(lines)
```

이 설계는 상당한 유연성을 제공합니다.

_질문: 이러한 유연성을 받아들여야 할까요, 아니면 거부해야 할까요?_
