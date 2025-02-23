# データ生成関数を作成する

次に、アニメーション用のデータを生成する関数を作成する必要があります。この関数は、時間とともに減衰するサイン波を生成します。`itertools.count()`関数を使って、無限の数のシーケンスを生成します。これらの数を使って、サイン波の値を計算します。

```python
def data_gen():
    for cnt in itertools.count():
        t = cnt / 10
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
```
