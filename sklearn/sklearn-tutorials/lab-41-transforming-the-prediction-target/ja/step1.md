# ラベル2値化

ラベル2値化は、多クラスラベルを2値インジケータ行列に変換するプロセスです。`LabelBinarizer`クラスを使って達成できます。

```python
from sklearn import preprocessing

# LabelBinarizerインスタンスを作成
lb = preprocessing.LabelBinarizer()

# 多クラスラベルのリストにLabelBinarizerを適用
lb.fit([1, 2, 6, 4, 2])

# LabelBinarizerが学習したクラスを取得
lb.classes_

# 多クラスラベルのリストを2値インジケータ行列に変換
lb.transform([1, 6])
```
