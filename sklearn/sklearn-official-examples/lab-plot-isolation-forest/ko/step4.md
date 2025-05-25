# 이산 결정 경계 시각화

`DecisionBoundaryDisplay` 클래스를 사용하여 이산 결정 경계를 시각화합니다. 배경색은 해당 영역의 샘플이 이상치로 예측되는지 여부를 나타냅니다. 산점도는 실제 레이블을 표시합니다.

```python
import matplotlib.pyplot as plt
from sklearn.inspection import DecisionBoundaryDisplay

disp = DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    response_method="predict",
    alpha=0.5,
)
disp.ax_.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor="k")
disp.ax_.set_title("IsolationForest 의 이진 결정 경계")
plt.axis("square")
plt.legend(handles=handles, labels=["이상치", "내부 데이터 포인트"], title="실제 클래스")
plt.show()
```
