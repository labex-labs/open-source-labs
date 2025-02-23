# JavaScript でオブジェクトを完全に凍結する方法

JavaScript でオブジェクトを完全に凍結するには、次の手順に従います。

1. `Object.keys()` を使用して、渡されたオブジェクトのすべてのプロパティを取得します。
2. `Array.prototype.forEach()` を使用して、プロパティを反復処理します。
3. 必要に応じて `deepFreeze()` を適用しながら、すべてのオブジェクトであるプロパティに再帰的に `Object.freeze()` を呼び出します。
4. 最後に、`Object.freeze()` を使用して与えられたオブジェクトを凍結します。

以下がコードです。

```js
const deepFreeze = (obj) => {
  Object.keys(obj).forEach((prop) => {
    if (typeof obj[prop] === "object") deepFreeze(obj[prop]);
  });
  return Object.freeze(obj);
};
```

次のコードを使用して、完全に凍結されたオブジェクトをテストできます。

```js
"use strict";

const val = deepFreeze([1, [2, 3]]);

val[0] = 3; // 許可されていません
val[1][0] = 4; // 同様に許可されていません
```

上記のコードはエラーを投げます。なぜなら、`val` オブジェクトは完全に凍結されており、変更できないからです。
