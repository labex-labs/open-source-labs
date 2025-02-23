# 配列をコンパクトに結合する方法のヒント

コーディングを練習するには、ターミナル/SSH を開いて `node` と入力します。

以下は、配列から偽の値を削除し、残りの値を文字列に結合する方法です：

- `Array.prototype.filter()` を使って、`false`、`null`、`0`、`""`、`undefined`、`NaN` などの偽の値をフィルタリングします。
- `Array.prototype.join()` を使って、残りの値を文字列に結合します。

```js
const compactJoin = (arr, delim = ",") => arr.filter(Boolean).join(delim);
```

そして、関数を呼び出して、配列を引数として渡します：

```js
compactJoin(["a", "", "b", "c"]); // 'a,b,c'
```
