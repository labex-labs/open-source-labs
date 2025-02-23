# JavaScript における 2 次元配列の初期化

JavaScript において 2 次元配列を初期化するには、次のコードを使用できます。

```js
const initialize2DArray = (width, height, value = null) => {
  return Array.from({ length: height }).map(() =>
    Array.from({ length: width }).fill(value)
  );
};
```

このコードは、`Array.from()` と `Array.prototype.map()` を使用して、`height` 行の配列を作成します。その各行は、`width` の長さの新しい配列です。また、`Array.prototype.fill()` を使用して、配列内のすべての要素を `value` パラメータに設定します。`value` が提供されない場合、既定値は `null` になります。

この関数を次のように呼び出すことができます。

```js
initialize2DArray(2, 2, 0); // [[0, 0], [0, 0]]
```

これにより、幅が 2、高さが 2、すべての値が 0 に設定された 2 次元配列が作成されます。
