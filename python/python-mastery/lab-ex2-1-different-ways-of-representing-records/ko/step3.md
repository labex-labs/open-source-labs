# 튜플을 사용하여 구조화된 데이터 작업

지금까지는 원시 텍스트 데이터를 저장하는 것을 다루었습니다. 그러나 데이터 분석과 관련하여 일반적으로 데이터를 더 체계적이고 구조화된 형식으로 변환해야 합니다. 이렇게 하면 다양한 작업을 수행하고 데이터에서 통찰력을 얻기가 더 쉬워집니다. 이 단계에서는 `csv` 모듈을 사용하여 데이터를 튜플 목록으로 읽는 방법을 배웁니다. 튜플은 여러 값을 저장할 수 있는 Python 의 간단하고 유용한 데이터 구조입니다.

## 튜플로 리더 함수 만들기

`/home/labex/project` 디렉토리에 `readrides.py`라는 새 파일을 만들어 보겠습니다. 이 파일에는 CSV 파일에서 데이터를 읽어 튜플 목록으로 저장하는 코드가 포함됩니다.

```python
# readrides.py
import csv
import tracemalloc

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

if __name__ == '__main__':
    tracemalloc.start()

    rows = read_rides_as_tuples('/home/labex/project/ctabus.csv')

    current, peak = tracemalloc.get_traced_memory()
    print(f'Number of records: {len(rows)}')
    print(f'First record: {rows[0]}')
    print(f'Second record: {rows[1]}')
    print(f'Memory Use: Current {current/1024/1024:.2f} MB, Peak {peak/1024/1024:.2f} MB')
```

이 스크립트는 `read_rides_as_tuples`라는 함수를 정의합니다. 단계별로 수행하는 작업은 다음과 같습니다.

1. `filename` 매개변수로 지정된 CSV 파일을 엽니다. 이를 통해 파일 내부의 데이터에 액세스할 수 있습니다.
2. `csv` 모듈을 사용하여 파일의 각 줄을 구문 분석합니다. `csv.reader` 함수는 줄을 개별 값으로 분할하는 데 도움이 됩니다.
3. 각 행에서 네 개의 필드 (노선, 날짜, 요일 유형 및 승차 횟수) 를 추출합니다. 이러한 필드는 데이터 분석에 중요합니다.
4. 'rides' 필드를 정수로 변환합니다. CSV 파일의 데이터가 처음에 문자열 형식이고 계산에 숫자 값이 필요하기 때문에 필요합니다.
5. 이 네 개의 값으로 튜플을 만듭니다. 튜플은 불변 (immutable) 이므로 생성된 후에는 값을 변경할 수 없습니다.
6. 튜플을 `records`라는 목록에 추가합니다. 이 목록은 CSV 파일의 모든 레코드를 저장합니다.

이제 스크립트를 실행해 보겠습니다. 터미널을 열고 다음 명령을 입력합니다.

```bash
python3 /home/labex/project/readrides.py
```

다음과 유사한 출력이 표시됩니다.

```
Number of records: 577563
First record: ('3', '01/01/2001', 'U', 7354)
Second record: ('4', '01/01/2001', 'U', 9288)
Memory Use: Current 89.12 MB, Peak 89.15 MB
```

이전 예제와 비교하여 메모리 사용량이 증가했음을 알 수 있습니다. 다음과 같은 몇 가지 이유가 있습니다.

1. 이제 데이터를 구조화된 형식 (튜플) 으로 저장하고 있습니다. 구조화된 데이터는 일반적으로 정의된 구성이 있기 때문에 더 많은 메모리가 필요합니다.
2. 튜플의 각 값은 별도의 Python 객체입니다. Python 객체에는 메모리 사용량 증가에 기여하는 오버헤드가 있습니다.
3. 이러한 모든 튜플을 저장하는 추가 목록 구조가 있습니다. 목록은 요소 저장을 위해 메모리도 사용합니다.

이 접근 방식을 사용하는 장점은 이제 데이터가 제대로 구조화되어 분석할 준비가 되었다는 것입니다. 인덱스로 각 레코드의 특정 필드에 쉽게 액세스할 수 있습니다. 예를 들어:

```python
# Example of accessing tuple elements (add this to readrides.py file to try it)
first_record = rows[0]
route = first_record[0]
date = first_record[1]
daytype = first_record[2]
rides = first_record[3]
print(f"Route: {route}, Date: {date}, Day type: {daytype}, Rides: {rides}")
```

그러나 숫자 인덱스로 데이터에 액세스하는 것은 항상 직관적이지 않습니다. 특히 많은 필드를 처리할 때 어떤 인덱스가 어떤 필드에 해당하는지 기억하기 어려울 수 있습니다. 다음 단계에서는 코드를 더 읽기 쉽고 유지 관리 가능하게 만들 수 있는 다른 데이터 구조를 살펴보겠습니다.
