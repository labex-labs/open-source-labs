# フリップを使って関数の引数を並び替える

関数の引数の順序を入れ替えるには、`flip` 関数を使います。この関数は関数を引数として受け取り、最初の引数と最後の引数を入れ替える新しい関数を返します。

`flip` を実装するには：

- 引数の分解構文と可変長引数を持つクロージャを使います。
- 最初の引数を展開演算子 (`...`) を使ってスプライスし、残りの引数を適用する前に最後の引数にします。

```js
const flip =
  (fn) =>
  (first, ...rest) =>
    fn(...rest, first);
```

以下は、`flip` を使って `Object.assign` の引数を並び替える方法の例です：

```js
let a = { name: "John Smith" };
let b = {};

// Object.assign の引数を入れ替える新しい関数を作成する
const mergeFrom = flip(Object.assign);

// 最初の引数を a にバインドする新しい関数を作成する
let mergePerson = mergeFrom.bind(null, a);

// 新しい関数に b を第二引数として渡す
mergePerson(b); // b は現在 a に等しくなる

// あるいは、新しい関数を使わずに a と b をマージする
b = {};
Object.assign(b, a); // b は現在 a に等しくなる
```
