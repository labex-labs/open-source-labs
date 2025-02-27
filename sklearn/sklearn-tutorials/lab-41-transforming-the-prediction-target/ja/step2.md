# マルチラベル2値化

マルチラベル2値化は、ラベルのコレクションのコレクションをインジケータ形式に変換するプロセスです。これは`MultiLabelBinarizer`クラスを使って達成できます。

```python
from sklearn.preprocessing import MultiLabelBinarizer

# ラベルのコレクションのリストを定義
y = [[2, 3, 4], [2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2]]

# MultiLabelBinarizerインスタンスを作成し、コレクションのリストにfit_transformを適用
MultiLabelBinarizer().fit_transform(y)
```
