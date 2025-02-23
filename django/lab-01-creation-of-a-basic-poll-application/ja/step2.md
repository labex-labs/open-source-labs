# プロジェクトの作成

Djangoを初めて使用する場合、初期設定を行う必要があります。具体的には、Djangoの「プロジェクト」を自動生成する必要があります。これは、Djangoのインスタンスの設定のコレクションであり、データベース構成、Django固有のオプション、アプリケーション固有の設定を含みます。

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

- 外側の `mysite/` ルートディレクトリは、プロジェクトのコンテナです。その名前はDjangoにとっては重要ではありません。好きな名前に変更できます。
- `manage.py`：Djangoプロジェクトと様々な方法で対話できるコマンドラインユーティリティ。
- 内側の `mysite/` ディレクトリは、プロジェクトの実際のPythonパッケージです。その名前は、その中にある何かをインポートする際に使用するPythonパッケージ名です（例：`mysite.urls`）。
- `mysite/__init__.py`：空のファイルで、このディレクトリがPythonパッケージとして見なされるようにPythonに伝えます。
- `mysite/settings.py`：このDjangoプロジェクトの設定/構成。
- `mysite/urls.py`：このDjangoプロジェクトのURL宣言；Djangoで動作するサイトの「目次」。
- `mysite/asgi.py`：ASGI互換のWebサーバーがプロジェクトを提供するためのエントリポイント。
- `mysite/wsgi.py`：WSGI互換のWebサーバーがプロジェクトを提供するためのエントリポイント。
