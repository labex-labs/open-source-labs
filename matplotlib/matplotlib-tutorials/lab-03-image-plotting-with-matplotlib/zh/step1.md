# 导入图像数据

首先，我们需要导入必要的库，并将图像数据加载到 NumPy 数组中。在我们的例子中，我们将使用 `PIL` 库来加载图像，然后将其转换为 NumPy 数组。

```python
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = np.asarray(Image.open('./stinkbug.png'))
```
