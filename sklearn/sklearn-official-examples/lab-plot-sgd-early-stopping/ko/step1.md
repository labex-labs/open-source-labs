# 필요한 라이브러리 및 MNIST 데이터셋 로드

첫 번째 단계는 필요한 라이브러리와 데이터셋을 로드하는 것입니다. `pandas`, `numpy`, `matplotlib`, `scikit-learn` 라이브러리를 사용할 것입니다. 또한 scikit-learn 의 `fetch_openml` 함수를 사용하여 MNIST 데이터셋을 로드합니다.

```python
import time
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.utils._testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning
from sklearn.utils import shuffle

# MNIST 데이터셋 로드
def load_mnist(n_samples=None, class_0="0", class_1="8"):
    """MNIST 로드, 두 클래스 선택, 셔플, n_samples 만 반환."""
    # http://openml.org/d/554에서 데이터 로드
    mnist = fetch_openml("mnist_784", version=1, as_frame=False, parser="pandas")

    # 이진 분류를 위해 두 클래스만 선택
    mask = np.logical_or(mnist.target == class_0, mnist.target == class_1)

    X, y = shuffle(mnist.data[mask], mnist.target[mask], random_state=42)
    if n_samples is not None:
        X, y = X[:n_samples], y[:n_samples]
    return X, y

X, y = load_mnist(n_samples=10000)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
```
