# 可変長関数の変換

可変長関数を変換するには、次の手順に従います。

1. ターミナル/SSH を開き、コーディングを開始するために `node` と入力します。
2. 可変長関数を受け取る関数を作成します。
3. クロージャとスプレッド演算子 (`...`) を使って、引数の配列を関数の入力にマッピングします。
4. 引数の配列を受け取り、それらの引数で元の可変長関数を呼び出す新しい関数を返します。

この手法を使って `Math.max` 関数を変換する方法の例を次に示します。

```js
const spreadOver = (fn) => (argsArr) => fn(...argsArr);

const arrayMax = spreadOver(Math.max);
arrayMax([1, 2, 3]); // 3
```
