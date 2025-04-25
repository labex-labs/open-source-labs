# 必要なライブラリとデータのインポート

まず、必要なライブラリである`matplotlib`、`numpy`、および`matplotlib.cbook`をインポートする必要があります。また、`mpl-data/sample_data`ディレクトリから、日付、始値、高値、安値、終値、出来高、調整後終値のフィールドを持つ yahoo csv データから numpy レコード配列を読み込む必要があります。レコード配列は、日付列に日単位 ('D') の np.datetime64 として日付を格納します。このデータを使って金融時系列をプロットします。

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# Load data from sample_data directory
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
r = r[:9]  # get the first 9 days
```
