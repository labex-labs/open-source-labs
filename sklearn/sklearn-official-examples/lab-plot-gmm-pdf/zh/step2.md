# 生成数据

接下来，我们将生成一个包含两个组件的高斯混合数据集。我们将创建一个以 (20, 20) 为中心的平移高斯数据集和一个零中心拉伸高斯数据集。然后，我们将把这两个数据集连接成最终的训练集。

```python
n_samples = 300

# 生成随机样本，两个组件
np.random.seed(0)

# 生成以 (20, 20) 为中心的球形数据
shifted_gaussian = np.random.randn(n_samples, 2) + np.array([20, 20])

# 生成零中心拉伸高斯数据
C = np.array([[0.0, -0.7], [3.5, 0.7]])
stretched_gaussian = np.dot(np.random.randn(n_samples, 2), C)

# 将两个数据集连接成最终的训练集
X_train = np.vstack([shifted_gaussian, stretched_gaussian])
```
