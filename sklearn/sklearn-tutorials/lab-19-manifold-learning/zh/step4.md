# 比较结果

比较不同流形学习算法的结果。可视化转换后的数据，以查看算法如何保留数据的底层结构。

```python
import matplotlib.pyplot as plt

# 创建转换后数据的散点图
plt.scatter(X_transformed[:, 0], X_transformed[:, 1], c=y)
plt.title('流形学习')
plt.xlabel('分量 1')
plt.ylabel('分量 2')
plt.show()
```
