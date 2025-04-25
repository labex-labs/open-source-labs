# プロジェクトの作成

Django を初めて使用する場合、初期設定を行う必要があります。具体的には、Django の「プロジェクト」を自動生成する必要があります。これは、Django のインスタンスの設定のコレクションであり、データベース構成、Django 固有のオプション、アプリケーション固有の設定を含みます。

コマンドラインから、コードを保存したいディレクトリに移動してから、次のコマンドを実行します。

```bash
cd ~/project
django-admin startproject mysite
```

これにより、現在のディレクトリに `mysite` ディレクトリが作成されます。

`startproject` が作成したものを見てみましょう。

```plaintext
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

これらのファイルは以下の通りです。

- 外側の `mysite/` ルートディレクトリは、プロジェクトのコンテナです。その名前は Django にとっては重要ではありません。好きな名前に変更できます。
- `manage.py`：Django プロジェクトと様々な方法で対話できるコマンドラインユーティリティ。
- 内側の `mysite/` ディレクトリは、プロジェクトの実際の Python パッケージです。その名前は、その中にある何かをインポートする際に使用する Python パッケージ名です（例：`mysite.urls`）。
- `mysite/__init__.py`：空のファイルで、このディレクトリが Python パッケージとして見なされるように Python に伝えます。
- `mysite/settings.py`：この Django プロジェクトの設定/構成。
- `mysite/urls.py`：この Django プロジェクトの URL 宣言；Django で動作するサイトの「目次」。
- `mysite/asgi.py`：ASGI 互換の Web サーバーがプロジェクトを提供するためのエントリポイント。
- `mysite/wsgi.py`：WSGI 互換の Web サーバーがプロジェクトを提供するためのエントリポイント。
