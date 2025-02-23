# JavaScript の配列から値を抽出する方法

JavaScript の配列から特定の値を抽出するには、`Array.prototype.filter()` と `Array.prototype.includes()` メソッドを使用できます。以下がその方法です。

```js
const pull = (arr, ...args) => {
  let argState = Array.isArray(args[0]) ? args[0] : args;
  let pulled = arr.filter((v) => !argState.includes(v));
  arr.length = 0;
  pulled.forEach((v) => arr.push(v));
};
```

`pull` 関数は、配列と削除する値を表す 1 つ以上の引数を受け取ります。その後、`Array.prototype.filter()` を使用して指定された値をフィルタリングすることで新しい配列を作成します。そして、元の配列の長さを `0` にリセットし、`Array.prototype.push()` を使用して抽出された値のみで再作成することで、元の配列を変更します。

`pull` 関数の使用方法の例を以下に示します。

```js
let myArray = ["a", "b", "c", "a", "b", "c"];
pull(myArray, "a", "c"); // myArray = [ 'b', 'b' ]
```

この例では、`pull` 関数は `myArray` 配列から `'a'` と `'c'` のすべての出現を削除し、`'b'` と `'b'` の値のみを含む新しい配列を返します。
