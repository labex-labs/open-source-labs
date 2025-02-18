# 画像を読み込む

次に、プロット上に重ねる画像を読み込む必要があります。`matplotlib.cbook` モジュールの `get_sample_data` メソッドを使用してサンプル画像を読み込むことができます。この例では、`logo2.png` 画像を使用します。

```python
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)
```
