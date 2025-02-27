# 特徴量の重要度を評価する

不純度の平均減少量 (MDI) に基づいて特徴量の重要度を評価します。特徴量の重要度は、フィッティングされた属性 `feature_importances_` によって提供され、各木内の不純度の減少の累積の平均と標準偏差として計算されます。

```python
import time
import matplotlib.pyplot as plt

start_time = time.time()
img_shape = data.images[0].shape
importances = forest.feature_importances_
elapsed_time = time.time() - start_time

print(f"Elapsed time to compute the importances: {elapsed_time:.3f} seconds")
imp_reshaped = importances.reshape(img_shape)
plt.matshow(imp_reshaped, cmap=plt.cm.hot)
plt.title("Pixel importances using impurity values")
plt.colorbar()
plt.show()
```
