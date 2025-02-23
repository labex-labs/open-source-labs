# JavaScript で N 次元配列を初期化する方法

JavaScript で N 次元配列を作成するには、`initializeNDArray` 関数を使うことができます。この関数は値と任意の次元数を引数として受け取り、その値で初期化された新しい配列を返します。

`initializeNDArray` を使うには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを始めるために `node` と入力します。
2. 再帰を使って指定された次元数の配列を作成します。
3. `Array.from()` と `Array.prototype.map()` を使って、各行が `initializeNDArray()` を使って初期化された新しい配列である行を生成します。

ここに `initializeNDArray` 関数のコードを示します。

```js
const initializeNDArray = (val, ...args) =>
  args.length === 0
    ? val
    : Array.from({ length: args[0] }).map(() =>
        initializeNDArray(val, ...args.slice(1))
      );
```

その後、望ましい値と次元数で `initializeNDArray` を呼び出すことができます。たとえば：

```js
initializeNDArray(1, 3); // [1, 1, 1]
initializeNDArray(5, 2, 2, 2); // [[[5, 5], [5, 5]], [[5, 5], [5, 5]]]
```
