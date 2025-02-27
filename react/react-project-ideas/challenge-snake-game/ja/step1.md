# ヘビゲーム

始めるには、エディタを開きます。エディタから以下のファイルが見えます。

```txt
├── public
├── src
│   ├── components
│   │   ├── Food.js
│   │   └── Snake.js
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
- `randomFoodPosition` 関数は、ゲーム盤上の食べ物の位置をランダムに生成するために定義されています。
- `App` 関数の中では、useStateフックを使っていくつかの状態変数が定義されています。
  - `snake` はヘビの現在の状態を表します。
  - `lastDirection` はヘビが最後に移動した方向を表します。
  - `foodPosition` は食べ物の現在の位置を表します。
  - `isStarted` はゲームが開始されたかどうかを判断します。
  - `gameOver` はゲームが終了したかどうかを示します。
  - `playgroundRef` はゲーム盤要素への参照です。

## 例

コードを完成させたら、次のコマンドで実行します。

```bash
npm start
```

完成した結果は以下の通りです。

![Snake game final result](../assets/finished.gif)
