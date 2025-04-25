# オブジェクトを逆にする関数

元のオブジェクトを変更することなく、オブジェクトのキーと値のペアを逆にするには、`invertKeyValues` 関数を使用します。

- ターミナル/SSH で `invertKeyValues(obj, fn)` と入力することで関数を呼び出します。ここで、`obj` は逆にするオブジェクトで、`fn` は逆にしたキーに適用するオプショナルな関数です。

- `Object.keys()` と `Array.prototype.reduce()` メソッドを使用して、逆にしたキーと値のペアを持つ新しいオブジェクトを作成します。関数が提供されている場合、それは各逆にしたキーに適用されます。

- `fn` を省略した場合、関数は何も適用されずに逆にしたキーのみを返します。

- 関数は、各逆にした値が逆にした値を生成するためのキーの配列であるオブジェクトを返します。

```js
const invertKeyValues = (obj, fn) =>
  Object.keys(obj).reduce((acc, key) => {
    const val = fn ? fn(obj[key]) : obj[key];
    acc[val] = acc[val] || [];
    acc[val].push(key);
    return acc;
  }, {});
```

使用例：

```js
invertKeyValues({ a: 1, b: 2, c: 1 }); // { 1: [ 'a', 'c' ], 2: [ 'b' ] }
invertKeyValues({ a: 1, b: 2, c: 1 }, (value) => "group" + value);
// { group1: [ 'a', 'c' ], group2: [ 'b' ] }
```
