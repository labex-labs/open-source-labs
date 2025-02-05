# 加载并显示原始图像

我们将从加载并显示颐和园的原始图像开始。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_sample_image

# 加载颐和园照片
china = load_sample_image("china.jpg")

# 显示原始图像
plt.figure()
plt.axis("off")
plt.title("原始图像")
plt.imshow(china)
plt.show()
```
