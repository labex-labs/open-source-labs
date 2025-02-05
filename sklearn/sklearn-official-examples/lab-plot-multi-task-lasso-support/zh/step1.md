# 生成数据

首先，我们需要生成一些示例数据，用于拟合我们的模型。我们将使用numpy生成100个样本，每个样本有30个特征和40个任务。我们还将随机选择5个相关特征，并使用具有随机频率和相位的正弦波为它们创建系数。最后，我们将向数据中添加一些随机噪声。

```python
import numpy as np

rng = np.random.RandomState(42)

# Generate some 2D coefficients with sine waves with random frequency and phase
n_samples, n_features, n_tasks = 100, 30, 40
n_relevant_features = 5
coef = np.zeros((n_tasks, n_features))
times = np.linspace(0, 2 * np.pi, n_tasks)
for k in range(n_relevant_features):
    coef[:, k] = np.sin((1.0 + rng.randn(1)) * times + 3 * rng.randn(1))

X = rng.randn(n_samples, n_features)
Y = np.dot(X, coef.T) + rng.randn(n_samples, n_tasks)
```
