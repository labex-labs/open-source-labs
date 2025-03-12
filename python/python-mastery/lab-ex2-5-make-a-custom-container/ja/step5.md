# スライシングに対応したカスタムコンテナの拡張

私たちのカスタムコンテナは個々のレコードへのアクセスには便利です。しかし、スライシングに関しては問題があります。カスタムコンテナをスライスしようとすると、結果は通常期待するものと異なります。

これが起こる理由を理解しましょう。Python では、スライシングはシーケンスの一部を抽出するためによく使われる操作です。しかし、私たちのカスタムコンテナの場合、Python はスライスされたデータだけを持つ新しい `RideData` オブジェクトを作成する方法を知りません。その代わり、スライス内の各インデックスに対して `__getitem__` を呼び出した結果を含むリストを作成します。

1. Python シェルでスライシングをテストしましょう。

```python
import readrides

rows = readrides.read_rides_as_dicts('ctabus.csv')
r = rows[0:10]  # Take a slice of the first 10 records
type(r)  # This will likely be a list, not a RideData object
print(r)  # This might look like a list of numbers, not dictionaries
```

このコードでは、まず `readrides` モジュールをインポートします。次に、`ctabus.csv` ファイルからデータを読み込み、`rows` 変数に格納します。最初の 10 レコードをスライスして結果の型を確認すると、`RideData` オブジェクトではなくリストになっていることがわかります。結果を出力すると、辞書ではなく数値のリストのように見えるかもしれません。

2. `RideData` クラスを修正して、スライシングを適切に処理できるようにしましょう。`readrides.py` を開き、`__getitem__` メソッドを更新します。

```python
def __getitem__(self, index):
    if isinstance(index, slice):
        # Handle slice
        result = RideData()
        result.routes = self.routes[index]
        result.dates = self.dates[index]
        result.daytypes = self.daytypes[index]
        result.numrides = self.numrides[index]
        return result
    else:
        # Handle single index
        return {'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]}
```

この更新された `__getitem__` メソッドでは、まず `index` がスライスかどうかを確認します。スライスであれば、`result` という名前の新しい `RideData` オブジェクトを作成します。そして、元のデータ列 (`routes`、`dates`、`daytypes`、`numrides`) のスライスでこの新しいオブジェクトを埋めます。これにより、カスタムコンテナをスライスすると、リストではなく別の `RideData` オブジェクトが得られます。`index` がスライスでない場合（つまり、単一のインデックスである場合）、関連するレコードを含む辞書を返します。

3. 改善されたスライシング機能をテストしましょう。

```python
import readrides

rows = readrides.read_rides_as_dicts('ctabus.csv')
r = rows[0:10]  # Take a slice of the first 10 records
type(r)  # Should now be readrides.RideData
len(r)   # Should be 10
r[0]     # Should be the same as rows[0]
r[1]     # Should be the same as rows[1]
```

`__getitem__` メソッドを更新した後、再度スライシングをテストできます。最初の 10 レコードをスライスすると、結果の型は `readrides.RideData` になるはずです。スライスの長さは 10 で、スライス内の個々の要素にアクセスすると、元のコンテナ内の対応する要素にアクセスした場合と同じ結果が得られるはずです。

4. 異なるスライスパターンでもテストできます。

```python
# Get every other record from the first 20
r2 = rows[0:20:2]
len(r2)  # Should be 10

# Get the last 10 records
r3 = rows[-10:]
len(r3)  # Should be 10
```

ここでは、異なるスライスパターンをテストしています。最初のスライス `rows[0:20:2]` は最初の 20 レコードから 1 つおきのレコードを取得し、結果のスライスの長さは 10 であるはずです。2 番目のスライス `rows[-10:]` は最後の 10 レコードを取得し、その長さも 10 であるはずです。

スライシングを適切に実装することで、私たちのカスタムコンテナは標準の Python リストにさらに似た動作をするようになり、同時に列指向ストレージのメモリ効率を維持します。

このように、Python の組み込みコンテナを模倣しながらも内部表現が異なるカスタムコンテナクラスを作成するアプローチは、コードがユーザーに提示するインターフェースを変更せずにメモリ使用量を最適化する強力な手法です。
