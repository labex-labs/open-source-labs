# 연습 문제 6.6: 제너레이터를 사용하여 데이터 생성

연습 문제 6.5 의 코드를 살펴보면, 코드의 첫 번째 부분은 데이터 줄을 생성하고, `while` 루프의 끝에 있는 문은 데이터를 소비합니다. 제너레이터 함수의 주요 특징은 모든 데이터 생성 코드를 재사용 가능한 함수로 이동할 수 있다는 것입니다.

파일 읽기가 제너레이터 함수 `follow(filename)`에 의해 수행되도록 연습 문제 6.5 의 코드를 수정하십시오. 다음 코드가 작동하도록 만드십시오.

```python
>>> for line in follow('stocklog.csv'):
          print(line, end='')

... 여기에 출력 줄이 생성되어야 합니다 ...
```

주식 시세 코드를 다음과 같이 수정하십시오.

```python
if __name__ == '__main__':
    for line in follow('stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```
