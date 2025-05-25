# 라이브러리 가져오기 및 데이터셋 생성

필요한 라이브러리를 가져오고 100,000 개의 샘플과 20 개의 특징을 가진 합성 이진 분류 데이터셋을 생성합니다. 20 개의 특징 중 2 개는 정보적이고, 2 개는 중복되며, 나머지 16 개는 정보가 없습니다. 100,000 개의 샘플 중 100 개는 모델 학습에 사용되고 나머지는 테스트에 사용됩니다.

```python
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# 데이터셋 생성
X, y = make_classification(
    n_samples=100_000, n_features=20, n_informative=2, n_redundant=2, random_state=42
)

train_samples = 100  # 모델 학습에 사용할 샘플 수
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    shuffle=False,
    test_size=100_000 - train_samples,
)
```
