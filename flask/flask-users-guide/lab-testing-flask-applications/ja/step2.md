# テストの作成

テスト環境をセットアップしたので、Flask アプリケーションのテストを作成し始めることができます。作成したい一般的なテストの例をいくつか紹介します。

1. ルートをテストする

   ```python
   def test_hello(client):
       response = client.get("/")
       assert response.status_code == 200
       assert b"Hello, World!" in response.data
   ```

   このテストは、ルート ("/") に対して GET リクエストを送信し、レスポンスのステータスコードが 200 であり、レスポンスデータに文字列 "Hello, World!" が含まれていることを確認します。

2. POST リクエストをテストする

   ```python
   def test_login(client):
       response = client.post("/login", data={"username": "test", "password": "pass"})
       assert response.status_code == 200
       assert b"Logged in successfully" in response.data
   ```

   このテストは、ユーザー名とパスワードを含むフォームデータを使って、ログインルート ("/login") に対して POST リクエストを送信します。レスポンスのステータスコードが 200 であり、レスポンスデータに文字列 "Logged in successfully" が含まれていることを確認します。

3. コマンドをテストする

   ```python
   def test_hello_command(runner):
       result = runner.invoke(args=["hello"])
       assert result.exit_code == 0
       assert "Hello, World!" in result.output
   ```

   このテストは、"hello" という名前のコマンドを実行し、コマンドがコード 0 で終了し、出力に文字列 "Hello, World!" が含まれていることを確認します。
