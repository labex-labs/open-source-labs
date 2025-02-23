# JavaScriptオブジェクトにキーがあるかどうかを確認する関数

JavaScriptオブジェクト内に対象の値が存在するかどうかを確認するには、`hasKey`関数を使用します。

この関数には2つの引数が必要です。探索対象のJSONオブジェクト`obj`と、確認するキーの配列`keys`です。オブジェクトに指定されたキーがあるかどうかを確認する手順は以下の通りです。

1. `keys`配列が空でないことを確認します。空の場合は`false`を返します。
2. `Array.prototype.every()`メソッドを使用して、`keys`配列を反復処理し、`obj`の内部の深さまで各キーを順次確認します。
3. `Object.prototype.hasOwnProperty()`メソッドを使用して、`obj`に現在のキーがないか、またはオブジェクトでないことを確認します。これらの条件のいずれかがtrueの場合、処理を中止して`false`を返します。
4. それ以外の場合は、次の反復処理で使用するために、キーの値を`obj`に代入します。
5. `keys`配列が正常に反復処理された場合は、`true`を返します。

以下が`hasKey`関数のコードです。

```js
const hasKey = (obj, keys) => {
  return (
    keys.length > 0 &&
    keys.every((key) => {
      if (typeof obj !== "object" || !obj.hasOwnProperty(key)) return false;
      obj = obj[key];
      return true;
    })
  );
};
```

`hasKey`関数の使用例をいくつか示します。

```js
let obj = {
  a: 1,
  b: { c: 4 },
  "b.d": 5
};

hasKey(obj, ["a"]); // true
hasKey(obj, ["b"]); // true
hasKey(obj, ["b", "c"]); // true
hasKey(obj, ["b.d"]); // true
hasKey(obj, ["d"]); // false
hasKey(obj, ["c"]); // false
hasKey(obj, ["b", "f"]); // false
```
