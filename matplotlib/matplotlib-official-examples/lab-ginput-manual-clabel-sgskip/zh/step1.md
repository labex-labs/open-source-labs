# 通过点击三个点定义一个三角形

在这一步中，我们将通过点击三个点来定义一个三角形。我们将使用`ginput`和`waitforbuttonpress`函数来实现这一点。`ginput`函数允许我们用鼠标在绘图上选择点，而`waitforbuttonpress`函数则等待按钮按下事件。

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

tellme('你将定义一个三角形，点击开始')

plt.waitforbuttonpress()

while True:
    pts = []
    while len(pts) < 3:
        tellme('用鼠标选择 3 个角点')
        pts = np.asarray(plt.ginput(3, timeout=-1))
        if len(pts) < 3:
            tellme('点太少，重新开始')
            time.sleep(1)  # 等待一秒

    ph = plt.fill(pts[:, 0], pts[:, 1], 'r', lw=2)

    tellme('满意吗？按键点击表示是，鼠标点击表示否')

    if plt.waitforbuttonpress():
        break

    # 清除填充
    for p in ph:
        p.remove()
```
