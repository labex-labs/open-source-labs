# SVM 을 이용한 분류

- 필요한 라이브러리를 가져옵니다.

```python
from sklearn import svm
```

- 학습 샘플 `X`와 클래스 레이블 `y`를 정의합니다.

```python
X = [[0, 0], [1, 1]]
y = [0, 1]
```

- `SVC` 분류기의 인스턴스를 생성하고 데이터를 맞춥니다.

```python
clf = svm.SVC()
clf.fit(X, y)
```

- 학습된 모델을 사용하여 새로운 값을 예측합니다.

```python
clf.predict([[2., 2.]])
```
