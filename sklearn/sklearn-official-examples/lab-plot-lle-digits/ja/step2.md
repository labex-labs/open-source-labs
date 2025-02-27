# 埋め込み関数をプロットする

埋め込みをプロットするためのヘルパー関数を定義します。この関数は、埋め込みデータとプロットのタイトルを入力として受け取ります。この関数は、埋め込み上の各数字をプロットし、一群の数字に対して注釈ボックスを表示します。

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
    shown_images = np.array([[1.0, 1.0]])  # ただ大きな値
    for i in range(X.shape[0]):
        # 埋め込み上の各数字をプロットする
        # 一群の数字に対して注釈ボックスを表示する
        dist = np.sum((X[i] - shown_images) ** 2, 1)
        if np.min(dist) < 4e-3:
            # あまり近い点は表示しない
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
