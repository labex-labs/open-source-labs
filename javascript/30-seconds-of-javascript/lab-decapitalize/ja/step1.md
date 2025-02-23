# 文字列の先頭文字を小文字にする JavaScript 関数

文字列の先頭文字を小文字にするには、次の JavaScript 関数を使用します。

```js
const decapitalize = ([first, ...rest], upperRest = false) => {
  return (
    first.toLowerCase() +
    (upperRest ? rest.join("").toUpperCase() : rest.join(""))
  );
};
```

この関数を使用するには、ターミナル/SSH を開いて `node` と入力します。その後、先頭の引数として小文字にしたい文字列で `decapitalize` 関数を呼び出します。

任意で、文字列の残りを大文字に変換するには、2 番目の引数 `upperRest` を `true` に設定できます。`upperRest` が指定されていない場合、既定値は `false` になります。

以下はいくつかの例です。

```js
decapitalize("FooBar"); // 'fooBar'
decapitalize("FooBar", true); // 'fOOBAR'
```
