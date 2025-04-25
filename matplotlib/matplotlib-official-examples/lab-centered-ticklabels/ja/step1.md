# 金融データの読み込み

まず、Matplotlib の`cbook.get_sample_data()`関数を使って Google の株価の一部の金融データを読み込む必要があります。ここでは、過去 250 日分のデータを使用します。

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# 一部の金融データを読み込む；Google の株価
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
r = r[-250:]  # 過去 250 日分を取得する
```
