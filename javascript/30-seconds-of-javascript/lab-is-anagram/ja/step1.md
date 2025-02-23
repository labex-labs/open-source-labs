# 文字列がアナグラムであるかどうかを確認する JavaScript 関数

文字列が別の文字列のアナグラムであるかどうかを確認するには、次の JavaScript 関数を使用します。大文字小文字を区別せず、空白、句読点、特殊文字を無視します。

```js
const isAnagram = (str1, str2) => {
  const normalize = (str) =>
    str
      .toLowerCase()
      .replace(/[^a-z0-9]/gi, "")
      .split("")
      .sort()
      .join("");
  return normalize(str1) === normalize(str2);
};
```

この関数を使用するには、ターミナル/SSH を開いて `node` と入力します。その後、2 つの文字列を引数として関数を呼び出します。

```js
isAnagram("iceman", "cinema"); // true
```

この関数は、不要な文字を削除するために、適切な正規表現を使用して `String.prototype.toLowerCase()` と `String.prototype.replace()` を使っています。また、両方の文字列に対して `String.prototype.split()`、`Array.prototype.sort()`、`Array.prototype.join()` を使って文字列を正規化し、正規化された形式が等しいかどうかを確認しています。
