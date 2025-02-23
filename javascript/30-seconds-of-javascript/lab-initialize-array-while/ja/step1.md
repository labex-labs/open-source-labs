# JavaScript で while ループを使って配列を初期化して埋める方法

JavaScript でコーディングを練習するには、ターミナル/SSH を開いて `node` と入力します。

`initializeArrayWhile` 関数は、条件が満たされている間、関数で生成された値で配列を初期化して埋めます。以下がその動作方法です。

1. `arr` という空の配列、`i` というインデックス変数、`el` という要素を作成します。
2. `conditionFn` 関数が与えられたインデックス `i` と要素 `el` に対して `true` を返す限り、`while` ループを使って `mapFn` 関数を使って配列に要素を追加します。
3. `conditionFn` 関数は3つの引数を取ります。現在のインデックス、前の要素、配列自体。
4. `mapFn` 関数は3つの引数を取ります。現在のインデックス、現在の要素、配列自体。
5. `initializeArrayWhile` 関数は配列を返します。

以下がコードです。

```js
const initializeArrayWhile = (conditionFn, mapFn) => {
  const arr = [];
  let i = 0;
  let el = mapFn(i, undefined, arr);
  while (conditionFn(i, el, arr)) {
    arr.push(el);
    i++;
    el = mapFn(i, el, arr);
  }
  return arr;
};
```

`initializeArrayWhile` 関数を使って配列を初期化して値で埋めることができます。たとえば：

```js
initializeArrayWhile(
  (i, val) => val < 10,
  (i, val, arr) => (i <= 1 ? 1 : val + arr[i - 2])
); // [1, 1, 2, 3, 5, 8]
```
