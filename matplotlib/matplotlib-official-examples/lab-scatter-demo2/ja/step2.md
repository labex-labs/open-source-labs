# データを読み込む

yahoo csv データから、mpl-data/sample_data ディレクトリにある date、open、high、low、close、volume、adj_close のフィールドを持つ numpy レコード配列を読み込みます。レコード配列は、日付列に日単位 ('D') の np.datetime64 として日付を格納します。

```python
import matplotlib.cbook as cbook

price_data = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
price_data = price_data[-250:]  # get the most recent 250 trading days
```
