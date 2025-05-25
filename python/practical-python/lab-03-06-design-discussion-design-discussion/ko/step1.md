# 파일 이름 대 이터러블 (Iterables)

동일한 출력을 반환하는 다음 두 프로그램을 비교해 보겠습니다.

```python
# Provide a filename
def read_data(filename):
    records = []
    with open(filename) as f:
        for line in f:
            ...
            records.append(r)
    return records

d = read_data('file.csv')
```

```python
# Provide lines
def read_data(lines):
    records = []
    for line in lines:
        ...
        records.append(r)
    return records

with open('file.csv') as f:
    d = read_data(f)
```

- 이 함수들 중 어떤 것을 선호하십니까? 이유는 무엇입니까?
- 이 함수들 중 어떤 것이 더 유연합니까?
