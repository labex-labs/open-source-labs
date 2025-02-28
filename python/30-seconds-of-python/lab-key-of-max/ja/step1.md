# 基本関数の作成

まずは関数の核心部分を作成しましょう。段階的に構築していきます。最初に、`key_of_max.py` という名前のファイルを作成します。LabEx の組み込みコードエディタを使用するか、`nano` や `vim` のようなターミナルベースのエディタを使用することができます。`key_of_max.py` の中に、以下のコードを追加します。

![key_of_max 関数があるコードエディタ](../assets/20250214-14-44-53-838b9T58.png)

```python
def key_of_max(d):
  """
  辞書 'd' 内の最大値に関連付けられたキーを返します。

  複数のキーが最大値を共有する場合、そのいずれかが返されます。
  """
  return max(d, key=d.get)
```

これを詳しく見ていきましょう。

- **`def key_of_max(d):`**: これは `key_of_max` という名前の関数を定義しています。この関数は 1 つの引数 `d` を受け取り、これは操作対象の辞書を表します。
- **`return max(d, key=d.get)`**: これが関数の核心部分です。少しずつ分析してみましょう。
  - **`max(d,...)`**: 組み込みの `max()` 関数は最大の要素を見つけます。デフォルトでは、`max()` に辞書を渡すと、最大の _キー_（アルファベット順）を見つけます。しかし、私たちは最大の _値_ に _関連付けられた_ キーを求めています。
  - **`key=d.get`**: これが重要な部分です。`key` 引数は `max()` に要素の比較方法を指示します。`d.get` は辞書のメソッドです。`d.get(some_key)` を呼び出すと、`some_key` に関連付けられた _値_ が返されます。`key=d.get` と設定することで、`max()` に「辞書 `d` の要素を _値_ で比較し、キーではなく比較してください」と指示しています。その結果、`max()` 関数は最大値に対応する _キー_ を返します。
