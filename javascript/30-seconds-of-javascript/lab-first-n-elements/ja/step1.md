# JavaScript で配列の最初の N 要素を取得する方法

JavaScript で配列の最初の `n` 要素を取得するには、`Array.prototype.slice()` メソッドを使うことができます。方法は次の通りです。

```js
const firstN = (arr, n) => arr.slice(0, n);
```

このコード スニペットでは、`arr` は要素を抽出したい配列を表し、`n` は抽出したい要素の数を表します。`slice()` メソッドは 2 つの引数をとります。開始インデックス（この場合 `0`）と終了インデックス（この場合 `n`）です。このメソッドは抽出された要素を含む新しい配列を返します。

`firstN()` 関数を使う方法の例を次に示します。

```js
firstN(["a", "b", "c", "d"], 2); // ['a', 'b']
```

これは `['a', 'b', 'c', 'd']` 配列の最初の 2 つの要素である `['a', 'b']` を返します。
