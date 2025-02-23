# 文字列を構成する文字をソートする方法

文字列をアルファベット順にソートするには、次のコードを使用します。

```js
const sortCharactersInString = (str) =>
  [...str].sort((a, b) => a.localeCompare(b)).join("");
```

まず、ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。

使用例：

```js
sortCharactersInString("cabbage"); // 'aabbceg'
```
