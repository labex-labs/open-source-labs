# 3 点をクリックして三角形を定義する

このステップでは、3 点をクリックすることで三角形を定義します。これを達成するために、`ginput` 関数と `waitforbuttonpress` 関数を使用します。`ginput` 関数を使うと、マウスでプロット上の点を選択でき、`waitforbuttonpress` 関数はボタン押下イベントを待ちます。

```python
import time
import matplotlib.pyplot as plt
import numpy as np

def tellme(s):
    print(s)
    plt.title(s, fontsize=16)
    plt.draw()

plt.figure()
plt.xlim(0, 1)
plt.ylim(0, 1)

tellme('You will define a triangle, click to begin')

plt.waitforbuttonpress()

while True:
    pts = []
    while len(pts) < 3:
        tellme('Select 3 corners with mouse')
        pts = np.asarray(plt.ginput(3, timeout=-1))
        if len(pts) < 3:
            tellme('Too few points, starting over')
            time.sleep(1)  # Wait a second

    ph = plt.fill(pts[:, 0], pts[:, 1], 'r', lw=2)

    tellme('Happy? Key click for yes, mouse click for no')

    if plt.waitforbuttonpress():
        break

    # Get rid of fill
    for p in ph:
        p.remove()
```
