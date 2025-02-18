# 文字列内のパターンの最後の出現箇所を置き換える関数

以下は、文字列内のパターンの最後の出現箇所を置き換える関数です。

```js
const replaceLast = (str, pattern, replacement) => {
```

この関数を使用するには、ターミナル/SSH を開き、`node` と入力します。

- まず、`typeof` を使用して、`pattern` が文字列か正規表現かを判断します。
- `pattern` が文字列の場合、それを `match` として使用します。
- それ以外の場合、`pattern` の `RegExp.prototype.source` を使用して新しい正規表現を作成し、`'g'` フラグを追加します。`String.prototype.match()` と `Array.prototype.slice()` を使用して、最後の一致箇所（あれば）を取得します。

```js
const match =
  typeof pattern === "string"
    ? pattern
    : (str.match(new RegExp(pattern.source, "g")) || []).slice(-1)[0];
```

- `String.prototype.lastIndexOf()` を使用して、文字列内の一致箇所の最後の出現位置を見つけます。
- 一致箇所が見つかった場合、`String.prototype.slice()` とテンプレートリテラルを使用して、一致する部分文字列を指定された `replacement` で置き換えます。
- 一致箇所が見つからない場合、元の文字列を返します。

```js
  if (!match) return str;
  const last = str.lastIndexOf(match);
  return last!== -1
   ? `${str.slice(0, last)}${replacement}${str.slice(last + match.length)}`
    : str;
};
```

この関数の使用例をいくつか紹介します。

```js
replaceLast("abcabdef", "ab", "gg"); // 'abcggdef'
replaceLast("abcabdef", /ab/, "gg"); // 'abcggdef'
replaceLast("abcabdef", "ad", "gg"); // 'abcabdef'
replaceLast("abcabdef", /ad/, "gg"); // 'abcabdef'
```
