# 레이블 전파 (Label Propagation)

#### 레이블 전파 알고리즘 개요

레이블 전파는 준지도 그래프 추론 알고리즘의 한 유형입니다. 입력 데이터셋의 모든 항목에 대한 유사도 그래프를 구성하고, 이 그래프를 사용하여 레이블이 지정된 데이터의 레이블을 레이블이 지정되지 않은 데이터로 전파합니다. 레이블 전파는 분류 작업에 사용될 수 있으며, 커널 메서드를 지원하여 데이터를 다른 차원 공간으로 투영할 수 있습니다.

#### scikit-learn 에서 레이블 전파 사용

scikit-learn 에서는 `LabelPropagation`과 `LabelSpreading` 두 가지 레이블 전파 모델을 제공합니다. 두 모델 모두 유사도 그래프를 구성하고 레이블을 전파합니다. 레이블 전파 사용 예시는 다음과 같습니다.

```python
from sklearn.semi_supervised import LabelPropagation

# 레이블 전파 모델을 생성합니다.
label_propagation = LabelPropagation()

# 레이블이 지정된 데이터로 레이블 전파 모델을 학습시킵니다.
label_propagation.fit(X_labeled, y_labeled)

# 새로운 샘플에 대한 레이블을 예측합니다.
y_pred = label_propagation.predict(X_test)
```

위의 예에서 `X_labeled`와 `y_labeled`는 레이블이 지정된 데이터이고, `X_test`는 예측할 새로운 샘플입니다.
