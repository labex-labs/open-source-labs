# サンプルデータの生成

3 つの独立成分からなるサンプルの混合信号を生成します。信号にノイズを加え、データを標準化します。また、3 つの独立成分を混合するための混合行列も生成します。

```python
import numpy as np
from scipy import signal

np.random.seed(0)
n_samples = 2000
time = np.linspace(0, 8, n_samples)

s1 = np.sin(2 * time)  # 信号 1: 正弦波信号
s2 = np.sign(np.sin(3 * time))  # 信号 2: 方形波信号
s3 = signal.sawtooth(2 * np.pi * time)  # 信号 3: のこぎり波信号

S = np.c_[s1, s2, s3]
S += 0.2 * np.random.normal(size=S.shape)  # ノイズを加える

S /= S.std(axis=0)  # データを標準化する
# データを混合する
A = np.array([[1, 1, 1], [0.5, 2, 1.0], [1.5, 1.0, 2.0]])  # 混合行列
X = np.dot(S, A.T)  # 観測値を生成する
```
