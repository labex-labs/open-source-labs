# 准备数据

我们首先定义一个我们想要逼近的函数，并准备绘制它。

```python
def f(x):
    """Function to be approximated by polynomial interpolation."""
    return x * np.sin(x)

# 我们想要绘制的整个范围
x_plot = np.linspace(-1, 11, 100)

# 为了使情况更有趣，我们只给出一小部分点用于训练。
x_train = np.linspace(0, 10, 100)
rng = np.random.RandomState(0)
x_train = np.sort(rng.choice(x_train, size=20, replace=False))
y_train = f(x_train)

# 创建这些数组的二维数组版本，以便输入到变换器中
X_train = x_train[:, np.newaxis]
X_plot = x_plot[:, np.newaxis]
```
