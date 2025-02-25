# データの保存と読み込み

Pandas は、csv、excel、hdf5 などの様々な形式でデータを保存および読み込むためのメソッドを提供します。

```python
# データを csv ファイルに保存
df.to_csv("foo.csv")

# csv ファイルからデータを読み込む
pd.read_csv("foo.csv")
```
