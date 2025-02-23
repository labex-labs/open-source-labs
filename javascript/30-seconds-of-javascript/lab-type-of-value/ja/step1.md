# 値の型を取得する関数

値の型を取得するには、次の関数を使用します。

```js
const getType = (v) => {
  if (v === undefined) {
    return "undefined";
  }

  if (v === null) {
    return "null";
  }

  return v.constructor.name;
};
```

- 値が `undefined` または `null` の場合、関数は `'undefined'` または `'null'` を返します。
- それ以外の場合、`Object.prototype.constructor` と `Function.prototype.name` を使用してコンストラクタの名前を返します。

使用例:

```js
getType(new Set([1, 2, 3])); // 'Set'
```
