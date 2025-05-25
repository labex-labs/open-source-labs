# 데이터 생성

3 개의 정보 특징만 있는 합성 데이터 세트를 생성합니다. 정보 특징이 X 의 첫 세 열에 해당하도록 데이터 세트를 명시적으로 섞지 않습니다. 또한, 데이터 세트를 학습 및 테스트 하위 집합으로 분할합니다.

```python
X, y = make_classification(
    n_samples=1000,
    n_features=10,
    n_informative=3,
    n_redundant=0,
    n_repeated=0,
    n_classes=2,
    random_state=0,
    shuffle=False,
)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
```
