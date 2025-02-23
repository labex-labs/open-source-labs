# 循環参照を持つ JSON を文字列化する方法

循環参照を含む JSON オブジェクトを文字列化するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために `node` を入力します。
2. `WeakSet.prototype.add()` と `WeakSet.prototype.has()` を使って、既に見た値を格納して確認するための `WeakSet` を作成します。
3. `seen` に既に存在する値を省略し、必要に応じて新しい値を追加するカスタムの置換関数を使って `JSON.stringify()` を使用します。
4. ⚠️ **注意:** この関数は循環参照を見つけて削除しますが、これによりシリアライズされた JSON で循環データが失われます。

`stringifyCircularJSON` 関数のコードは次のとおりです。

```js
const stringifyCircularJSON = (obj) => {
  const seen = new WeakSet();
  return JSON.stringify(obj, (key, value) => {
    if (value !== null && typeof value === "object") {
      if (seen.has(value)) return;
      seen.add(value);
    }
    return value;
  });
};
```

この関数をテストするには、循環参照を持つオブジェクトを作成して `stringifyCircularJSON` を呼び出すことができます。

```js
const obj = { n: 42 };
obj.obj = obj;
stringifyCircularJSON(obj); // '{"n": 42}'
```
