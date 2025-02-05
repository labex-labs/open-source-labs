# 创建一个包含两个子图的图形

首先，我们需要创建一个包含两个子图的图形。我们将使用 `plt.subplots()` 方法来创建一个有两个并排子图的图形。

```python
import matplotlib.pyplot as plt

fig, (ax, ax2) = plt.subplots(1, 2, figsize=[5.5, 2.8])
```
