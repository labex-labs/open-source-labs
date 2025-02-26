# カスタムフォーム

始めるには、エディタを開きます。エディタから次のファイルが見えます。

```txt
├── public
├── src
│   ├── components
│   │   └── CustomForm
│   │       ├── CustomForm.css
│   │       └── CustomForm.js
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

- このチャレンジは `App.js` ファイルで完了してください。
- `useRef` フックを使用して、2 つの ref オブジェクト `usernameRef` と `passwordRef` を作成します。これらの ref は、入力フィールドの値にアクセスするために使用されます。
- `handleLogin` 関数：この関数は、「ログイン」ボタンがクリックされたときに呼び出されます。ユーザー名とパスワード入力フィールドの値をコンソールにログ出力し、入力されたユーザー名とパスワードで警告を表示します。
- `handleRegister` 関数：この関数は、「登録」ボタンがクリックされたときに呼び出されます。ユーザー名とパスワード入力フィールドの値をコンソールにログ出力します。

## 例

コードを完成させたら、次のコマンドで実行します。

```bash
npm start
```

完成した結果は次のとおりです。

![Custom Form Final Result](../assets/finished.gif)
