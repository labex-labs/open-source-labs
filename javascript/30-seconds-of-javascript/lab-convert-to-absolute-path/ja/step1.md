# Node.js でチルダパスを絶対パスに変換する方法

Node.js でコーディングを始めるには、ターミナルまたは SSH を開き、`node` と入力します。チルダパスを絶対パスに変換するには、次のコードを使用します。

```js
const untildify = (str) =>
  str.replace(/^~($|\/|\\)/, `${require("os").homedir()}$1`);
```

このコードは、正規表現と `os.homedir()` を使って `String.prototype.replace()` を用い、パスの先頭の `~` をホームディレクトリに置き換えます。以下は、`untildify` 関数の使い方の例です。

```js
untildify("~/node"); // returns '/Users/aUser/node'
```
