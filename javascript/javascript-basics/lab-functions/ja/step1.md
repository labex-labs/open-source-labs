# 関数

> VM 内には既に `index.html` が用意されています。

[関数](https://developer.mozilla.org/ja/docs/Glossary/Function) は、再利用したい機能をパッケージ化する方法です。コード内で関数名を呼び出すと実行されるコードの本体を定義することができます。これは、同じコードを繰り返し書くのに代わる良い方法です。既に関数のいくつかの使い方を見てきました。

例えば：

```js
let myVariable = document.querySelector("h1");
```

```js
alert("hello!");
```

これらの関数 `document.querySelector` と `alert` は、ブラウザに組み込まれています。

> 右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、「Web 8080」タブを更新して、ウェブページをプレビューできます。

変数名のように見えるものがあり、その後に丸括弧 `()` が続いている場合、それはおそらく関数です。関数はしばしば [引数](https://developer.mozilla.org/ja/docs/Glossary/Argument) を取ります：関数が仕事をするために必要なデータの断片です。引数は丸括弧の中に入り、引数が複数ある場合はコンマで区切られます。

例えば、`alert()` 関数はブラウザウィンドウ内にポップアップボックスを表示しますが、表示するメッセージを関数に伝えるために、文字列を引数として与える必要があります。

独自の関数も定義できます。

次の例では、2 つの数値を引数として受け取り、それらを掛け合わせる簡単な関数を作成します：

> ターミナル/SSH を開き、コーディングを練習するには `node` と入力してください。

```js
function multiply(num1, num2) {
  let result = num1 * num2;
  return result;
}
```

コンソールでこれを実行してみてください。その後、いくつかの引数を使ってテストしてください。例えば：

```js
multiply(4, 7);
multiply(20, 20);
multiply(0.5, 3);
```

> **注：** [`return`](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Statements/return) 文は、ブラウザに `result` 変数を関数の外に返すように指示します。そうすることで、それを使うことができるようになります。これは必要です。なぜなら、関数内で定義された変数はそれらの関数内でのみ利用可能だからです。これは変数のスコープと呼ばれます。([変数のスコープ](https://developer.mozilla.org/ja/docs/Web/JavaScript/Guide/Grammar_and_types#variable_scope) に関する詳細はこちらを参照してください。)
