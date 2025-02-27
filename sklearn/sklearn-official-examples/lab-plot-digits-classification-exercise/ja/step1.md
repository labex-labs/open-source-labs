# Digitsデータセットを読み込む

scikit-learnの`load_digits`関数を使ってDigitsデータセットを読み込みます。この関数は2つの配列を返します。入力データを含む`X_digits`とターゲットラベルを含む`y_digits`です。

```python
from sklearn import datasets

X_digits, y_digits = datasets.load_digits(return_X_y=True)
```
