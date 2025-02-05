# 导入必要的库

我们首先需要导入生成动画所需的必要库。我们将使用 `numpy` 来生成随机数，使用 `matplotlib` 进行绘图，并使用 `FFMpegWriter` 将帧写入文件。

```python
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
```
