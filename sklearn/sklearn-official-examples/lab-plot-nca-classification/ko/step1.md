# 라이브러리 가져오기

필요한 라이브러리를 가져오는 것으로 시작합니다. 가장 가까운 이웃 분류와 NCA 를 수행하기 위해 scikit-learn 을 사용합니다. 클래스 결정 경계를 플롯하기 위해 matplotlib 를 사용합니다.

```python
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier, NeighborhoodComponentsAnalysis
from sklearn.pipeline import Pipeline
from sklearn.inspection import DecisionBoundaryDisplay
```
