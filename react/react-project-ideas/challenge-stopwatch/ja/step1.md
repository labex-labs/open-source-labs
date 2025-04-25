# ストップウォッチ

始めるには、エディタを開きます。エディタから以下のファイルが見えます。

```txt
├── public
├── src
│   ├── components
│   │   ├──common
│   │   ├── stopwatch
│   │   ├── timer
│   │   ├── App.css
│   │   └── App.js
│   ├── index.css
│   └── index.js
├── package-lock.json
└── package.json
```

## 要件

- プロジェクトの依存関係をインストールするには、次のコマンドを使用します。

  ```bash
  npm i
  ```

- このチャレンジは、`src/components/timer/Timer.js` ファイルで完了してください。
- `onStart` 関数は、useEffect フックによって 1 秒ごとに呼び出されます。
  - タイマーが 0 時間、0 分、0 秒に達したかどうかを確認します。その場合は、isStarted を false に設定して返します。
  - タイマーが起動していない場合は、何も変更せずに返します。
  - タイマーが動作している場合は、タイマーを 1 秒減らします。
  - 分または秒が 0 に達した場合は、setTimer 関数を使用して、時間、分、または秒を適切に調整します。
- `onReset` 関数は、「リセット」ボタンがクリックされたときに呼び出されます。
  - isStarted を false に設定し、タイマーを 0 時間、0 分、0 秒にリセットします。

## 例

コードを完成させたら、次のコマンドで実行します。

```bash
npm start
```

完成した結果は次のとおりです。

![完了したストップウォッチのデモ](../assets/finished.gif)
