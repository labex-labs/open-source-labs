# 임베딩 함수 플롯

임베딩을 플롯하기 위한 도우미 함수를 정의합니다. 이 함수는 임베딩 데이터와 플롯 제목을 입력으로 받습니다. 함수는 임베딩 위에 각 숫자를 플롯하고, 숫자 그룹에 대한 주석 상자를 표시합니다.

```python
import numpy as np
from matplotlib import offsetbox
from sklearn.preprocessing import MinMaxScaler

def plot_embedding(X, title):
    _, ax = plt.subplots()
    X = MinMaxScaler().fit_transform(X)

    for digit in digits.target_names:
        ax.scatter(
            *X[y == digit].T,
            marker=f"${digit}$",
            s=60,
            color=plt.cm.Dark2(digit),
            alpha=0.425,
            zorder=2,
        )
    shown_images = np.array([[1.0, 1.0]])  # just something big
    for i in range(X.shape[0]):
        # 임베딩 위에 각 숫자를 플롯합니다.
        # 숫자 그룹에 대한 주석 상자를 표시합니다.
        dist = np.sum((X[i] - shown_images) ** 2, 1)
        if np.min(dist) < 4e-3:
            # 너무 가까운 점은 표시하지 않습니다.
            continue
        shown_images = np.concatenate([shown_images, [X[i]]], axis=0)
        imagebox = offsetbox.AnnotationBbox(
            offsetbox.OffsetImage(digits.images[i], cmap=plt.cm.gray_r), X[i]
        )
        imagebox.set(zorder=1)
        ax.add_artist(imagebox)

    ax.set_title(title)
    ax.axis("off")
```
