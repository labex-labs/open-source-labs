# 데이터셋 가져오기

첫 번째 단계는 사용할 데이터셋을 가져오는 것입니다.

```python
# pandas 라이브러리 가져오기
import pandas as pd

# 데이터셋 읽기
titanic = pd.read_csv("data/titanic.csv")

# 데이터셋의 처음 5 개 행 표시
titanic.head()
```
