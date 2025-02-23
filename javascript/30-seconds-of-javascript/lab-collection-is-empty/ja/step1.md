# コレクションが空かどうかをチェックする

コレクションが空かどうかをチェックするには、ターミナル/SSH を開いて `node` と入力します。このプログラムは、値が空のオブジェクト/コレクションであり、列挙可能なプロパティがなく、またはコレクションとは考えられない任意の型であるかどうかをチェックします。

このプログラムを使用するには、提供された値が `null` であるか、またはその `length` が `0` に等しいかどうかを確認します。以下はコードの例です：

```js
const isEmpty = (val) => val == null || !(Object.keys(val) || val).length;
```

次に、以下のコードを使用してプログラムをテストできます：

```js
isEmpty([]); // true
isEmpty({}); // true
isEmpty(""); // true
isEmpty([1, 2]); // false
isEmpty({ a: 1, b: 2 }); // false
isEmpty("text"); // false
isEmpty(123); // true - 型はコレクションとは考えられない
isEmpty(true); // true - 型はコレクションとは考えられない
```
