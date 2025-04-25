# データの生成

まず、Scikit-learn の`make_swiss_roll`関数を使ってスイスロールデータセットを生成します。スイスロールデータセットは、渦巻き形状の 3 次元データセットです。

```python
from sklearn.datasets import make_swiss_roll

n_samples = 1500
noise = 0.05
X, _ = make_swiss_roll(n_samples, noise=noise)
# Make it thinner
X[:, 1] *= 0.5
```
