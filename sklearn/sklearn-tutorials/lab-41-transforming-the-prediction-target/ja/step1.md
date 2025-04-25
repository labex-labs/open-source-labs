# ラベル 2 値化

ラベル 2 値化は、多クラスラベルを 2 値インジケータ行列に変換するプロセスです。`LabelBinarizer`クラスを使って達成できます。

```python
from sklearn import preprocessing

# LabelBinarizer インスタンスを作成
lb = preprocessing.LabelBinarizer()

# 多クラスラベルのリストに LabelBinarizer を適用
lb.fit([1, 2, 6, 4, 2])

# LabelBinarizer が学習したクラスを取得
lb.classes_

# 多クラスラベルのリストを 2 値インジケータ行列に変換
lb.transform([1, 6])
```
