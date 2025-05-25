# 딕셔너리 구성

처음부터 딕셔너리를 구성하는 예시입니다.

```python
prices = {} # Initial empty dict

# 새로운 항목 삽입
prices['GOOG'] = 513.25
prices['CAT'] = 87.22
prices['IBM'] = 93.37
```

파일의 내용으로 딕셔너리를 채우는 예시입니다.

```python
prices = {} # Initial empty dict

with open('prices.csv', 'rt') as f:
    for line in f:
        row = line.split(',')
        prices[row[0]] = float(row[1])
```

참고: `prices.csv` 파일에서 이 코드를 실행하면 거의 작동하지만, 마지막에 빈 줄이 있어 충돌이 발생합니다. 이를 해결하기 위해 코드를 수정하는 방법을 찾아야 합니다 (연습문제 2.6 참조).
