# 変数

> ターミナル/SSH を開き、`node` と入力してコーディングの練習を始めましょう。

変数は値を格納するコンテナです。変数を宣言するには、`let` キーワードを使い、その後に変数名を指定します。

```js
let myVariable;
```

行末のセミコロンは文の終わりを示します。1 行に複数の文を書く場合にのみ必要です。ただし、文の終わりにセミコロンを付けるのが良い習慣だと考える人もいます。セミコロンを使うべき場合と使わないべき場合には他にもルールがあります。

変数名はほぼ自由に付けることができますが、いくつかの制限があります。不確かな場合は、[変数名の有効性を確認](https://mothereff.in/js-variables) することができます。

JavaScript は大文字と小文字を区別します。つまり、`myVariable` と `myvariable` は異なります。コードで問題が発生した場合は、大文字と小文字を確認してみてください！

変数を宣言した後、値を代入することができます。

```js
myVariable = "Bob";
```

また、これらの操作を 1 行で行うこともできます。

```js
let myVariable = "Bob";
```

変数名を呼び出すことで値を取得します。

```js
myVariable;
```

変数に値を代入した後、コードの後半でその値を変更することができます。

```js
let myVariable = "Bob";
myVariable = "Steve";
```

変数は異なる [データ型](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures) の値を保持することができることに注意してください。

| 変数                                                                     | 説明                                                                                                                                          | 例                                                                                                                |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| [文字列](https://developer.mozilla.org/en-US/docs/Glossary/String)       | これは文字列と呼ばれるテキストの並びです。値が文字列であることを示すには、シングルクォートまたはダブルクォートで囲みます。                    | `let myVariable = 'Bob';` または `let myVariable = "Bob";`                                                        |
| [数値](https://developer.mozilla.org/en-US/docs/Glossary/Number)         | これは数値です。数値にはクォートを付けません。                                                                                                | `let myVariable = 10;`                                                                                            |
| [ブール値](https://developer.mozilla.org/en-US/docs/Glossary/Boolean)    | これは真偽値です。`true` と `false` という単語は特別なキーワードで、クォートを必要としません。                                                | `let myVariable = true;`                                                                                          |
| [配列](https://developer.mozilla.org/en-US/docs/Glossary/Array)          | これは、複数の値を 1 つの参照に格納できる構造です。                                                                                           | `let myVariable = [1,'Bob','Steve',10];` 配列の各要素は `myVariable[0]`、`myVariable[1]` などのように参照します。 |
| [オブジェクト](https://developer.mozilla.org/en-US/docs/Glossary/Object) | これは何でもありえます。JavaScript のすべてはオブジェクトであり、変数に格納することができます。学習する際にはこのことを覚えておいてください。 | `let myVariable = document.querySelector('h1');` 上記のすべての例も同様です。                                     |

では、なぜ変数が必要なのでしょうか？変数はプログラミングで面白いことをするために必要です。もし値が変更できなければ、挨拶メッセージをカスタマイズしたり、画像ギャラリーに表示される画像を変更したりするような動的なことは何もできません。
