# 引数のコアレス（coalesce）ファクトリコード

コーディングを始めるには、ターミナル/SSH を開いて `node` と入力します。この関数は、引数として渡された検証関数に基づいて最初の `true` と評価される引数を返します。

```js
const coalesceFactory =
  (validator) =>
  (...args) =>
    args.find(validator);
```

提供された引数検証関数 `valid` から最初の `true` を返す引数を返すために、`Array.prototype.find()` を使用します。たとえば、

```js
const customCoalesce = coalesceFactory(
  (v) => ![null, undefined, "", NaN].includes(v)
);
customCoalesce(undefined, null, NaN, "", "Waldo"); // 'Waldo'
```

ここでは、`coalesceFactory` 関数がカスタマイズされて `customCoalesce` 関数が作成されています。`customCoalesce` 関数は、提供された引数から `null`、`undefined`、`NaN`、および空の文字列をフィルタリングし、フィルタリングされなかった最初の引数を返します。`customCoalesce(undefined, null, NaN, '', 'Waldo')` の出力は `'Waldo'` です。
