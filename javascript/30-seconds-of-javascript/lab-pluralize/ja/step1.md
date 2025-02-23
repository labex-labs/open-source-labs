# 文字列を複数形にする

与えられた数値に基づいて文字列を複数形にするには、`pluralize` 関数を使用します。まず、ターミナル/SSH を開き、`node` と入力します。この関数は、入力された数値に応じて、単数形または複数形の文字列を返すことができます。また、カスタムの複数形を使用するためにオプションの辞書を指定することもできます。

`pluralize` 関数を定義するには、`word` とオプションの `plural` 形式を受け取るクロージャを使用します。入力された `num` が `-1` または `1` の場合、`word` の単数形を返します。それ以外の場合、`plural` 形式を返します。カスタムの `plural` 形式が指定されていない場合、関数は単数形の `word` + `s` のデフォルトを使用します。

最初の引数がオブジェクトの場合、`pluralize` 関数は新しい関数を返します。この新しい関数は、指定された辞書を使用して、`word` の正しい複数形を解決することができます。

以下は、動作する `pluralize` 関数です：

```js
const pluralize = (val, word, plural = word + "s") => {
  const _pluralize = (num, word, plural = word + "s") =>
    [1, -1].includes(Number(num)) ? word : plural;
  if (typeof val === "object")
    return (num, word) => _pluralize(num, word, val[word]);
  return _pluralize(val, word, plural);
};
```

`pluralize` 関数を次のように使用できます：

```js
pluralize(0, "apple"); // 'apples'
pluralize(1, "apple"); // 'apple'
pluralize(2, "apple"); // 'apples'
pluralize(2, "person", "people"); // 'people'
```

カスタムの複数形の辞書がある場合、与えられた `word` に対して正しい複数形を自動的に使用する `autoPluralize` 関数を作成することができます：

```js
const PLURALS = {
  person: "people",
  radius: "radii"
};
const autoPluralize = pluralize(PLURALS);
autoPluralize(2, "person"); // 'people'
```
