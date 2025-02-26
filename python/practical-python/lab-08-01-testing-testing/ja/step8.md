# サードパーティのテストツール

組み込みの `unittest` モジュールはどこでも利用できるという利点があります。Python の一部ですからです。しかし、多くのプログラマーはこれが非常に冗長であると感じています。人気のある代替策は [pytest](https://docs.pytest.org/en/latest/) です。pytest を使うと、テストファイルは次のように簡略化されます。

```python
# test_simple.py
import simple

def test_simple():
    assert simple.add(2,2) == 4

def test_str():
    assert simple.add('hello','world') == 'helloworld'
```

テストを実行するには、`python -m pytest` のようなコマンドを入力するだけです。すると、すべてのテストを見つけて実行します。このモジュールは `pip install pytest` を使ってインストールできます。

この例だけでは `pytest` についてはまだたくさんありますが、試してみることにした場合は、通常簡単に始めることができます。

この演習では、Python の `unittest` モジュールを使う基本的な仕組みを調べます。

以前の演習では、`Stock` クラスを含む `stock.py` ファイルを書きました。この演習では、7.9 の演習で書かれた型付きプロパティを含むコードを使っていると仮定しています。何らかの理由でそれが機能しない場合は、`Solutions/7_9` のソリューションを作業ディレクトリにコピーすることができます。
