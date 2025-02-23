# 部分文字列のインデックス

与えられた文字列内の部分文字列のすべてのインデックスを見つけるには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. 組み込みメソッド `Array.prototype.indexOf()` を使用して、`str` 内の `searchValue` を検索します。
3. 値が見つかった場合、インデックスを返してインデックス `i` を更新するために `yield` を使用します。
4. `Array.prototype.indexOf()` から返される値が `-1` になったときにジェネレータを終了する `while` ループを使用します。

上記の手順を実装するためのサンプルコードは次のとおりです。

```js
const indexOfSubstrings = function* (str, searchValue) {
  let i = 0;
  while (true) {
    const r = str.indexOf(searchValue, i);
    if (r !== -1) {
      yield r;
      i = r + 1;
    } else return;
  }
};
```

次のコードで関数をテストできます。

```js
[...indexOfSubstrings("tiktok tok tok tik tok tik", "tik")]; // [0, 15, 23]
[...indexOfSubstrings("tutut tut tut", "tut")]; // [0, 2, 6, 10]
[...indexOfSubstrings("hello", "hi")]; // []
```
