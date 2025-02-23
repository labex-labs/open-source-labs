# オブジェクトが特定の値を含むかどうかを確認する関数

オブジェクトが特定の値を含むかどうかを確認するには、次の関数を使用します。

```js
const hasValue = (obj, value) => Object.values(obj).includes(value);
```

この関数を使用するには、検索対象のオブジェクトとターゲット値を引数として渡します。オブジェクトに値が含まれている場合は `true` を返し、含まれていない場合は `false` を返します。

以下は例です。

```js
const obj = { a: 100, b: 200 };
console.log(hasValue(obj, 100)); // true
console.log(hasValue(obj, 999)); // false
```

コーディングを始めるには、ターミナル/SSH を開いて `node` と入力します。
