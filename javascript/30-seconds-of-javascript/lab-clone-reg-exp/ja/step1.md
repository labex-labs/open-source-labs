# 正規表現のクローン作成

正規表現をクローンするには、`RegExp` コンストラクター、`RegExp.prototype.source`、および `RegExp.prototype.flags` を使用します。

```js
const cloneRegExp = (regExp) => new RegExp(regExp.source, regExp.flags);
```

このコードは、与えられた正規表現のクローンを作成します。たとえば：

```js
const regExp = /lorem ipsum/gi;
const regExp2 = cloneRegExp(regExp); // regExp!== regExp2
```
