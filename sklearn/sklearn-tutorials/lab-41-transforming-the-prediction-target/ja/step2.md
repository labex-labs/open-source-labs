# マルチラベル 2 値化

マルチラベル 2 値化は、ラベルのコレクションのコレクションをインジケータ形式に変換するプロセスです。これは`MultiLabelBinarizer`クラスを使って達成できます。

```python
from sklearn.preprocessing import MultiLabelBinarizer

# ラベルのコレクションのリストを定義
y = [[2, 3, 4], [2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2]]

# MultiLabelBinarizer インスタンスを作成し、コレクションのリストに fit_transform を適用
MultiLabelBinarizer().fit_transform(y)
```
