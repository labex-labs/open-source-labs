# 背景画像の追加

次に、画像用のサブディレクトリを作成します。`polls/static/polls/` ディレクトリ内に `images` サブディレクトリを作成します。このディレクトリ内に、背景として使用したい任意の画像ファイルを追加します。このチュートリアルの目的では、VM の `/tmp/background.png` ディレクトリにある `background.png` という名前のファイルを使用しています。

`/tmp/background.png` を `polls/static/polls/images/background.png` にコピーする必要があります。

その後、スタイルシート (`polls/static/polls/style.css`) に画像への参照を追加します：

```css
body {
  background: white url("images/background.png") no-repeat;
}
```

**Web 8080** タブを再読み込むと、画面の左上に背景が読み込まれているはずです。

![background image example](../assets/20230908-15-39-41-8dGms0NM.png)

> `{% static %}` テンプレートタグは、Django によって生成されない静的ファイル（あなたのスタイルシートのようなもの）では使用できません。静的ファイル同士をリンクする際には常に**相対パス**を使用する必要があります。そうすることで、`STATIC_URL`（`static` テンプレートタグが URL を生成する際に使用する）を変更しても、静的ファイル内の多数のパスを変更する必要がなくなるからです。

これが**基本事項**です。フレームワークに含まれる設定やその他の詳細については、`静的ファイルの使い方 </howto/static-files/index>` と `静的ファイルのリファレンス </ref/contrib/staticfiles>` を参照してください。`静的ファイルの展開 </howto/static-files/deployment>` では、実際のサーバーで静的ファイルを使用する方法について説明されています。

静的ファイルに慣れたら、Django の自動生成された管理サイトをカスタマイズする方法を学ぶために、「Django の管理サイトのカスタマイズ」を読んでください。
