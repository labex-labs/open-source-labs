# 데이터 로드 및 준비

다음으로 데이터를 로드하고 준비합니다. scikit-learn 을 사용하여 아이리스 데이터 세트를 로드하고 두 개의 특징만 선택합니다. 그런 다음 데이터를 훈련 세트와 테스트 세트로 분할합니다.

```python
n_neighbors = 1

dataset = datasets.load_iris()
X, y = dataset.data, dataset.target

# 두 개의 특징만 사용합니다. 두 차원 데이터 세트를 사용하여 이러한 보기 흉한 슬라이싱을 피할 수 있습니다.
X = X[:, [0, 2]]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.7, random_state=42
)
```
