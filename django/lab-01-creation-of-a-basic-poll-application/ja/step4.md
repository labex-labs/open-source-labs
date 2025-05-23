# 投票アプリケーションの作成

これで、「プロジェクト」と呼ばれる環境がセットアップされましたので、作業を始める準備が整いました。

Django で書く各アプリケーションは、特定の規約に従った Python パッケージで構成されます。Django には、アプリケーションの基本的なディレクトリ構造を自動生成するユーティリティが付属しているため、ディレクトリを作成することよりもコードの記述に集中することができます。

> プロジェクトとアプリケーションの違い
> プロジェクトとアプリケーションの違いは何でしょうか？アプリケーションは、何かを行う Web アプリケーションです。たとえば、ブログシステム、公開記録のデータベース、または小さな投票アプリケーションなどです。プロジェクトは、特定の Web サイトの設定とアプリケーションのコレクションです。プロジェクトには複数のアプリケーションが含まれる場合があります。アプリケーションは複数のプロジェクトに含まれる場合があります。

あなたのアプリケーションは、`Pythonパス<tut-searchpath>`上のどこにでも配置できます。このチュートリアルでは、投票アプリケーションを`manage.py`ファイルと同じディレクトリに作成します。これにより、それ自体のトップレベルモジュールとしてインポートできるようになり、`mysite`のサブモジュールではなくなります。

アプリケーションを作成するには、`manage.py`と同じディレクトリにいることを確認して、次のコマンドを入力します。

```bash
cd ~/project/mysite
python manage.py startapp polls
```

これにより、`polls`というディレクトリが作成され、以下のような構成になっています。

```plaintext
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

このディレクトリ構造に投票アプリケーションが配置されます。
