# 라이브러리 가져오기

이 실험에서는 필요한 라이브러리를 가져오는 것으로 시작합니다. scikit-learn 을 사용하여 합성 데이터셋을 생성하고, MLPClassifier 를 사용하여 MLP 모델을 구축하며, StandardScaler 를 사용하여 데이터를 표준화하고, make_pipeline 을 사용하여 변환 및 분류기의 파이프라인을 생성합니다.

```python
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
```
