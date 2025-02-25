# データを読み込む

次に、プロットしたいデータを読み込みます。`mpl-data/sample_data` ディレクトリからの Yahoo csv データの numpy レコード配列を使用します。このレコード配列は、日付列に日単位 ('D') の np.datetime64 として日付を格納しています。

```python
data = cbook.get_sample_data('goog.npz')['price_data']
```
