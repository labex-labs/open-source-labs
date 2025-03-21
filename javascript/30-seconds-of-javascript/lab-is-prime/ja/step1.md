# 数が素数であるかどうかを確認する関数

コーディングを練習するには、ターミナル/SSH を開いて `node` と入力します。この関数は、与えられた整数が素数であるかどうかを確認します。数が素数であるかどうかを確認する手順は以下の通りです。

1. `2` から与えられた数の平方根までの数を確認します。
2. それらの数のいずれかが与えられた数を割り切る場合は、`false` を返します。
3. それらの数のいずれも与えられた数を割り切らない場合は、数が `2` 未満でない限り、`true` を返します。

ここに、この関数を JavaScript で実装するコードを示します。

```js
const isPrime = (num) => {
  const boundary = Math.floor(Math.sqrt(num));
  for (let i = 2; i <= boundary; i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return num >= 2;
};
```

この関数を、引数として数を指定して呼び出すことでテストできます。

```js
isPrime(11); // true
```
