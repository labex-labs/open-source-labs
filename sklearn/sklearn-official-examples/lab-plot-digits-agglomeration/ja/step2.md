# データセットの読み込み

このステップでは、scikit-learnから手書き数字のデータセットを読み込みます。このデータセットには、0から9までの手書き数字の画像が含まれています。

```python
digits = datasets.load_digits()
images = digits.images
X = np.reshape(images, (len(images), -1))
```
