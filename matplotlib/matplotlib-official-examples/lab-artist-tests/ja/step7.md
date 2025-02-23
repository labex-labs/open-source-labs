# テキスト アーティストを作成する

次に、`matplotlib.text` の `Text` クラスを使用してテキスト アーティストを作成します。引数として x 座標と y 座標、テキスト ラベル、水平および垂直の配置、および軸オブジェクトを指定できます。

```python
t = text.Text(3, 2.5, 'text label', ha='left', va='bottom', axes=ax)
```
