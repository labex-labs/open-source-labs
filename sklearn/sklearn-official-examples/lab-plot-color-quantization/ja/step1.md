# 元の画像を読み込んで表示する

まず、頤和園の元の画像を読み込んで表示します。

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_sample_image

# 頤和園の写真を読み込む
china = load_sample_image("china.jpg")

# 元の画像を表示する
plt.figure()
plt.axis("off")
plt.title("Original Image")
plt.imshow(china)
plt.show()
```
