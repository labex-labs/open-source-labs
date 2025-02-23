# JavaScriptにおける値が数値であるかのチェック

JavaScriptにおいて値が数値であるかどうかをチェックするには、`typeof`演算子を使用して値が数値プリミティブとして分類されているかどうかを判断できます。`NaN`に関する問題を防ぐために（`NaN`は`typeof`が`number`であり、自身と等しくない）、値が自身と等しいかどうかを`val === val`を使ってチェックすることもできます。

与えられた値が数値であるかどうかをチェックする例の関数は次の通りです。

```js
const isNumber = (val) => typeof val === "number" && val === val;
```

この関数を次のように使うことができます。

```js
isNumber(1); // true
isNumber("1"); // false
isNumber(NaN); // false
```
