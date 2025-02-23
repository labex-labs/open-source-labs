# 値の型をチェックする関数

提供された値が指定された型であるかどうかをチェックするには、次の手順に従います。

- `Array.prototype.includes()`を使用して、値が`undefined`または`null`でないことを確認します。
- `Object.prototype.constructor`を使用して、値のコンストラクタープロパティを指定された`type`と比較します。
- 以下の`is()`関数はこれらのチェックを行い、値が指定された型の場合に`true`を返し、それ以外の場合は`false`を返します。

```js
const is = (type, val) => ![, null].includes(val) && val.constructor === type;
```

`is()`を使用して、値が`Array`、`ArrayBuffer`、`Map`、`RegExp`、`Set`、`WeakMap`、`WeakSet`、`String`、`Number`、`Boolean`などのさまざまな型であるかどうかをチェックできます。たとえば：

```js
is(Array, [1]); // true
is(Map, new Map()); // true
is(String, ""); // true
is(Number, 1); // true
is(Boolean, true); // true
```
