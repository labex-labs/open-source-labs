# 예시: 기록 유지 (Keeping a History)

문제: 마지막 N 개의 항목에 대한 기록을 원합니다. 해결책: `deque`를 사용합니다.

```python
from collections import deque

history = deque(maxlen=N)
with open(filename) as f:
    for line in f:
        history.append(line)
        ...
```

`collections` 모듈은 표 작성 및 인덱싱과 같은 특수 목적의 데이터 처리 문제를 다루는 데 가장 유용한 라이브러리 모듈 중 하나일 수 있습니다.

이 연습에서는 몇 가지 간단한 예제를 살펴보겠습니다. 대화형 모드에서 주식 포트폴리오가 로드되도록 `report.py` 프로그램을 실행하여 시작합니다.

```bash
$ python3 -i report.py
```
