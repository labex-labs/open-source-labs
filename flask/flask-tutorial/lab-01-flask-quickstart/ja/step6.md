# 動的コンテンツの追加

Flask を使えば、動的コンテンツをテンプレートに渡すことができます。名前パラメータを渡して個別の挨拶を表示するようにルートを変更しましょう。

1. `app.py` ファイルを変更して、ルートで名前パラメータを受け取るようにします。

   ```python
   @app.route("/<name>")
   def hello(name):
       return render_template("index.html", name=name)
   ```

2. `index.html` ファイルを開き、個別の挨拶を表示するように `<h1>` タグを変更します。

   ```html
   <h1>Hello, {{ name }}!</h1>
   ```
