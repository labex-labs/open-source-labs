# データセットの読み込みとデータの分割

まず、Scikit-Learn ライブラリを使って digits データセットを読み込みます。このデータセットは、0 から 9 までの数字の 8x8 画像で構成されています。各画像は 64 個の特徴の配列として表されます。データを特徴量と目的変数に分割します。

```python
from sklearn.datasets import load_digits
digits = load_digits()
X = digits.images.reshape((len(digits.images), -1))
y = digits.target
```
