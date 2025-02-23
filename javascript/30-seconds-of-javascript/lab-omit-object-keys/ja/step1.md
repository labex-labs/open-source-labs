# オブジェクトからキーを削除する

オブジェクトから特定のキーを削除するには、削除するオブジェクトとキーの配列を引数にとる `omit` 関数を使います。

- `Object.keys()` メソッドを使ってオブジェクトのすべてのキーを取得します。
- 次に、`Array.prototype.filter()` メソッドを使ってキーのリストから指定されたキーを削除します。
- 最後に、`Array.prototype.reduce()` を使って残ったキーと値のペアで新しいオブジェクトを作成します。

```js
const omit = (obj, keysToRemove) =>
  Object.keys(obj)
    .filter((key) => !keysToRemove.includes(key))
    .reduce((newObj, key) => {
      newObj[key] = obj[key];
      return newObj;
    }, {});
```

使用例:

```js
omit({ a: 1, b: "2", c: 3 }, ["b"]); // { 'a': 1, 'c': 3 }
```
