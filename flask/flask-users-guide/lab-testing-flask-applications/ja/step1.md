# テスト環境のセットアップ

Flask アプリケーションのテストを書き始める前に、テスト環境をセットアップする必要があります。以下がその手順です。

1. 次のコマンドを実行して `pytest` フレームワークをインストールします。

   ```bash
   pip install pytest
   ```

2. Flask アプリケーションの `tests` フォルダに `conftest.py` という新しいファイルを作成します。

3. `conftest.py` ファイルで必要なモジュールをインポートします。

   ```python
   import pytest
   from my_app import create_app
   ```

4. アプリケーションインスタンスを作成して構成する `app` という名前のフィクスチャを定義します。

   ```python
   @pytest.fixture()
   def app():
       app = create_app()
       app.config.update({
           "TESTING": True,
       })
       yield app
   ```

   アプリケーションファクトリパターンを使用している場合は、フィクスチャを適切に変更する必要があります。

5. テストクライアントと CLI ランナー用のフィクスチャを定義します。

   ```python
   @pytest.fixture()
   def client(app):
       return app.test_client()

   @pytest.fixture()
   def runner(app):
       return app.test_cli_runner()
   ```
