# 文字列が有効な JSON かどうかを確認する

与えられた文字列が有効な JSON かどうかを確認するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `JSON.parse()` メソッドと `try...catch` ブロックを使って、提供された文字列が有効な JSON かどうかを確認します。
3. 文字列が有効な場合は `true` を返します。そうでない場合は `false` を返します。

このロジックを実装したコード スニペットの例を次に示します。

```js
const isValidJSON = (str) => {
  try {
    JSON.parse(str);
    return true;
  } catch (e) {
    return false;
  }
};
```

この関数を次のように異なる入力文字列でテストできます。

```js
isValidJSON('{"name":"Adam","age":20}'); // true
isValidJSON('{"name":"Adam",age:"20"}'); // false
isValidJSON(null); // false
```

最後の例では、`null` は有効な JSON 文字列ではないため、関数は `false` を返します。
