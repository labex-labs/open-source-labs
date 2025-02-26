# 個人ポートフォリオ

始めるには、エディタを開きます。エディタから以下のファイルが見えます。

```txt
├── public
├── src
│   ├── components
│   ├── App.css
│   ├── App.js
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

- このチャレンジは、`src/App.js` ファイルで完了してください。
- `toggleVisible` 関数は、スクロール位置を確認し、それに応じて `showBackToTopBtn` 状態を更新するために定義されています。
- `useEffect` フックは、ウィンドウのスクロールイベントにイベントリスナーを追加するために使用され、これにより `toggleVisible` 関数がトリガーされます。
- `scrollToTop` 関数は、トップに戻るボタンがクリックされたときにウィンドウをトップにスクロールするために定義されています。

## 例

コードを完了したら、次のコマンドで実行します。

```bash
npm start
```

完成した結果は次のとおりです。

![完了したプロジェクトのデモ](../assets/finished.gif)
