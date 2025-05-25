# 데이터 정의

이름이 지정된 튜플을 사용하여 데이터를 정의합니다. 학생의 이름, 학년 및 성별을 포함하는 `Student` 튜플을 정의합니다. 또한 점수 값, 단위 및 백분위수를 포함하는 `Score` 튜플을 정의합니다.

```python
from collections import namedtuple

Student = namedtuple('Student', ['name', 'grade', 'gender'])
Score = namedtuple('Score', ['value', 'unit', 'percentile'])
```
