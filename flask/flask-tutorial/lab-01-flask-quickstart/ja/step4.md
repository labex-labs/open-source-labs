# HTML テンプレートの追加

Flask は Jinja2 テンプレートを使用して HTML コンテンツを生成します。テンプレートファイルを作成し、ルートでレンダリングしましょう。

1. プロジェクト内に `templates` という名前の新しいディレクトリを作成します。
2. `templates` ディレクトリの中に、`index.html` という名前の新しいファイルを作成します。
3. `index.html` ファイルを開き、以下の HTML コードを追加します。

   ```html
   <!doctype html>
   <html>
     <head>
       <title>Flask Quickstart</title>
     </head>
     <body>
       <h1>Hello, Flask!</h1>
     </body>
   </html>
   ```

4. `app.py` ファイルを変更して、`index.html` テンプレートをレンダリングするようにします。

   ```python
   from flask import render_template

   @app.route("/")
   def hello_world():
       return render_template("index.html")
   ```
