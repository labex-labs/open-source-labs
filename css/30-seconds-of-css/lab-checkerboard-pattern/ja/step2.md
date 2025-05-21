# HTML 構造の作成

プロジェクトファイルを理解したので、チェッカーボードパターンの HTML 構造を作成しましょう。

1. 再度エディターで `index.html` ファイルを開きます。

2. チェッカーボードパターンのコンテナ要素を追加する必要があります。`<body>` タグ内のコメントを、クラス名が "checkerboard" の `<div>` 要素に置き換えます。

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Checkerboard Pattern</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <div class="checkerboard"></div>
  </body>
</html>
```

3. Ctrl+S を押すか、「ファイル」>「保存」をクリックして、`index.html` ファイルを保存します。

4. 次に、チェッカーボードの寸法を定義する基本的な CSS を追加しましょう。`style.css` ファイルを開き、次のコードを追加します。

```css
.checkerboard {
  width: 240px;
  height: 240px;
  background-color: #fff;
}
```

この CSS コードは以下のことを行います。

- チェッカーボードの幅と高さを 240 ピクセルに設定します。
- 背景色を白 (#fff) に設定します。

5. `style.css` ファイルを保存します。

6. **Web 8080** タブを更新して変更を確認します。

これで幅と高さが 240 ピクセルの白い正方形が表示されるはずです。これがチェッカーボードパターンのキャンバスになります。
