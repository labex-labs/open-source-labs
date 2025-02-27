# ナメコゲーム

始めるには、エディタを開きます。エディタから以下のファイルが見えます。

```txt
├── public
├── src
│   ├── components
│   │   ├── common
│   │   │   └── Utils.js
│   │   ├── Board.js
│   │   ├── Game.js
│   │   └── Square.js
│   ├── App.css
│   ├── App.js
│   ├── App.test.js
│   ├── index.css
│   ├── index.js
│   ├── logo.svg
│   ├── reportWebVitals.js
│   └── setupTests.js
├── package-lock.json
└── package.json
```

## 要件

- プロジェクトの依存関係をインストールするには、以下のコマンドを使用します。

  ```bash
  npm i
  ```

- このチャレンジは、`src/components/Game.js` ファイルで完了してください。
- `useState` フックを使用して、3つの状態変数を定義します。board、xTurn、およびwinner。
  - `board` はゲーム盤の状態を表します。9要素の配列として初期化され、各要素は最初はnullに設定されます。
  - `xTurn` は、現在がXの番かどうかを示すブール値のフラグです。
  - `winner` は、盤面の現在の状態に基づいて勝者を決定する `calculateWinner` 関数の結果を格納します。
- ゲーム盤のマスがクリックされたときに `handleClick` 関数が呼び出されます。
  - スプレッド演算子 (`[...board]`) を使用して現在の盤面の状態のコピーを作成し、tmpBoard に割り当てます。
  - 既に勝者がいる場合 (winner が真) またはクリックされたマスが既にマークされている場合 (`tmpBoard[i]` が真)、関数は何も変更せずに返します。
  - それ以外の場合、クリックされたマスの値を `tmpBoard` で "X" または "O" に更新します。これは、`xTurn` の値に基づいて行われます。
  - その後、更新された `tmpBoard` を `setBoard` を使用して盤面の状態の新しい値として設定し、`setXTurn` を使用して `xTurn` をトグルします。

## 例

コードを完成させたら、以下のコマンドで実行します。

```bash
npm start
```

完成した結果は以下の通りです。

![ナメコゲームのデモ](../assets/finished.gif)
