# 기본 반복 및 시퀀스 언패킹 (Sequence Unpacking)

이 단계에서는 `for` 루프를 사용한 기본 반복과 Python 에서의 시퀀스 언패킹을 살펴보겠습니다. 반복은 프로그래밍의 기본적인 개념으로, 시퀀스 내의 각 항목을 하나씩 처리할 수 있게 해줍니다. 반면에 시퀀스 언패킹은 시퀀스의 개별 요소를 변수에 편리하게 할당할 수 있도록 해줍니다.

## CSV 파일에서 데이터 로드하기

CSV 파일에서 데이터를 로드하는 것으로 시작해 보겠습니다. CSV (Comma-Separated Values, 쉼표로 구분된 값) 는 표 형식 데이터를 저장하는 데 사용되는 일반적인 파일 형식입니다. 시작하려면 WebIDE 에서 터미널을 열고 Python 인터프리터를 시작해야 합니다. 이렇게 하면 Python 코드를 대화식으로 실행할 수 있습니다.

```bash
cd ~/project
python3
```

이제 Python 인터프리터에 들어왔으므로, `portfolio.csv` 파일에서 데이터를 읽기 위해 다음 Python 코드를 실행할 수 있습니다. 먼저, CSV 파일 작업을 위한 기능을 제공하는 `csv` 모듈을 가져옵니다. 그런 다음 파일을 열고 데이터를 읽기 위해 `csv.reader` 객체를 생성합니다. `next` 함수를 사용하여 열 머리글을 가져오고, 나머지 데이터를 리스트로 변환합니다. 마지막으로, `pprint` 모듈의 `pprint` 함수를 사용하여 행을 더 읽기 쉬운 형식으로 출력합니다.

```python
import csv

f = open('portfolio.csv')
f_csv = csv.reader(f)
headers = next(f_csv)    # Get the column headers
rows = list(f_csv)       # Convert the remaining data to a list
from pprint import pprint
pprint(rows)             # Pretty print the rows
```

다음과 유사한 출력을 볼 수 있습니다.

```
[['AA', '100', '32.20'],
 ['IBM', '50', '91.10'],
 ['CAT', '150', '83.44'],
 ['MSFT', '200', '51.23'],
 ['GE', '95', '40.37'],
 ['MSFT', '50', '65.10'],
 ['IBM', '100', '70.44']]
```

## `for` 루프를 사용한 기본 반복

Python 의 `for` 문은 리스트, 튜플 또는 문자열과 같은 모든 데이터 시퀀스를 반복하는 데 사용됩니다. 이 경우, CSV 파일에서 로드한 데이터의 행을 반복하는 데 사용할 것입니다.

```python
for row in rows:
    print(row)
```

이 코드는 `rows` 리스트의 각 행을 순회하며 출력합니다. CSV 파일의 각 행이 하나씩 출력되는 것을 볼 수 있습니다.

```
['AA', '100', '32.20']
['IBM', '50', '91.10']
['CAT', '150', '83.44']
['MSFT', '200', '51.23']
['GE', '95', '40.37']
['MSFT', '50', '65.10']
['IBM', '100', '70.44']
```

## 루프에서 시퀀스 언패킹

Python 에서는 `for` 루프에서 시퀀스를 직접 언패킹할 수 있습니다. 이는 시퀀스의 각 항목의 구조를 알고 있을 때 매우 유용합니다. 이 경우, `rows` 리스트의 각 행에는 이름, 주식 수, 가격의 세 가지 요소가 포함되어 있습니다. 이러한 요소를 `for` 루프에서 직접 언패킹할 수 있습니다.

```python
for name, shares, price in rows:
    print(name, shares, price)
```

이 코드는 각 행을 `name`, `shares`, `price` 변수로 언패킹한 다음 출력합니다. 데이터를 더 읽기 쉬운 형식으로 출력하는 것을 볼 수 있습니다.

```
AA 100 32.20
IBM 50 91.10
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
MSFT 50 65.10
IBM 100 70.44
```

일부 값이 필요하지 않은 경우, 해당 값을 신경 쓰지 않음을 나타내기 위해 `_`를 자리 표시자로 사용할 수 있습니다. 예를 들어, 이름과 가격만 출력하려면 다음 코드를 사용할 수 있습니다.

```python
for name, _, price in rows:
    print(name, price)
```

이 코드는 각 행의 두 번째 요소를 무시하고 이름과 가격만 출력합니다.

```
AA 32.20
IBM 91.10
CAT 83.44
MSFT 51.23
GE 40.37
MSFT 65.10
IBM 70.44
```

## `*` 연산자를 사용한 확장 언패킹

더 고급 언패킹을 위해 `*` 연산자를 와일드카드로 사용할 수 있습니다. 이를 통해 여러 요소를 리스트로 수집할 수 있습니다. 이 기술을 사용하여 데이터를 이름별로 그룹화해 보겠습니다.

```python
from collections import defaultdict

byname = defaultdict(list)
for name, *data in rows:
    byname[name].append(data)

# Print the data for IBM
print(byname['IBM'])

# Iterate through IBM's data
for shares, price in byname['IBM']:
    print(shares, price)
```

이 코드에서는 먼저 `collections` 모듈에서 `defaultdict` 클래스를 가져옵니다. `defaultdict`는 키가 존재하지 않는 경우 자동으로 새 값 (이 경우 빈 리스트) 을 생성하는 딕셔너리입니다. 그런 다음 `*` 연산자를 사용하여 첫 번째 요소를 제외한 모든 요소를 `data`라는 리스트로 수집합니다. 이 리스트를 이름별로 그룹화하여 `byname` 딕셔너리에 저장합니다. 마지막으로, IBM 에 대한 데이터를 출력하고 이를 반복하여 주식 수와 가격을 출력합니다.

출력:

```
[['50', '91.10'], ['100', '70.44']]
50 91.10
100 70.44
```

이 예제에서 `*data`는 첫 번째 항목을 제외한 모든 항목을 리스트로 수집한 다음, 이름별로 그룹화된 딕셔너리에 저장합니다. 이는 가변 길이 시퀀스를 처리하기 위한 강력한 기술입니다.
