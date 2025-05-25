# k-최근접 이웃 모델에 대한 스케일링 효과

와인 데이터셋에서 두 개의 특징을 추출하여 K-최근접 이웃 분류기를 학습합니다. 스케일링된 데이터와 스케일링되지 않은 데이터를 사용하여 분류기의 결정 경계를 시각화합니다.

```python
import matplotlib.pyplot as plt
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.neighbors import KNeighborsClassifier

X_plot = X[["proline", "hue"]]
X_plot_scaled = scaler.fit_transform(X_plot)
clf = KNeighborsClassifier(n_neighbors=20)

def fit_and_plot_model(X_plot, y, clf, ax):
    clf.fit(X_plot, y)
    disp = DecisionBoundaryDisplay.from_estimator(
        clf,
        X_plot,
        response_method="predict",
        alpha=0.5,
        ax=ax,
    )
    disp.ax_.scatter(X_plot["proline"], X_plot["hue"], c=y, s=20, edgecolor="k")
    disp.ax_.set_xlim((X_plot["proline"].min(), X_plot["proline"].max()))
    disp.ax_.set_ylim((X_plot["hue"].min(), X_plot["hue"].max()))
    return disp.ax_

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 6))

fit_and_plot_model(X_plot, y, clf, ax1)
ax1.set_title("스케일링 없이 KNN")

fit_and_plot_model(X_plot_scaled, y, clf, ax2)
ax2.set_xlabel("스케일링된 proline")
ax2.set_ylabel("스케일링된 hue")
_ = ax2.set_title("스케일링된 KNN")
```
