# Python 에서 날짜 객체 이해하기

날짜 간의 월 차이를 계산하기 전에, Python 에서 날짜 객체로 작업하는 방법을 이해해야 합니다. 이 단계에서는 `datetime` 모듈에 대해 배우고 몇 가지 날짜 객체를 생성할 것입니다.

먼저, 프로젝트 디렉토리에 새 Python 파일을 생성해 보겠습니다. WebIDE 를 열고 왼쪽 탐색 패널에서 "New File" 아이콘을 클릭합니다. 파일 이름을 `month_difference.py`로 지정하고 `/home/labex/project` 디렉토리에 저장합니다.

이제 필요한 모듈을 가져오기 위해 다음 코드를 추가합니다.

```python
from datetime import date
from math import ceil

# Create example date objects
date1 = date(2023, 1, 15)  # January 15, 2023
date2 = date(2023, 3, 20)  # March 20, 2023

# Print the dates to see their format
print(f"Date 1: {date1}")
print(f"Date 2: {date2}")

# Calculate the difference in days
day_difference = (date2 - date1).days
print(f"Difference in days: {day_difference}")
```

파일을 저장하고 터미널을 사용하여 실행합니다.

```bash
python3 ~/project/month_difference.py
```

다음과 유사한 출력을 볼 수 있습니다.

```
Date 1: 2023-01-15
Date 2: 2023-03-20
Difference in days: 64
```

`datetime` 모듈의 `date` 클래스를 사용하면 연, 월, 일을 지정하여 날짜 객체를 생성할 수 있습니다. 한 날짜에서 다른 날짜를 빼면 Python 은 `timedelta` 객체를 반환합니다. `.days` 속성을 사용하여 이 객체 내의 일 수를 액세스할 수 있습니다.

이 예제에서는 2023 년 1 월 15 일과 2023 년 3 월 20 일 사이에 64 일이 있습니다.
