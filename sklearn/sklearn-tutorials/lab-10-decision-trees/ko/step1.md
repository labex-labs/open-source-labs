# 필요한 라이브러리 가져오기

먼저, 필요한 라이브러리를 가져와야 합니다. 의사결정 트리 분류기를 구축하고 학습하는 데 scikit-learn 을 사용할 것입니다.

```python
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
```
