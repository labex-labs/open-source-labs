# レーベンシュタイン距離アルゴリズム

2 つの文字列の違いを計算するには、レーベンシュタイン距離アルゴリズムを使用できます。以下にその方法を示します。

1. どちらかの文字列の `length` が 0 の場合、もう一方の文字列の `length` を返します。
2. ネストした `for` ループを使用して、ターゲット文字列とソース文字列の文字を反復処理します。
3. それぞれターゲット文字列とソース文字列の `i - 1` と `j - 1` に対応する文字を置換するコストを計算します（同じ場合は `0`、それ以外の場合は `1`）。
4. `Math.min()` を使用して、2 次元配列の各要素に、上のセルに 1 を加えた値、左のセルに 1 を加えた値、または左上のセルに先に計算したコストを加えた値の最小値を設定します。
5. 生成された配列の最後の行の最後の要素を返します。

このコーディングを練習するには、ターミナル/SSH を開いて `node` と入力します。以下は使用できるコードです。

```js
const levenshteinDistance = (s, t) => {
  if (!s.length) return t.length;
  if (!t.length) return s.length;
  const arr = [];
  for (let i = 0; i <= t.length; i++) {
    arr[i] = [i];
    for (let j = 1; j <= s.length; j++) {
      arr[i][j] =
        i === 0
          ? j
          : Math.min(
              arr[i - 1][j] + 1,
              arr[i][j - 1] + 1,
              arr[i - 1][j - 1] + (s[j - 1] === t[i - 1] ? 0 : 1)
            );
    }
  }
  return arr[t.length][s.length];
};

console.log(levenshteinDistance("duck", "dark")); // 2
```
