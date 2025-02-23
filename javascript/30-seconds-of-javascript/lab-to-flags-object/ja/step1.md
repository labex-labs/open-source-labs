# 配列をフラグオブジェクトに変換する

コーディングの練習を始めたい場合は、ターミナル/SSH を開いて `node` と入力します。

次の関数は、文字列を格納した配列を `true` にマッピングするオブジェクトに変換します。

これを行うには、`Array.prototype.reduce()` を使用します。このメソッドは配列をオブジェクトに変換し、各配列値をキーとして値を `true` に設定します。

```js
const flags = (arr) => arr.reduce((acc, str) => ({ ...acc, [str]: true }), {});
```

以下は例です。

```js
flags(["red", "green"]); // { red: true, green: true }
```
