# 反復可能オブジェクトをハッシュに変換する

反復可能オブジェクト（オブジェクトまたは配列）をハッシュ（キー付きデータストア）に変換するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングの練習を始めるために `node` と入力します。
2. `Object.values()` を使って反復可能オブジェクトの値を取得します。
3. `Array.prototype.reduce()` を使って値を反復処理し、参照値をキーとするオブジェクトを作成します。
4. 反復可能オブジェクトとオプショナルなキーパラメータを使って `toHash` 関数を呼び出し、参照値を指定します。

以下は、JavaScript での `toHash` 関数の例の実装です。

```js
const toHash = (iterable, key) =>
  Object.values(iterable).reduce((acc, data, index) => {
    acc[!key ? index : data[key]] = data;
    return acc;
  }, {});
```

異なる反復可能オブジェクトとキーを使って `toHash` 関数を呼び出すことで、異なるハッシュを作成できます。たとえば：

```js
toHash([4, 3, 2, 1]); // { 0: 4, 1: 3, 2: 2, 3: 1 }
toHash([{ a: "label" }], "a"); // { label: { a: 'label' } }
```
