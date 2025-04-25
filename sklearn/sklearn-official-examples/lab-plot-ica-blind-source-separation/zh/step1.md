# 生成示例数据

我们将生成一个由三个独立成分组成的示例混合信号。我们会给信号添加噪声并对数据进行标准化处理。我们还将生成一个混合矩阵来混合这三个独立成分。

```python
import numpy as np
from scipy import signal

np.random.seed(0)
n_samples = 2000
time = np.linspace(0, 8, n_samples)

s1 = np.sin(2 * time)  # 信号 1：正弦信号
s2 = np.sign(np.sin(3 * time))  # 信号 2：方波信号
s3 = signal.sawtooth(2 * np.pi * time)  # 信号 3：锯齿波信号

S = np.c_[s1, s2, s3]
S += 0.2 * np.random.normal(size=S.shape)  # 添加噪声

S /= S.std(axis=0)  # 标准化数据
# 混合数据
A = np.array([[1, 1, 1], [0.5, 2, 1.0], [1.5, 1.0, 2.0]])  # 混合矩阵
X = np.dot(S, A.T)  # 生成观测值
```
