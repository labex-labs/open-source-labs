# 関数を使ったオブジェクトのプロパティの照合

コーディングの練習を始めるには、ターミナル/SSH を開いて `node` と入力します。

この関数は 2 つのオブジェクトを比較し、最初のオブジェクトが 2 番目のオブジェクトと同等のプロパティ値を持っているかどうかを確認します。これは、提供された関数に基づいて行われます。

この関数を使用するには、次の手順に従います。

- `Object.keys()` を使用して、2 番目のオブジェクトのすべてのキーを取得します。
- `Array.prototype.every()`、`Object.prototype.hasOwnProperty()`、および提供された関数を使用して、最初のオブジェクトにすべてのキーが存在し、同等の値を持っているかどうかを判断します。
- 関数が提供されない場合、値は等価演算子を使用して比較されます。

```js
const matchesWith = (obj, source, fn) =>
  Object.keys(source).every((key) =>
    obj.hasOwnProperty(key) && fn
      ? fn(obj[key], source[key], key, obj, source)
      : obj[key] == source[key]
  );
```

ここでは、この関数を使用する方法の例を示します。

```js
const isGreeting = (val) => /^h(?:i|ello)$/.test(val);
matchesWith(
  { greeting: "hello" },
  { greeting: "hi" },
  (oV, sV) => isGreeting(oV) && isGreeting(sV)
); // true
```

この例では、2 つのオブジェクトが `greeting` プロパティについて同等の値を持っているかどうかを確認しています。両方の値が有効な挨拶であることを確認するために、`isGreeting` 関数を使用しています。
