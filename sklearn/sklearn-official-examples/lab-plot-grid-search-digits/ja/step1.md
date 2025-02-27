# データの読み込み

digitsデータセットを読み込み、画像をベクトルにフラット化します。8×8ピクセルの各画像を64ピクセルのベクトルに変換する必要があります。これにより、形状が`(n_images, n_pixels)`の最終的なデータ配列が得られます。また、データを等しいサイズの学習用とテスト用のセットに分割します。

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

n_samples = len(digits.images)
X = digits.images.reshape((n_samples, -1))
y = digits.target == 8

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
```
