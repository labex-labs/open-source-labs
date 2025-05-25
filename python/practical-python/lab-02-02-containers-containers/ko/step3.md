# 리스트 구성

처음부터 리스트를 구성합니다.

```python
records = []  # Initial empty list

# .append() 를 사용하여 더 많은 항목을 추가합니다.
records.append(('GOOG', 100, 490.10))
records.append(('IBM', 50, 91.3))
...
```

파일에서 레코드를 읽을 때의 예시입니다.

```python
records = []  # Initial empty list

with open('portfolio.csv', 'rt') as f:
    next(f) # Skip header
    for line in f:
        row = line.split(',')
        records.append((row[0], int(row[1]), float(row[2])))
```
