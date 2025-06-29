# HTML 構造の理解

アニメーションを作成する前に、扱う HTML 構造を理解する必要があります。このステップでは、提供された HTML ファイルを調べ、必要な修正を行います。

1. エディタで `index.html` ファイルを開きます。

2. ファイルが空または存在しない場合は、以下の内容で作成します。

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Zoom In Zoom Out Animation</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>CSS Animation Demo</h1>
    <p>This box demonstrates a zoom in zoom out animation:</p>

    <div class="zoom-in-out-box"></div>
  </body>
</html>
```

3. この HTML が何をするかを理解しましょう。
   - タイトルとビューポート設定を持つ標準的な HTML ドキュメント構造があります。
   - `style.css` という名前の外部 CSS ファイルをリンクしています。
   - デモを説明する見出しと段落を含んでいます。
   - 最も重要なのは、アニメーションされる `zoom-in-out-box` クラスの `<div>` 要素があることです。

4. 変更を加えた場合は、`index.html` ファイルを保存します。

この div 要素がアニメーションを作成するためのキャンバスになります。次のステップでは、この要素を CSS を使ってスタイルを設定します。
