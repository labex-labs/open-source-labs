# 혼동 행렬 생성

scikit-learn 의 ConfusionMatrixDisplay 클래스를 사용하여 혼동 행렬을 생성할 것입니다. 혼동 행렬은 각 클래스에 대한 올바른 예측과 잘못된 예측의 수를 보여줍니다.

```python
np.set_printoptions(precision=2)
disp = ConfusionMatrixDisplay.from_estimator(
    classifier,
    X_test,
    y_test,
    display_labels=class_names,
    cmap=plt.cm.Blues,
    normalize=None,
)
```
