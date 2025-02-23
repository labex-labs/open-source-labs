# 基本的なルートの作成

Flask のルートは、アプリケーションの URL パターンを定義します。「Hello, World!」のメッセージを表示する基本的なルートを作成しましょう。

1. `app.py` ファイルに以下のコードを追加します。

   ```python
   @app.route("/")
   def hello_world():
       return "Hello, World!"
   ```

2. ファイルを保存します。
