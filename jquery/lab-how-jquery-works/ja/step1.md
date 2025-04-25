# jQuery の仕組み

> VM 内には既に `index.html` が用意されています。

このファイルは環境初期化時に自動的に生成されます。自動生成されない場合は、上の画像に示すようにファイルを作成して機能させます。関数コードは以下の通りです。

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Demo</title>
  </head>
  <body>
    <p>jQuery</p>
    <script src="jquery.min.js"></script>
    <script>
      // ここにあなたのコードを記述します。
    </script>
  </body>
</html>
```

`<script>` 要素の `src` 属性は jQuery のコピー先を指す必要があります。[jQuery のダウンロード](https://jquery.com/download/) ページから jQuery のコピーをダウンロードし、`jquery.min.js` ファイルを HTML ファイルと同じディレクトリに保存します。

> 注：jQuery をダウンロードするとき、ファイル名にはバージョン番号が含まれる場合があります。たとえば `jquery-x.y.z.js` のように。このファイル名を `jquery.js` にリネームするか、`<script>` 要素の `src` 属性をファイル名に合わせて更新することを確認してください。

#### ドキュメント読み込み完了時にコードを起動する

ブラウザがドキュメントの読み込みを完了した後にコードを実行するようにするために、多くの JavaScript プログラマはコードを `onload` 関数にラップします。

```js
window.onload = function () {
  alert("welcome");
};
```

残念ながら、バナー広告を含むすべての画像のダウンロードが完了するまでコードは実行されません。ドキュメントが操作可能になった直後にコードを実行するには、jQuery には [ready イベント](http://api.jquery.com/ready/) と呼ばれる文があります。

```js
$(document).ready(function () {
  // ここにあなたのコードを記述します。
});
```

> 注：jQuery ライブラリは、`window` オブジェクトの `jQuery` と `$` という 2 つのプロパティを介してそのメソッドとプロパティを公開しています。`$` は単に `jQuery` のエイリアスであり、書きやすく速いために頻繁に使用されます。

たとえば、ready イベント内で、リンクにクリックハンドラを追加することができます。

```js
$(document).ready(function () {
  $("button").click(function () {
    $("p").text("Hello jQuery!");
  });
});
```

上記の jQuery コードを、`// ここにあなたのコードを記述します。` と書かれている箇所に HTML ファイルにコピーします。そして、HTML ファイルを保存して、ブラウザでテストページを再読み込みします。

#### 完全な例

以下の例は、上記で説明したクリックハンドリングコードを、直接 HTML `<body>` に埋め込んだものです。実際には、通常はコードを別の JS ファイルに配置し、`<script>` 要素の `src` 属性を使ってページに読み込む方が良い場合が多いです。

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Demo</title>
  </head>
  <body>
    <button>click me</button>
    <p>Hello World</p>
    <script src="jquery.min.js"></script>
    <script>
      $(document).ready(function () {
        $("button").click(function () {
          $("p").text("Hello jQuery!");
        });
      });
    </script>
  </body>
</html>
```

> 右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
