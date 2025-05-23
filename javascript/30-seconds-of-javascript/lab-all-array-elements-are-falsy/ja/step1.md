# 配列のすべての要素が偽であるかどうかをテストする関数

配列のすべての要素が偽であるかどうかをテストするには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを練習するために`node`と入力します。
2. `Array.prototype.some()`を使って、コレクション内の要素が提供された述語関数に基づいて`true`を返すかどうかをテストします。
3. 2 番目の引数`fn`を省略すると、関数はデフォルトで`Boolean`を使います。
4. 配列のすべての要素が偽の場合、関数は`true`を返し、それ以外の場合は`false`を返します。

ここに関数の例の実装を示します。

```js
const none = (arr, fn = Boolean) => !arr.some(fn);
```

この関数を次のように使うことができます。

```js
none([0, 1, 3, 0], (x) => x == 2); // true
none([0, 0, 0]); // true
```
