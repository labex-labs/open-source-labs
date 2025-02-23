# JavaScript のオブジェクトから関数プロパティ名を取得する方法

オブジェクトから関数プロパティ名の配列を取得するには、以下に示す `functions` 関数を使用します。この関数は、任意で継承されたプロパティも含めることができます。

`functions` 関数の使い方は以下の通りです。

1. ターミナル/SSH を開き、コーディングを練習するために `node` と入力します。
2. `Object.keys()` を使用して、オブジェクトの独自のプロパティを反復処理します。
3. 継承されたプロパティを含めたい場合は、`inherited` 引数を `true` に設定し、`Object.getPrototypeOf()` を使用してオブジェクトの継承されたプロパティを取得します。
4. `Array.prototype.filter()` を使用して、関数であるプロパティのみを残します。
5. デフォルトでは継承されたプロパティを含めないため、2 番目の引数 `inherited` を省略します。

```js
const functions = (obj, inherited = false) =>
  (inherited
    ? [...Object.keys(obj), ...Object.keys(Object.getPrototypeOf(obj))]
    : Object.keys(obj)
  ).filter((key) => typeof obj[key] === "function");
```

`functions` 関数の使用例は以下の通りです。

```js
function Foo() {
  this.a = () => 1;
  this.b = () => 2;
}
Foo.prototype.c = () => 3;
functions(new Foo()); // ['a', 'b']
functions(new Foo(), true); // ['a', 'b', 'c']
```
