# ConfusionMatrixDisplay 생성

학습된 모델을 사용하여 테스트 데이터셋에 대한 모델 예측값을 계산합니다. 이 예측값은 `ConfusionMatrixDisplay`를 사용하여 혼동 행렬을 계산하고 시각화하는 데 사용됩니다.

```python
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

y_pred = clf.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

cm_display = ConfusionMatrixDisplay(cm).plot()
```
