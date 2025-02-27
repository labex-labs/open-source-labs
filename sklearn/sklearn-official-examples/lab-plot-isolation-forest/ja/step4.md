# 離散的な決定境界を描画する

離散的な決定境界を可視化するために、`DecisionBoundaryDisplay`クラスを使用します。背景色は、その特定の領域内のサンプルがアウトライアと予測されるかどうかを表します。散布図は真のラベルを表示します。

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
disp.ax_.set_title("Binary decision boundary \nof IsolationForest")
plt.axis("square")
plt.legend(handles=handles, labels=["outliers", "inliers"], title="true class")
plt.show()
```
