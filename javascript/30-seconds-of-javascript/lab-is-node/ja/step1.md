# 現在のランタイム環境が Node.js であるかどうかを判断する方法

現在のランタイム環境が Node.js であるかどうかを判断するには、次の手順に従います。

1. ターミナル/SSH を開きます。
2. `node` と入力します。
3. 現在の Node.js プロセスに関する情報を提供する `process` グローバルオブジェクトを使用します。
4. `process`、`process.versions`、および `process.versions.node` が定義されているかどうかを確認します。

現在のランタイム環境が Node.js であるかどうかを判断するコードは次のとおりです。

```js
const isNode = () =>
  typeof process !== "undefined" &&
  !!process.versions &&
  !!process.versions.node;
```

`isNode` 関数を呼び出すことでコードをテストできます。

```js
isNode(); // true (Node)
isNode(); // false (ブラウザ)
```
