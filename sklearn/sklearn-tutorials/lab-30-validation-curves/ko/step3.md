# 검증 곡선 플롯

이제 `validation_curve` 함수를 사용하여 검증 곡선을 플롯해 보겠습니다. `Ridge` 추정기를 사용하고 `alpha` 하이퍼파라미터를 다양한 값 범위에서 변경할 것입니다.

```python
param_range = np.logspace(-7, 3, 3)
train_scores, valid_scores = validation_curve(
    Ridge(), X, y, param_name="alpha", param_range=param_range, cv=5)
```
