# 创建数据

我们将为这个实验生成一个随机数据集。该数据集将有三个变量`x`、`y`和`z`。我们将把`x`和`y`定义为均值为0、标准差为0.5的正态分布随机变量。`z`同样是均值为0、标准差为0.1的正态分布。

```python
e = np.exp(1)
np.random.seed(4)

y = np.random.normal(scale=0.5, size=(30000))
x = np.random.normal(scale=0.5, size=(30000))
z = np.random.normal(scale=0.1, size=len(x))
```
