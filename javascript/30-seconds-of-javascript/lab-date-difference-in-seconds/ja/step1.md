# JavaScript の Date オブジェクトの使い始め方

JavaScript は、日付と時間を扱うための組み込みの `Date` オブジェクトを提供しています。日付の差を計算する前に、まず JavaScript で `Date` オブジェクトを作成して操作する方法を理解しましょう。

## Node.js 環境の起動

まずは、対話型の Node.js 環境を開きましょう。

1. WebIDE 上部の「Terminal」メニューをクリックしてターミナルを開きます。
2. 以下のコマンドを入力して Enter キーを押します。

```bash
node
```

これで Node.js のプロンプト (`>`) が表示され、JavaScript の対話型環境に入ったことがわかります。これにより、ターミナルで直接 JavaScript コードを実行できます。

![node-prompt](../assets/screenshot-20250306-328ScUbO@2x.png)

## Date オブジェクトの作成

JavaScript では、いくつかの方法で新しい `Date` オブジェクトを作成できます。

```javascript
// 現在の日付と時刻
let now = new Date();
console.log(now);

// 特定の日付と時刻 (年，月 [0-11], 日，時，分，秒)
let specificDate = new Date(2023, 0, 15, 10, 30, 45); // 2023 年 1 月 15 日 10:30:45
console.log(specificDate);

// 文字列からの日付
let dateFromString = new Date("2023-01-15T10:30:45");
console.log(dateFromString);
```

これらの例を Node.js 環境でそれぞれ入力し、出力を確認してみてください。

なお、JavaScript では月は 0 から始まるインデックスで表されます。つまり、1 月は 0、2 月は 1 といった具合です。

## Date オブジェクトからタイムスタンプを取得する

JavaScript のすべての `Date` オブジェクトは、内部的に 1970 年 1 月 1 日 (UTC) から経過したミリ秒数として時間を格納しています。これをタイムスタンプと呼びます。

```javascript
let now = new Date();
console.log(now.getTime()); // ミリ秒単位のタイムスタンプを取得
```

このタイムスタンプは、日付の差を計算する際に役立ちます。
