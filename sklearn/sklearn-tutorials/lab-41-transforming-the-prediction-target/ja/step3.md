# ラベルエンコーディング

ラベルエンコーディングは、非数値ラベルを数値ラベルに変換するプロセスです。これは`LabelEncoder`クラスを使って達成できます。

```python
from sklearn import preprocessing

# LabelEncoderインスタンスを作成
le = preprocessing.LabelEncoder()

# 非数値ラベルのリストにLabelEncoderを適用
le.fit(["paris", "paris", "tokyo", "amsterdam"])

# LabelEncoderが学習したクラスを取得
list(le.classes_)

# 非数値ラベルのリストを数値ラベルに変換
le.transform(["tokyo", "tokyo", "paris"])

# 数値ラベルを逆変換して非数値ラベルに戻す
list(le.inverse_transform([2, 2, 1]))
```
