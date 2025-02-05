# 评估特征重要性

我们基于杂质平均减少量（MDI）来评估特征重要性。特征重要性由拟合属性 `feature_importances_` 提供，它们是通过计算每棵树内杂质减少量累积的均值和标准差得到的。

```python
import time
import matplotlib.pyplot as plt

start_time = time.time()
img_shape = data.images[0].shape
importances = forest.feature_importances_
elapsed_time = time.time() - start_time

print(f"计算重要性所花费的时间: {elapsed_time:.3f} 秒")
imp_reshaped = importances.reshape(img_shape)
plt.matshow(imp_reshaped, cmap=plt.cm.hot)
plt.title("使用杂质值的像素重要性")
plt.colorbar()
plt.show()
```
