# Flask のセットアップ

Flask を始めるには、インストールして新しいプロジェクトをセットアップする必要があります。以下の手順に従ってください。

1. ターミナルまたはコマンドプロンプトで以下のコマンドを実行して Flask をインストールします。

   ```bash
   pip install flask
   ```

2. 新しいファイルを開き、`app.py` として保存します。

   ```bash
   cd ~/project
   touch app.py
   ```

3. Flask モジュールをインポートし、Flask クラスのインスタンスを作成します。

   ```python
   from flask import Flask

   app = Flask(__name__)
   ```
