# JavaScript を使って文字列の部分文字列を数える方法

コーディングを練習したい場合は、ターミナル/SSH を開いて `node` と入力します。この JavaScript 関数は、指定された部分文字列が与えられた文字列に何回出現するかを数えます。

この関数を使用するには、次の手順に従います。

1. `str` と `searchValue` の 2 つのパラメータを持つ `countSubstrings` と呼ばれる関数を宣言します。
2. `count` と `i` の 2 つの変数を初期化します。
3. `Array.prototype.indexOf()` メソッドを使用して、`str` の中で `searchValue` を検索します。
4. 値が見つかった場合、`count` 変数をインクリメントし、`i` 変数を更新します。
5. `Array.prototype.indexOf()` から返される値が `-1` になるとすぐに返る `while` ループを使用します。
6. `count` 変数を返します。

以下は、`countSubstrings` 関数のコードです。

```js
const countSubstrings = (str, searchValue) => {
  let count = 0,
    i = 0;
  while (true) {
    const r = str.indexOf(searchValue, i);
    if (r !== -1) [count, i] = [count + 1, r + 1];
    else return count;
  }
};
```

次の例を使用して関数をテストできます。

```js
countSubstrings("tiktok tok tok tik tok tik", "tik"); // 3
countSubstrings("tutut tut tut", "tut"); // 4
```
