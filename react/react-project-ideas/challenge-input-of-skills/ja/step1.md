# スキルの入力

始めるには、エディタを開きます。エディタから次のファイルが見えます。

```txt
├── public
├── src
│   ├── components
│   │   └── TagInput.js
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

- このチャレンジは、`src/component/TagInput.js` ファイルで完了してください。
- `handleAddTag` 関数は、入力フィールドでキーが押されたときに呼び出されます。キーが Enter キーでない場合、関数は早期に返して何もしません。それ以外の場合、入力値をチェックし、空でなく既に追加されていない場合はタグの状態に追加します。その後、入力フィールドをクリアします。
- `onDeleteTag` 関数は、タグがクリックされたときに呼び出されます。クリックされたタグを削除するためにタグの状態をフィルタリングし、フィルタリングされたタグで状態を更新します。

## 例

コードを完成させたら、次のコマンドで実行します。

```bash
npm start
```

完成した結果は次のとおりです。

![Tag input functionality demo](../assets/finished.gif)
