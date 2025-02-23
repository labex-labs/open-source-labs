# 配列、オブジェクト、または文字列のサイズを取得する関数

この関数を使用するには、ターミナル/SSHを開いて`node`と入力します。この関数は、配列、オブジェクト、または文字列のサイズを取得します。

使用方法：

- `val`の型（`array`、`object`、または`string`）を判断します。
- 配列の場合は`Array.prototype.length`プロパティを使用します。
- 利用可能な場合は`length`または`size`値を使用し、オブジェクトの場合はキー数を使用します。
- 文字列の場合は、`val`から作成された[`Blob`オブジェクト](https://developer.mozilla.org/ja/docs/Web/API/Blob)の`size`を使用します。

```js
const size = (val) =>
  Array.isArray(val)
    ? val.length
    : val && typeof val === "object"
      ? val.size || val.length || Object.keys(val).length
      : typeof val === "string"
        ? new Blob([val]).size
        : 0;
```

例：

```js
size([1, 2, 3, 4, 5]); // 5
size("size"); // 4
size({ one: 1, two: 2, three: 3 }); // 3
```
