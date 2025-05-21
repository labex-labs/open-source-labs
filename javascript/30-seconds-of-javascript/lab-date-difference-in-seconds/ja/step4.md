# 実用的なアプリケーションの作成

これで日付の差を秒単位で計算する機能が動作する関数ができたので、もっと実用的なアプリケーションを作成しましょう。起動してから経過した時間を計算する簡単なタイマーを作成します。

## タイマーアプリケーションの作成

WebIDE で `timer.js` という名前の新しいファイルを作成します。

1. 左側のサイドバーにある「Explorer」アイコンをクリックします。
2. ファイルエクスプローラー内で右クリックし、「New File」を選択します。
3. ファイル名を `timer.js` と入力し、Enter を押します。
4. 以下のコードをファイルに追加します。

```javascript
// Function to calculate difference between two dates in seconds
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;

// Start time - when the script starts running
const startTime = new Date();
console.log(`Timer started at: ${startTime.toLocaleTimeString()}`);

// Function to update and display the elapsed time
function updateTimer() {
  const currentTime = new Date();
  const elapsedSeconds = getSecondsDiffBetweenDates(startTime, currentTime);

  // Format the time as hours:minutes:seconds
  const hours = Math.floor(elapsedSeconds / 3600);
  const minutes = Math.floor((elapsedSeconds % 3600) / 60);
  const seconds = Math.floor(elapsedSeconds % 60);

  const formattedTime = `${hours.toString().padStart(2, "0")}:${minutes
    .toString()
    .padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;

  // Clear the console and display the updated time
  console.clear();
  console.log(`Timer started at: ${startTime.toLocaleTimeString()}`);
  console.log(`Elapsed time: ${formattedTime}`);
}

// Update the timer every second
console.log("Timer is running... Press Ctrl+C to stop.");
const timerInterval = setInterval(updateTimer, 1000);

// Keep the script running
setTimeout(() => {
  clearInterval(timerInterval);
  console.log("\nTimer stopped after 1 minute.");
}, 60000); // Run for 1 minute
```

Ctrl+S を押すか、「File」>「Save」をクリックしてファイルを保存します。

## タイマーアプリケーションの実行

タイマーアプリケーションを実行するには、ターミナルで以下のコマンドを使用します。

```bash
node timer.js
```

タイマーが起動し、1 秒ごとに更新され、起動してから経過した時間が表示されます。タイマーは 1 分後に自動的に停止しますが、Ctrl+C を押すことで早く停止することもできます。

## タイマーアプリケーションの仕組みの理解

タイマーアプリケーションがどのように動作するかを分解してみましょう。

1. `getSecondsDiffBetweenDates` 関数を定義して、時間の差を秒単位で計算します。
2. スクリプトが実行を開始したときの開始時間を記録します。
3. `updateTimer` 関数を定義します。この関数は以下のことを行います。
   - 現在の時間を取得します。
   - 開始時間から経過した秒数を計算します。
   - 経過時間を「時：分：秒」の形式に整形します。
   - 整形された時間を表示します。
4. `setInterval` を使用して、`updateTimer` 関数を 1000 ミリ秒（1 秒）ごとに実行します。
5. `setTimeout` を使用して、60000 ミリ秒（1 分）後にタイマーを停止します。

このアプリケーションは、日付差関数を実時間のタイマーを作成するために実用的に利用する例を示しています。
