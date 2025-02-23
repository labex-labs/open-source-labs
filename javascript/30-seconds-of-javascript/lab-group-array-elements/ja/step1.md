# 配列要素をグループ化する

元の配列内の要素の位置に基づいて配列要素をグループ化するには、以下に示す `zip` 関数を使用します。

- ターミナル/SSH を開き、コーディングを練習するには `node` と入力します。
- `zip` 関数は、`Math.max()` と `Function.prototype.apply()` を使用して、引数の中で最も長い配列を取得します。
- その長さの配列を返り値として作成し、マッピング関数付きで `Array.from()` を使用してグループ化された要素の配列を作成します。
- 引数の配列の長さが異なる場合、値が見つからない場合は `undefined` が使用されます。

```js
const zip = (...arrays) => {
  const maxLength = Math.max(...arrays.map((x) => x.length));
  return Array.from({ length: maxLength }).map((_, i) => {
    return Array.from({ length: arrays.length }, (_, k) => arrays[k][i]);
  });
};
```

使用例:

```js
zip(["a", "b"], [1, 2], [true, false]); // [['a', 1, true], ['b', 2, false]]
zip(["a"], [1, 2], [true, false]); // [['a', 1, true], [undefined, 2, false]]
```
