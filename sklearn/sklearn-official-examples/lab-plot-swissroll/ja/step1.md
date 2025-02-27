# スイスロールデータセットの生成

まず、`sklearn.datasets` の `make_swiss_roll()` 関数を使ってスイスロールデータセットを生成します。この関数は、渦巻き状の3次元データセットを生成します。

```python
import matplotlib.pyplot as plt
from sklearn import manifold, datasets

sr_points, sr_color = datasets.make_swiss_roll(n_samples=1500, random_state=0)
```
