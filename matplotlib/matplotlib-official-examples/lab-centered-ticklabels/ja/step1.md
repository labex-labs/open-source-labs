# 金融データの読み込み

まず、Matplotlibの`cbook.get_sample_data()`関数を使ってGoogleの株価の一部の金融データを読み込む必要があります。ここでは、過去250日分のデータを使用します。

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# 一部の金融データを読み込む；Googleの株価
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
r = r[-250:]  # 過去250日分を取得する
```
