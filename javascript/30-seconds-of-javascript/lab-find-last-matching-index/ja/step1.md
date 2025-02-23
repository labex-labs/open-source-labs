# JavaScriptを使って配列内の最後の一致要素のインデックスを見つける方法

JavaScriptの配列内で特定の条件に一致する最後の要素のインデックスを見つけるには、`findLastIndex`関数を使います。その使い方は以下の通りです。

```js
const findLastIndex = (arr, fn) =>
  (arr
    .map((val, i) => [i, val])
    .filter(([i, val]) => fn(val, i, arr))
    .pop() || [-1])[0];
```

`findLastIndex`関数は2つの引数をとります。探索対象の配列と、各要素をテストする関数です。その動作方法は以下の通りです。

1. `Array.prototype.map()`を使って、`[インデックス, 値]`のペアの新しい配列を作成します。
2. `Array.prototype.filter()`を使って、`fn`関数によって提供された条件に一致しない要素を配列から削除します。
3. `Array.prototype.pop()`を使って、フィルタリングされた配列の最後の要素を取得します。
4. フィルタリングされた配列が空の場合、`-1`を返します。

`findLastIndex`の使い方の例を以下に示します。

```js
findLastIndex([1, 2, 3, 4], (n) => n % 2 === 1); // 2 (値3のインデックス)
findLastIndex([1, 2, 3, 4], (n) => n === 5); // -1 (見つからない場合のデフォルト値)
```

コーディングの練習を始めるには、ターミナル/SSHを開いて`node`と入力します。
