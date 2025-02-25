# PyArrow を使ったデータの読み込み

PyArrow は、いくつかの pandas IO リーダーに統合されている IO 読み込み機能を提供しています。

```python
# IO モジュールをインポート
import io

# StringIO オブジェクトを作成
data = io.StringIO("""a,b,c\n1,2.5,True\n3,4.5,False""")

# エンジンとして PyArrow を使ってデータを pandas の DataFrame に読み込む
df = pd.read_csv(data, engine="pyarrow")
```
