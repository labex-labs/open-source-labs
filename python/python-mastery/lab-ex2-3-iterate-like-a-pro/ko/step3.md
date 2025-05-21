# 제너레이터 표현식과 메모리 효율성

이 단계에서는 제너레이터 표현식을 살펴보겠습니다. 이는 Python 에서 대용량 데이터 세트를 처리할 때 매우 유용합니다. 코드를 훨씬 더 메모리 효율적으로 만들 수 있으며, 이는 많은 양의 데이터를 처리할 때 중요합니다.

## 제너레이터 표현식 이해하기

제너레이터 표현식은 리스트 컴프리헨션과 유사하지만 중요한 차이점이 있습니다. 리스트 컴프리헨션을 사용하면 Python 은 모든 결과를 한 번에 포함하는 리스트를 생성합니다. 이는 특히 대용량 데이터 세트로 작업하는 경우 많은 메모리를 차지할 수 있습니다. 반면에 제너레이터 표현식은 필요에 따라 한 번에 하나씩 결과를 생성합니다. 즉, 모든 결과를 한 번에 메모리에 저장할 필요가 없으므로 상당한 양의 메모리를 절약할 수 있습니다.

이것이 어떻게 작동하는지 간단한 예제를 살펴보겠습니다.

```python
# Start a new Python session if needed
# python3

# List comprehension (creates a list in memory)
nums = [1, 2, 3, 4, 5]
squares_list = [x*x for x in nums]
print(squares_list)

# Generator expression (creates a generator object)
squares_gen = (x*x for x in nums)
print(squares_gen)  # This doesn't print the values, just the generator object

# Iterate through the generator to get values
for n in squares_gen:
    print(n)
```

이 코드를 실행하면 다음과 같은 출력을 볼 수 있습니다.

```
[1, 4, 9, 16, 25]
<generator object <genexpr> at 0x7f...>
1
4
9
16
25
```

제너레이터에 대해 주목해야 할 중요한 점은 한 번만 반복할 수 있다는 것입니다. 제너레이터의 모든 값을 처리하고 나면 소진되어 값을 다시 가져올 수 없습니다.

```python
# Try to iterate again over the same generator
for n in squares_gen:
    print(n)  # Nothing will be printed, as the generator is already exhausted
```

`next()` 함수를 사용하여 제너레이터에서 한 번에 하나씩 값을 수동으로 가져올 수도 있습니다.

```python
# Create a fresh generator
squares_gen = (x*x for x in nums)

# Get values one by one
print(next(squares_gen))  # 1
print(next(squares_gen))  # 4
print(next(squares_gen))  # 9
```

제너레이터에 더 이상 값이 없으면 `next()`를 호출하면 `StopIteration` 예외가 발생합니다.

## yield 를 사용한 제너레이터 함수

더 복잡한 제너레이터 로직의 경우 `yield` 문을 사용하여 제너레이터 함수를 작성할 수 있습니다. 제너레이터 함수는 한 번에 하나의 결과를 반환하는 대신 `yield`를 사용하여 한 번에 하나씩 값을 반환하는 특수한 유형의 함수입니다.

```python
def squares(nums):
    for x in nums:
        yield x*x

# Use the generator function
for n in squares(nums):
    print(n)
```

이 코드를 실행하면 다음과 같은 출력을 볼 수 있습니다.

```
1
4
9
16
25
```

## 제너레이터 표현식으로 메모리 사용량 줄이기

이제 제너레이터 표현식이 대용량 데이터 세트로 작업할 때 메모리를 절약하는 방법을 살펴보겠습니다. 매우 큰 CTA 버스 데이터 파일을 사용합니다.

```bash
cd /home/labex/project
unzip ctabus.csv.zip && rm ctabus.csv.zip
```

먼저, 메모리 집약적인 방식을 시도해 보겠습니다.

```python
import tracemalloc
tracemalloc.start()

import readrides
rows = readrides.read_rides_as_dicts('ctabus.csv')
rt22 = [row for row in rows if row['route'] == '22']
max_row = max(rt22, key=lambda row: int(row['rides']))
print(max_row)

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

이제 Python 을 종료하고 제너레이터 기반 방식과 비교하기 위해 다시 시작합니다.

```bash
exit() python3
```

```python
import tracemalloc
tracemalloc.start()

import csv
f = open('ctabus.csv')
f_csv = csv.reader(f)
headers = next(f_csv)

# Use generator expressions for all operations
rows = (dict(zip(headers, row)) for row in f_csv)
rt22 = (row for row in rows if row['route'] == '22')
max_row = max(rt22, key=lambda row: int(row['rides']))
print(max_row)

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

이 두 가지 방식 간의 메모리 사용량에 상당한 차이가 있음을 알 수 있습니다. 제너레이터 기반 방식은 모든 것을 한 번에 메모리에 로드하지 않고 데이터를 점진적으로 처리하므로 메모리 효율성이 훨씬 높습니다.

## 축소 함수를 사용한 제너레이터 표현식

제너레이터 표현식은 전체 시퀀스를 처리하고 단일 결과를 생성하는 `sum()`, `min()`, `max()`, `any()`, `all()`과 같은 함수와 결합할 때 특히 유용합니다.

몇 가지 예를 살펴보겠습니다.

```python
from readport import read_portfolio
portfolio = read_portfolio('portfolio.csv')

# Calculate the total value of the portfolio
total_value = sum(s['shares']*s['price'] for s in portfolio)
print(f"Total portfolio value: {total_value}")

# Find the minimum number of shares in any holding
min_shares = min(s['shares'] for s in portfolio)
print(f"Minimum shares in any holding: {min_shares}")

# Check if any stock is IBM
has_ibm = any(s['name'] == 'IBM' for s in portfolio)
print(f"Portfolio contains IBM: {has_ibm}")

# Check if all stocks are IBM
all_ibm = all(s['name'] == 'IBM' for s in portfolio)
print(f"All stocks are IBM: {all_ibm}")

# Count IBM shares
ibm_shares = sum(s['shares'] for s in portfolio if s['name'] == 'IBM')
print(f"Total IBM shares: {ibm_shares}")
```

제너레이터 표현식은 문자열 연산에도 유용합니다. 튜플의 값을 결합하는 방법은 다음과 같습니다.

```python
s = ('GOOG', 100, 490.10)
# This would fail: ','.join(s)
# Use a generator expression to convert all items to strings
joined = ','.join(str(x) for x in s)
print(joined)  # Output: 'GOOG,100,490.1'
```

이러한 예에서 제너레이터 표현식을 사용하는 주요 장점은 중간 리스트가 생성되지 않아 메모리 효율적인 코드가 된다는 것입니다.
