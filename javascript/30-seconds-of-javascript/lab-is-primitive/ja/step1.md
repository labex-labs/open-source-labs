# プリミティブ値の確認

コーディングを練習するには、ターミナルまたはSSHを開いて `node` と入力します。その後、次の手順に従って値がプリミティブかどうかを確認できます。

1. 確認したい値から `Object(val)` を使ってオブジェクトを作成します。
2. 作成したオブジェクトと元の値を厳密な不等号演算子 `!==` を使って比較します。
3. 2つの値が等しくなければ、元の値はプリミティブです。

`isPrimitive` 関数のコードは次のとおりです。

```js
const isPrimitive = (val) => Object(val) !== val;
```

この関数を次の値でテストできます。

```js
isPrimitive(null); // true
isPrimitive(undefined); // true
isPrimitive(50); // true
isPrimitive("Hello!"); // true
isPrimitive(false); // true
isPrimitive(Symbol()); // true
isPrimitive([]); // false
isPrimitive({}); // false
```

確認したい値がプリミティブであれば、関数は `true` を返します。それ以外の場合は `false` を返します。
