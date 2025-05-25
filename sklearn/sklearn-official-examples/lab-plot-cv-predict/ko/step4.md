# 예측 오류 시각화

scikit-learn 의 `PredictionErrorDisplay`를 사용하여 예측 오류를 시각화합니다. 실제 값 대 예측 값, 그리고 잔차 대 예측 값을 플롯합니다.

```python
import matplotlib.pyplot as plt
from sklearn.metrics import PredictionErrorDisplay

fig, axs = plt.subplots(ncols=2, figsize=(8, 4))
PredictionErrorDisplay.from_predictions(
    y,
    y_pred=y_pred,
    kind="actual_vs_predicted",
    subsample=100,
    ax=axs[0],
    random_state=0,
)
axs[0].set_title("실제 값 대 예측 값")
PredictionErrorDisplay.from_predictions(
    y,
    y_pred=y_pred,
    kind="residual_vs_predicted",
    subsample=100,
    ax=axs[1],
    random_state=0,
)
axs[1].set_title("잔차 대 예측 값")
fig.suptitle("교차 검증된 예측값 플롯")
plt.tight_layout()
plt.show()
```
