# 生成测试数据点

我们生成一组随机的测试数据点，其x和y值在 -1 到 1 之间。我们还使用步骤2中定义的 `experiment_res` 函数生成相应的一组z值。

```python
# User parameters for data test points

# Number of test data points, tested from 3 to 5000 for subdiv=3
n_test = 200

# Random points
random_gen = np.random.RandomState(seed=19680801)
x_test = random_gen.uniform(-1., 1., size=n_test)
y_test = random_gen.uniform(-1., 1., size=n_test)
z_test = experiment_res(x_test, y_test)
```
