# 시카고 교통국 (CTA) 데이터를 사용한 데이터 분석 챌린지

이제 다양한 Python 데이터 구조와 collections 모듈을 사용하는 연습을 했으므로 이러한 기술을 실제 데이터 분석 작업에 적용할 때입니다. 이 실험에서는 시카고 교통국 (CTA) 의 버스 승차 데이터에 대한 분석을 수행합니다. 이 실용적인 응용 프로그램은 실제 데이터 세트에서 의미 있는 정보를 추출하기 위해 Python 을 사용하는 방법을 이해하는 데 도움이 됩니다.

## 데이터 이해

먼저, 작업할 교통 데이터를 살펴보겠습니다. Python 터미널에서 데이터를 로드하고 기본 구조를 이해하기 위해 일부 코드를 실행합니다.

```python
>>> import readrides
>>> rows = readrides.read_rides_as_dicts('/home/labex/project/ctabus.csv')
>>> print(len(rows))
# This will show the number of records in the dataset

>>> # Let's look at the first record to understand the structure
>>> import pprint
>>> pprint.pprint(rows[0])
```

`import readrides` 문은 CSV 파일에서 데이터를 읽는 함수가 있는 사용자 지정 모듈을 가져옵니다. `readrides.read_rides_as_dicts` 함수는 지정된 CSV 파일에서 데이터를 읽고 각 행을 딕셔너리로 변환합니다. `len(rows)`는 데이터 세트의 총 레코드 수를 제공합니다. `pprint.pprint(rows[0])`을 사용하여 첫 번째 레코드를 인쇄하면 각 레코드의 구조를 명확하게 볼 수 있습니다.

데이터에는 다양한 버스 노선에 대한 일일 승차 기록이 포함되어 있습니다. 각 레코드에는 다음이 포함됩니다.

- `route`: 버스 노선 번호
- `date`: "YYYY-MM-DD" 형식의 날짜
- `daytype`: 평일의 경우 "W", 토요일의 경우 "A", 일요일/공휴일의 경우 "U"
- `rides`: 해당 날짜의 승차 횟수

## 분석 작업

각 챌린지 질문을 하나씩 해결해 보겠습니다.

### 질문 1: 시카고에는 몇 개의 버스 노선이 있습니까?

이 질문에 답하려면 데이터 세트에서 고유한 모든 노선 번호를 찾아야 합니다. 이 작업에 세트 컴프리헨션을 사용합니다.

```python
>>> # Get all unique route numbers using a set comprehension
>>> unique_routes = {row['route'] for row in rows}
>>> print(len(unique_routes))
```

세트 컴프리헨션은 세트를 만드는 간결한 방법입니다. 이 경우 `rows` 목록의 각 행을 반복하고 `route` 값을 추출합니다. 세트는 고유한 요소만 저장하므로 모든 고유한 노선 번호의 세트가 생성됩니다. 이 세트의 길이를 인쇄하면 고유한 버스 노선의 총 수를 얻을 수 있습니다.

이러한 노선 중 일부가 무엇인지 확인할 수도 있습니다.

```python
>>> # Print a few of the route numbers
>>> print(list(unique_routes)[:10])
```

여기서는 고유한 노선의 세트를 목록으로 변환한 다음 해당 목록의 처음 10 개 요소를 인쇄합니다.

### 질문 2: 2011 년 2 월 2 일에 22 번 버스를 탄 사람은 몇 명입니까?

이 질문의 경우, 주어진 노선과 날짜와 일치하는 특정 레코드를 찾기 위해 데이터를 필터링해야 합니다.

```python
>>> # Find rides on route 22 on February 2, 2011
>>> target_date = "2011-02-02"
>>> target_route = "22"
>>>
>>> for row in rows:
...     if row['route'] == target_route and row['date'] == target_date:
...         print(f"Rides on route {target_route} on {target_date}: {row['rides']}")
...         break
```

먼저 `target_date` 및 `target_route` 변수를 정의합니다. 그런 다음 `rows` 목록의 각 행을 반복합니다. 각 행에 대해 `route` 및 `date`가 대상 값과 일치하는지 확인합니다. 일치하는 항목이 발견되면 승차 횟수를 인쇄하고 찾고 있는 레코드를 찾았으므로 루프를 종료합니다.

`target_date` 및 `target_route` 변수를 변경하여 모든 날짜의 모든 노선을 확인할 수 있도록 수정할 수 있습니다.

### 질문 3: 각 버스 노선에서 총 승차 횟수는 얼마입니까?

Counter 를 사용하여 노선별 총 승차 횟수를 계산해 보겠습니다. Counter 는 `collections` 모듈의 딕셔너리 하위 클래스로, 해시 가능한 객체를 계산하는 데 사용됩니다.

```python
>>> from collections import Counter
>>>
>>> # Initialize a counter
>>> total_rides_by_route = Counter()
>>>
>>> # Sum up rides for each route
>>> for row in rows:
...     total_rides_by_route[row['route']] += row['rides']
...
>>> # View the top 5 routes by total ridership
>>> for route, rides in total_rides_by_route.most_common(5):
...     print(f"Route {route}: {rides:,} total rides")
```

먼저 `collections` 모듈에서 `Counter` 클래스를 가져옵니다. 그런 다음 `total_rides_by_route`라는 빈 카운터를 초기화합니다. `rows` 목록의 각 행을 반복하면서 각 노선의 승차 횟수를 카운터에 추가합니다. 마지막으로 `most_common(5)` 메서드를 사용하여 총 승차 횟수가 가장 많은 상위 5 개 노선을 가져와 결과를 인쇄합니다.

### 질문 4: 2001 년부터 2011 년까지 승차 횟수가 가장 많이 증가한 5 개의 버스 노선은 무엇입니까?

이것은 더 복잡한 작업입니다. 각 노선에 대해 2001 년의 승차 횟수를 2011 년의 승차 횟수와 비교해야 합니다.

```python
>>> # Create dictionaries to store total annual rides by route
>>> rides_2001 = Counter()
>>> rides_2011 = Counter()
>>>
>>> # Collect data for each year
>>> for row in rows:
...     if row['date'].startswith('2001-'):
...         rides_2001[row['route']] += row['rides']
...     elif row['date'].startswith('2011-'):
...         rides_2011[row['route']] += row['rides']
...
>>> # Calculate increases
>>> increases = {}
>>> for route in unique_routes:
...     if route in rides_2001 and route in rides_2011:
...         increase = rides_2011[route] - rides_2001[route]
...         increases[route] = increase
...
>>> # Find the top 5 routes with the biggest increases
>>> import heapq
>>> top_5_increases = heapq.nlargest(5, increases.items(), key=lambda x: x[1])
>>>
>>> # Display the results
>>> print("Top 5 routes with the greatest ridership increase from 2001 to 2011:")
>>> for route, increase in top_5_increases:
...     print(f"Route {route}: increased by {increase:,} rides")
...     print(f"  2001 rides: {rides_2001[route]:,}")
...     print(f"  2011 rides: {rides_2011[route]:,}")
...     print()
```

먼저 2001 년과 2011 년의 각 노선에 대한 총 승차 횟수를 저장하기 위해 `rides_2001` 및 `rides_2011`의 두 개의 `Counter` 객체를 만듭니다. `rows` 목록의 각 행을 반복하면서 날짜가 '2001-' 또는 '2011-'로 시작하는지 확인하고 승차 횟수를 해당 카운터에 추가합니다.

그런 다음 각 노선의 승차 횟수 증가를 저장하기 위해 빈 딕셔너리 `increases`를 만듭니다. 고유한 노선을 반복하고 각 노선에 대해 2001 년 승차 횟수에서 2011 년 승차 횟수를 빼서 증가를 계산합니다.

가장 큰 증가를 보인 상위 5 개 노선을 찾기 위해 `heapq.nlargest` 함수를 사용합니다. 이 함수는 반환할 요소 수 (이 경우 5), 반복 가능한 객체 (`increases.items()`) 및 요소를 비교하는 방법을 지정하는 키 함수 (`lambda x: x[1]`) 를 사용합니다.

마지막으로 결과를 인쇄하여 노선 번호, 승차 횟수 증가 및 2001 년과 2011 년의 승차 횟수를 표시합니다.

이 분석은 10 년 동안 승차 횟수가 가장 많이 증가한 버스 노선을 식별하며, 이는 인구 패턴 변화, 서비스 개선 또는 기타 흥미로운 추세를 나타낼 수 있습니다.

이러한 분석을 여러 가지 방법으로 확장할 수 있습니다. 예를 들어 다음을 수행할 수 있습니다.

- 요일별 승차 패턴 분석
- 승차 횟수가 감소하는 노선 찾기
- 계절별 승차 횟수 변동 비교

이 랩에서 배운 기술은 이러한 종류의 데이터 탐색 및 분석을 위한 견고한 기반을 제공합니다.
