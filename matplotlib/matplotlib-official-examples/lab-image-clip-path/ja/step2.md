# 画像の読み込み

サンプル画像を読み込むために、`cbook`の`get_sample_data`メソッドを使用します。このメソッドは、画像を表示するために`imshow`に渡すことができるファイルライクオブジェクトを返します。

```python
with cbook.get_sample_data('grace_hopper.jpg') as image_file:
    image = plt.imread(image_file)
```
