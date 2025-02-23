# 与えられた関数に基づいて配列から値を抽出する方法

コーディングの練習を始めるには、ターミナル/SSH を開き、`node` と入力します。

`pullBy` 関数は、与えられた反復子関数に基づいて指定された値をフィルタリングすることで元の配列を変更します。以下がその動作方法です。

1. 最後に提供された引数が関数であるかどうかを確認します。
2. `Array.prototype.map()` を使って反復子関数 `fn` をすべての配列要素に適用します。
3. `Array.prototype.filter()` と `Array.prototype.includes()` を使って不要な値を抽出します。
4. `Array.prototype.length` を設定して、渡された配列の長さを `0` にリセットします。
5. `Array.prototype.push()` を使って、抽出された値のみで再作成します。

以下がコードです。

```js
const pullBy = (arr, ...args) => {
  const length = args.length;
  let fn = length > 1 ? args[length - 1] : undefined;
  fn = typeof fn == "function" ? (args.pop(), fn) : undefined;
  let argState = (Array.isArray(args[0]) ? args[0] : args).map((val) =>
    fn(val)
  );
  let pulled = arr.filter((v, i) => !argState.includes(fn(v)));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
};
```

そして、それを使う方法の例です。

```js
var myArray = [{ x: 1 }, { x: 2 }, { x: 3 }, { x: 1 }];
pullBy(myArray, [{ x: 1 }, { x: 3 }], (o) => o.x); // myArray = [{ x: 2 }]
```

この例では、`x` プロパティが `1` または `3` であるすべての要素を抽出しています。結果の `myArray` には、`x` プロパティが `2` である要素のみが含まれます。
