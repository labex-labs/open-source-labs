# オブジェクトの内部辞書の探索

Python において、オブジェクトは基本的な概念です。オブジェクトは、データを保持し、特定の振る舞いを持つコンテナと考えることができます。Python のオブジェクトの興味深い側面の 1 つは、属性をどのように格納するかです。属性は、オブジェクトに属する変数のようなものです。Python はこれらの属性を特殊な辞書に格納しており、この辞書は `__dict__` 属性を通じてアクセスできます。この辞書はオブジェクトの内部部分であり、Python はそのオブジェクトに関連するすべてのデータをここに管理しています。

`SimpleStock` のインスタンスを使って、この内部構造を詳しく見てみましょう。Python では、インスタンスはクラスから作成された個々のオブジェクトです。たとえば、`SimpleStock` がクラスである場合、`goog` と `ibm` はそのクラスのインスタンスです。

これらのインスタンスの内部辞書を見るには、Python の対話型シェルを使用できます。Python の対話型シェルは、コードをすぐにテストして結果を確認するのに便利なツールです。Python の対話型シェルで、以下のコマンドを入力して、インスタンスの `__dict__` 属性を調べましょう。

```python
>>> goog.__dict__
{'name': 'GOOG', 'shares': 100, 'price': 490.1}
>>> ibm.__dict__
{'name': 'IBM', 'shares': 50, 'price': 91.23}
```

これらのコマンドを実行すると、出力結果から各インスタンスが独自の内部辞書を持っていることがわかります。この辞書には、すべてのインスタンス属性が含まれています。たとえば、`goog` インスタンスでは、属性 `name`、`shares`、`price` がそれぞれの値とともに辞書に格納されています。これが、Python がオブジェクト属性を内部的に実装する方法です。すべてのオブジェクトは、そのすべての属性を保持するプライベートな辞書を持っています。

`__dict__` 属性がオブジェクトの内部実装について明らかにすることを理解することは重要です。

1. 辞書のキーは属性名に対応しています。たとえば、`goog` インスタンスでは、キー `'name'` はオブジェクトの `name` 属性に対応しています。
2. 辞書の値は属性値です。したがって、値 `'GOOG'` は `goog` インスタンスの `name` 属性の値です。
3. 各インスタンスは独自の `__dict__` を持っています。これは、あるインスタンスの属性が他のインスタンスの属性とは独立していることを意味します。たとえば、`goog` インスタンスの `shares` 属性は、`ibm` インスタンスの `shares` 属性と異なる値を持つことができます。

この辞書ベースのアプローチにより、Python はオブジェクトに対して非常に柔軟に対応できます。次のステップで見るように、この柔軟性を利用して、様々な方法でオブジェクト属性を変更およびアクセスすることができます。
