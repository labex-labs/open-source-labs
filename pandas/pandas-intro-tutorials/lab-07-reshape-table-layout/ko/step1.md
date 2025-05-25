# 라이브러리 임포트 및 데이터 로드

먼저, 필요한 라이브러리를 임포트하고 데이터 세트를 로드하겠습니다.

```python
import pandas as pd

# 타이타닉 데이터 세트 로드
titanic = pd.read_csv("data/titanic.csv")

# 대기 질 데이터 세트 로드
air_quality = pd.read_csv("data/air_quality_long.csv", index_col="date.utc", parse_dates=True)
```
