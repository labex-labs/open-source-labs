# 文字列が小文字かどうかをチェックするJavaScript関数

与えられた文字列が小文字かどうかをチェックするには、次のJavaScript関数を使用できます。まず、`String.prototype.toLowerCase()`を使って文字列を小文字に変換し、その後、厳密な等値比較（`===`）を使って元の文字列と比較します。

```js
const isLowerCase = (str) => str === str.toLowerCase();
```

以下は使用例です：

```js
isLowerCase("abc"); // true
isLowerCase("a3@$"); // true
isLowerCase("Ab4"); // false
```

この関数を使用するには、ターミナル/SSHを開いて`node`と入力します。
