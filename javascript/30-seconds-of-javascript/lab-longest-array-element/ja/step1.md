# 配列内の最長の要素を見つける方法

配列内の最長の要素を見つけるには、ターミナル/SSH を開いて `node` と入力します。この関数は任意の数の反復可能なオブジェクトまたは `length` プロパティを持つオブジェクトを受け取り、最長のものを返します。オブジェクトの長さを比較して最長のものを見つけるために `Array.prototype.reduce()` を使います。複数のオブジェクトが同じ長さの場合、関数は最初のものを返します。引数が提供されない場合、`undefined` を返します。

以下がコードです。

```js
const longestItem = (...vals) =>
  vals.reduce((a, x) => (x.length > a.length ? x : a));
```

この関数を以下のように使うことができます。

```js
longestItem("this", "is", "a", "testcase"); // 'testcase'
longestItem(...["a", "ab", "abc"]); // 'abc'
longestItem(...["a", "ab", "abc"], "abcd"); // 'abcd'
longestItem([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]); // [1, 2, 3, 4, 5]
longestItem([1, 2, 3], "foobar"); // 'foobar'
```
