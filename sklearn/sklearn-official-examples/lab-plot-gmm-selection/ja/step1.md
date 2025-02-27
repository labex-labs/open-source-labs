# データ生成

`numpy.random.randn` によって返される標準正規分布をランダムサンプリングすることで、2 つのコンポーネント（それぞれ `n_samples` 個含む）を生成します。一方のコンポーネントは球形を保ちながらシフトさせ、再スケーリングします。もう一方は、より一般的な共分散行列を持つように変形させます。

```python
import numpy as np

n_samples = 500
np.random.seed(0)
C = np.array([[0.0, -0.1], [1.7, 0.4]])
component_1 = np.dot(np.random.randn(n_samples, 2), C)  # general
component_2 = 0.7 * np.random.randn(n_samples, 2) + np.array([-4, 1])  # spherical

X = np.concatenate([component_1, component_2])
```
