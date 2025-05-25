# 필요한 라이브러리 및 데이터 가져오기

먼저 Pandas 라이브러리와 Titanic 데이터 세트를 가져와야 합니다.

```python
# Import pandas library
import pandas as pd

# Load the Titanic dataset
titanic = pd.read_csv("data/titanic.csv")
titanic.head()
```
