# 라이브러리 가져오기

먼저 필요한 라이브러리를 가져와야 합니다. 시각화에는 `matplotlib`를, 데이터셋 로드 및 평가에는 `sklearn`의 `datasets`와 `metrics`를, 서포트 벡터 머신 학습에는 `svm`을 사용합니다.

```python
import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
```
