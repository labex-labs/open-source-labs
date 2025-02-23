# 文字列が絶対URLであるかどうかを確認する関数

与えられた文字列が絶対URLであるかどうかを確認するには、次の手順に従います。

1. ターミナル/SSHを開き、コーディングの練習を始めるために `node` と入力します。
2. `RegExp.prototype.test()` を使用して、文字列が絶対URLであるかどうかをテストします。
3. 関数は `const isAbsoluteURL = str => /^[a-z][a-z0-9+.-]*:/.test(str);` と定義する必要があります。
4. この関数は文字列引数 `str` を受け取り、文字列が絶対URLの場合には `true` を返し、それ以外の場合は `false` を返します。
5. 提供された例を使用して関数をテストします。

```js
isAbsoluteURL("https://google.com"); // true
isAbsoluteURL("ftp://www.myserver.net"); // true
isAbsoluteURL("/foo/bar"); // false
```
