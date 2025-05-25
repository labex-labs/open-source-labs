# 주성분 분석 (PCA) 차원 축소에 대한 스케일링 효과

주성분 분석 (PCA) 을 사용하여 와인 데이터셋의 차원을 축소합니다. 스케일링되지 않은 데이터에 PCA 를 적용한 주성분과 먼저 StandardScaler 를 사용하여 데이터를 스케일링한 후 PCA 를 적용한 주성분을 비교합니다.

```python
import pandas as pd
from sklearn.decomposition import PCA

pca = PCA(n_components=2).fit(X_train)
scaled_pca = PCA(n_components=2).fit(scaled_X_train)
X_train_transformed = pca.transform(X_train)
X_train_std_transformed = scaled_pca.transform(scaled_X_train)

first_pca_component = pd.DataFrame(
    pca.components_[0], index=X.columns, columns=["without scaling"]
)
first_pca_component["with scaling"] = scaled_pca.components_[0]
first_pca_component.plot.bar(
    title="첫 번째 주성분의 가중치", figsize=(6, 8)
)

_ = plt.tight_layout()

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

target_classes = range(0, 3)
colors = ("blue", "red", "green")
markers = ("^", "s", "o")

for target_class, color, marker in zip(target_classes, colors, markers):
    ax1.scatter(
        x=X_train_transformed[y_train == target_class, 0],
        y=X_train_transformed[y_train == target_class, 1],
        color=color,
        label=f"class {target_class}",
        alpha=0.5,
        marker=marker,
    )

    ax2.scatter(
        x=X_train_std_transformed[y_train == target_class, 0],
        y=X_train_std_transformed[y_train == target_class, 1],
        color=color,
        label=f"class {target_class}",
        alpha=0.5,
        marker=marker,
    )

ax1.set_title("스케일링되지 않은 학습 데이터셋의 PCA 후")
ax2.set_title("표준화된 학습 데이터셋의 PCA 후")

for ax in (ax1, ax2):
    ax.set_xlabel("첫 번째 주성분")
    ax.set_ylabel("두 번째 주성분")
    ax.legend(loc="upper right")
    ax.grid()

_ = plt.tight_layout()
```
