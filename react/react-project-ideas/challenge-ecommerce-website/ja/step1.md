# eコマースサイト

始めるには、エディタを開きます。エディタから次のファイルを見ることができます。

```txt
├── public
├── src
│   ├── components
│   ├── context
│   ├── mockData
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

- このチャレンジは、`src/components/itemDetail/ItemDetail.js`ファイルで完了してください。
- `getItemDetail`関数が定義されています。これはidパラメータを受け取り、与えられたidに一致するitems配列からの商品オブジェクトを返します。
- 商品をクリックして商品詳細ページを表示する機能の実装。

## 例

コードを完成させたら、次のコマンドで実行します。

```bash
npm start
```

完成した結果は次のとおりです。

![Ecommerce product detail demo](../assets/finished.gif)
