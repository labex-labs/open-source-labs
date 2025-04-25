# アロー関数を使用した日付差関数の実装

これで日付の差を計算する方法がわかったので、アロー関数を使って関数をより簡潔なバージョンで実装してみましょう。

## JavaScript のアロー関数

アロー関数は、JavaScript で関数を書くための短い構文を提供します。以下は、アロー関数の構文を使って日付差関数を書き換えた例です。

```javascript
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;
```

この関数は、前の関数とまったく同じことを行いますが、よりクリーンで簡潔な構文になっています。

## JavaScript ファイルの作成

関数を保存してテストするために、JavaScript ファイルを作成しましょう。Ctrl+D を押すか、`.exit` と入力して Enter を押して Node.js 環境を終了します。

次に、WebIDE で `dateDifference.js` という名前の新しいファイルを作成します。

1. 左側のサイドバーにある「Explorer」アイコンをクリックします。
2. ファイルエクスプローラー内で右クリックし、「New File」を選択します。
3. ファイル名を `dateDifference.js` と入力し、Enter を押します。
4. 以下のコードをファイルに追加します。

```javascript
// Function to calculate difference between two dates in seconds
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;

// Test examples
console.log("Example 1:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:15"),
    new Date("2020-12-24 00:00:17")
  )
); // Expected output: 2

console.log("\nExample 2:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:00"),
    new Date("2020-12-24 00:01:00")
  )
); // Expected output: 60

console.log("\nExample 3:");
console.log(
  getSecondsDiffBetweenDates(
    new Date("2020-12-24 00:00:00"),
    new Date("2020-12-24 01:00:00")
  )
); // Expected output: 3600
```

Ctrl+S を押すか、「File」>「Save」をクリックしてファイルを保存します。

## JavaScript ファイルの実行

先ほど作成したファイルを実行するには、ターミナルで以下のコマンドを使用します。

```bash
node dateDifference.js
```

以下の出力が表示されるはずです。

```
Example 1:
2

Example 2:
60

Example 3:
3600
```

これにより、関数が正しく動作していることが確認できます。

- 最初の例：00:00:15 と 00:00:17 の差は 2 秒です。
- 2 番目の例：00:00:00 と 00:01:00 の差は 60 秒（1 分）です。
- 3 番目の例：00:00:00 と 01:00:00 の差は 3600 秒（1 時間）です。
