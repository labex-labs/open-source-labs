# データを読み込む

yahoo csvデータから、mpl-data/sample_dataディレクトリにあるdate、open、high、low、close、volume、adj_closeのフィールドを持つnumpyレコード配列を読み込みます。レコード配列は、日付列に日単位('D')のnp.datetime64として日付を格納します。

```python
import matplotlib.cbook as cbook

price_data = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
price_data = price_data[-250:]  # get the most recent 250 trading days
```
