# データ可視化

このステップでは、生成したデータを可視化します。

```python
import matplotlib.pyplot as plt

plt.plot(X, y, label="Expected signal")
plt.legend()
plt.xlabel("X")
_ = plt.ylabel("y")
```
