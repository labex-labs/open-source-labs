# 라이브러리 가져오기

투표 회귀 분석 (Voting Regressor) 을 사용하여 당뇨병 예측을 수행하기 위해 필요한 라이브러리를 가져옵니다.

```python
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import VotingRegressor
```
