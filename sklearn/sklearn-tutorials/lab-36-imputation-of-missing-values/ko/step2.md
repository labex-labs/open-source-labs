# SimpleImputer 를 이용한 단변량 특징 임퓨테이션

`SimpleImputer` 클래스는 단변량 방식으로 누락된 값을 임퓨테이션하기 위한 기본 전략을 제공합니다. 누락된 값을 상수 값으로 대체하거나, 각 열의 평균, 중앙값 또는 가장 빈번한 값을 사용하여 누락된 값을 임퓨테이션하는 등 다양한 전략을 선택할 수 있습니다.

평균 전략을 고려해 보겠습니다. `SimpleImputer`의 인스턴스를 생성하고 데이터에 맞춰 학습하여 임퓨테이션 전략을 학습합니다. 그런 다음 `transform` 메서드를 사용하여 학습된 전략에 따라 누락된 값을 임퓨테이션할 수 있습니다.

```python
imp = SimpleImputer(strategy='mean')
X = [[1, 2], [np.nan, 3], [7, 6]]
imp.fit(X)
X_test = [[np.nan, 2], [6, np.nan], [7, 6]]
imputed_X_test = imp.transform(X_test)
```
