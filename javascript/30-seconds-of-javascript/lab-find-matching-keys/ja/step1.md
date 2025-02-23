# 一致するキーを見つける

オブジェクト内で特定の値と一致するすべてのキーを見つけるには、次の手順に従います。

1. ターミナル/SSHを開き、コーディングを練習するために `node` と入力します。
2. `Object.keys()` を使ってオブジェクトのすべてのプロパティを取得します。
3. `Array.prototype.filter()` を使って各キーと値のペアをテストし、指定された値と等しいすべてのキーを返します。

このロジックを実装した例の関数は次のとおりです。

```js
const findKeys = (obj, val) =>
  Object.keys(obj).filter((key) => obj[key] === val);
```

この関数を次のように使うことができます。

```js
const ages = {
  Leo: 20,
  Zoey: 21,
  Jane: 20
};
findKeys(ages, 20); // [ 'Leo', 'Jane' ]
```
